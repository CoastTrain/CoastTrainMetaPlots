import numpy as np
from glob import glob 
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
from imageio import imread
import tensorflow as tf
import os

def mean_iou_np(y_true, y_pred):
    """
    mean_iou(y_true, y_pred)
    This function computes the mean IoU between `y_true` and `y_pred`: this version is  numpy

    INPUTS:
        * y_true: true masks, one-hot encoded.
            * Inputs are B*W*H*N tensors, with
                B = batch size,
                W = width,
                H = height,
                N = number of classes
        * y_pred: predicted masks, either softmax outputs, or one-hot encoded.
            * Inputs are B*W*H*N tensors, with
                B = batch size,
                W = width,
                H = height,
                N = number of classes
    OPTIONAL INPUTS: None
    GLOBAL INPUTS: None
    OUTPUTS:
        * IoU score [tensor]
    """
    # yt0 = tf.expand_dims(lbl, 0)
    # yp0 = (est_label > 0.5).astype('float32')
    yt0 = y_true[:,:,:,0]
    yp0 = (y_pred[:,:,:,0] > 0.5).astype('float32')
    inter = np.count_nonzero(np.logical_and(np.equal(yt0, 1), np.equal(yp0, 1)))
    union = np.count_nonzero(tf.add(yt0, yp0))
    try:
        iou = np.where(np.equal(union, 0), 1., (inter/union))
    except:
        iou = 1.0

    return iou


#-----------------------------------
def mean_dice_np(y_true, y_pred):
    """
    dice_coef(y_true, y_pred)

    This function computes the mean Dice coefficient between `y_true` and `y_pred`: this version is tensorflow (not numpy) and is used by tensorflow training and evaluation functions

    INPUTS:
        * y_true: true masks, one-hot encoded.
            * Inputs are B*W*H*N tensors, with
                B = batch size,
                W = width,
                H = height,
                N = number of classes
        * y_pred: predicted masks, either softmax outputs, or one-hot encoded.
            * Inputs are B*W*H*N tensors, with
                B = batch size,
                W = width,
                H = height,
                N = number of classes
    OPTIONAL INPUTS: None
    GLOBAL INPUTS: None
    OUTPUTS:
        * Dice score [tensor]
    """
    smooth = 1.
    y_true_f = np.reshape(tf.dtypes.cast(y_true, tf.float32), [-1])
    y_pred_f = np.reshape(tf.dtypes.cast(y_pred, tf.float32), [-1])
    intersection = np.sum(y_true_f * y_pred_f)
    return (2. * intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth)


data_files = [
'datasetA_NAIP/A_naip_meta_served.csv',
'datasetC_S2/C_s2_meta_served.csv'
]

roots = [
'/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetA_NAIP',
'/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetC_S2'
]

plt.figure(figsize=(16,12))

for counter, (data_file, root) in enumerate(zip(data_files, roots)):

    dataset = pd.read_csv(data_file)
    NCLASSES = dataset["num_classes"][0]

    try:
        label_names = ["_".join(a.split("_")[:-2]) for a in dataset["labels"].values]
    except:
        label_names = ["_".join(a.split("_")[:-2]) for a in dataset["label_image_filename"].values]

    num_dupes=len(label_names) - len(np.unique(label_names))
    print("Number of duplicate image pairs: {}".format(num_dupes))

    # get pairs as  a list
    d = defaultdict(list)  # key - number, value - list of indexes

    for i, n in enumerate(label_names):
        d[n].append(i)  # add index to list for this number n
    # duplicates as indices
    dupes = [v for v in d.values() if len(v) > 1]

    #list of image name roots that are pairs
    pairs = [(label_names[d[0]], label_names[d[1]]) for d in dupes]


    kl = tf.keras.losses.KLDivergence()
    kld_scores=[]
    iou_scores=[]; dice_scores=[]
    # for each pair, find the label image pair names, and read in
    for p in pairs: 
        ims = [d for d in dataset["labels"].values if d.startswith(p[0])]
        im1=imread(root+os.sep+ims[0])
        im2=imread(root+os.sep+ims[1])
        # iou_scores.append(iou(im1, im2,NCLASSES))

        nx,ny = im1.shape
        lstack1 = np.zeros((nx,ny,NCLASSES+1))
        lstack1[:,:,:NCLASSES+1] = (np.arange(NCLASSES+1) == 1+im1[...,None]-1).astype(int) #one-hot encode
        lstack2 = np.zeros((nx,ny,NCLASSES+1))
        lstack2[:,:,:NCLASSES+1] = (np.arange(NCLASSES+1) == 1+im2[...,None]-1).astype(int) #one-hot encode

        dice=mean_dice_np(np.expand_dims(lstack1, 0), np.expand_dims(lstack2, 0))
        dice_scores.append(float(dice))

        iou=mean_iou_np(np.expand_dims(lstack1, 0), np.expand_dims(lstack2, 0))
        iou_scores.append(float(iou))

        kld=kl(tf.expand_dims(lstack1, 0), tf.expand_dims(lstack2, 0))
        kld_scores.append(kld.numpy())

    kld_scores = np.array(kld_scores)
    iou_scores = np.array(iou_scores)
    kld_scores[iou_scores == 0.0] = 0.0    
    iou_scores[iou_scores == 0.0] = 1.0

    plt.subplot(2,2,counter+1)
    plt.hexbin(iou_scores,kld_scores, gridsize=16, cmap='Greys', vmin=1)
    cb=plt.colorbar()
    plt.plot(np.mean(iou_scores),np.mean(kld_scores),'kx')
    plt.text(np.mean(iou_scores)-.07,np.mean(kld_scores)+.1,'Mean = ('+str(np.mean(iou_scores))[:4]+','+str(np.mean(kld_scores))[:4]+')', fontsize=8)
    cb.set_label('Number of images')
    plt.xlabel('IoU'); plt.ylabel('Kullback-Leibler Divergence')
    if counter==0:
        plt.title('a) NAIP: {} images, {} classes'.format(num_dupes, NCLASSES), loc='left')
    else:
        plt.title('b) Sentinel-2: {} images, {} classes'.format(num_dupes, NCLASSES), loc='left')

    # plt.show()


plt.savefig('agreement_stats_coasttrain_naip_s2.png', dpi=300, bbox_inches='tight')
plt.close('all')

