import numpy as np
from glob import glob 
import matplotlib.pyplot as plt
from imageio import imread
import pandas as pd
from matplotlib import cm

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetA_NAIP'
data_file = root+'/A_naip_meta_served.csv'
example_image = root+'/images/chunk1_m_3211714_se_11_1_20100503_multiband_ID1.jpg'
example_label = root+'/labels/chunk1_m_3211714_se_11_1_20100503_multiband_ID1_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('a)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('b)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('c)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_naip.png', dpi=300, bbox_inches='tight')
plt.close('all')

###============================================================


root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetJ_NAIP_6classes'

data_file = root+'/J_naip_6class_meta_served.csv'
example_image = root+'/images/chunk9_m_3411936_se_11_1_20120505_multiband_ID3.jpg'
example_label = root+'/labels/chunk9_m_3411936_se_11_1_20120505_multiband_ID3_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
classes[3] = 'vegetated_ground'
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('d)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('e)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('f)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_naip6class.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetB_quadrangles'
data_file = root+'/B_quads_gulf_meta_served.csv'
example_image = root+'/images/crms0354_2012_ID5.jpg'
example_label = root+'/labels/crms0354_2012_ID5_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('g)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('h)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('i)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_quads.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetG_madeira'
data_file = root+'/G_madeira_meta_served.csv'
example_image = root+'/images/20180124_MadeiraBeachFL_ortho_5cm_09_11_ID3.jpg'
example_label = root+'/labels/20180124_MadeiraBeachFL_ortho_5cm_09_11_ID3_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('j)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('k)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('l)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_madeira.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================


root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetH_dauphin'

data_file = root+'/H_dauphin_meta_served.csv'
example_image = root+'/images/2018-12-LittleDauphinIsland-ortho-rgb-5cm_03_03_ID3.jpg'
example_label = root+'/labels/2018-12-LittleDauphinIsland-ortho-rgb-5cm_03_03_ID3_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('m)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('n)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('o)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_dauphin.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================


root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetI_sandwich'

data_file = root+'/I_sandwich_metadata_served.csv'
example_image = root+'/images/20160921_SandwichTNB_Ortho_5cm_UTM19N_NAVD88_cog_5cm_clipped_05_03_ID2.jpg'
example_label = root+'/labels/20160921_SandwichTNB_Ortho_5cm_UTM19N_NAVD88_cog_5cm_clipped_05_03_ID2_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('p)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('q)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('r)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_sandwich.png', dpi=300, bbox_inches='tight')
plt.close('all')



###=========================================================
###=========================================================
###=========================================================
###=========================================================
###=========================================================
###=========================================================

###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetC_S2'

data_file = root+'/C_s2_meta_served.csv'
example_image = root+'/images/chunk1_20190716T183921_20190716T184625_T11SKT.TCI_RGB_site51_ID6.jpg'
example_label = root+'/labels/chunk1_20190716T183921_20190716T184625_T11SKT.TCI_RGB_site51_ID6_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('a)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('b)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('c)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_s2.png', dpi=300, bbox_inches='tight')
plt.close('all')



###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetD_S2_4classes'

data_file = root+'/D_s2_4classes_meta_served.csv'
example_image = root+'/images/20200308T154101_20200308T154114_T18SVE_lr_ID1.jpg'
example_label = root+'/labels/20200308T154101_20200308T154114_T18SVE_lr_ID1_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('d)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('e)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('f)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_s2_4class.png', dpi=300, bbox_inches='tight')
plt.close('all')




###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetE_L8'

data_file = root+'/E_L8_meta_all_served.csv'
example_image = root+'/images/galvestonwest_2020-04-30-16-50-30_L8_rgb_ID4.jpg'
example_label = root+'/labels/galvestonwest_2020-04-30-16-50-30_L8_rgb_ID4_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('g)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('h)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('i)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_l8.png', dpi=300, bbox_inches='tight')
plt.close('all')



###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetF_l8elwha'

data_file = root+'/F_elwha_l8_served.csv'
example_image = root+'/images/2015-11-21-19-01-58_L8_rgb_ID2.jpg'
example_label = root+'/labels/2015-11-21-19-01-58_L8_rgb_ID2_label.jpg'

dataset = pd.read_csv(data_file)
NCLASSES = dataset["num_classes"][0]
classes = dataset["classes_array"][0]
classes = [c.strip().replace("'","") for c in classes.split(",")]
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('j)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('k)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('l)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_l8elwha.png', dpi=300, bbox_inches='tight')
plt.close('all')

#!montage -border 0 -geometry 4000x+0+0 -tile 1x6 example_coasttrain_naip.png example_coasttrain_naip6class.png example_coasttrain_quads.png example_coasttrain_madeira.png example_coasttrain_dauphin.png example_coasttrain_sandwich.png example_coasttrain_all_orthos.png 

#!montage -border 0 -geometry 4000x+0+0 -tile 1x6 example_coasttrain_s2.png example_coasttrain_s2_4class.png example_coasttrain_l8.png example_coasttrain_l8elwha.png example_coasttrain_all_satellites.png