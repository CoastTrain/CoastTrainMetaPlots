
import numpy as np
from glob import glob 
import matplotlib.pyplot as plt
from imageio import imread
import pandas as pd
from matplotlib import cm


config = { 
"aliases":
      {
        "water": "water",
        "sediment_plume": "water",
        "whitewater": "whitewater",
        "surf":"whitewater",
        "sediment": "sediment",
        "sand":"sediment", 
        "gravel":"sediment",
        "gravel_shell": "sediment",
        "cobble_boulder": "sediment",
        "mud_silt": "sediment",
        "developed": "developed",
        "dev":"developed",
        "coastal_defense":"developed",
        "pavement_road": "developed",
        "other_anthro": "developed",
        "vehicles": "developed",
        "development":"developed",
        "buildings":"developed",  
        "other_natural_terrain": "natural_terrain",
        "other_bare_natural_terrain":"natural_terrain",
        "bare_ground":"natural_terrain",
        "bedrock":"natural_terrain",
        "non-vegetated-wet":"natural_terrain",
        "non-vegetated-dry":"natural_terrain",
        "non_vegetated_dry":"natural_terrain",
        "non_vegetated_wet":"natural_terrain",
        "agricultural":"natural_terrain",
        "bare_ground":"natural_terrain", 
        "vegetated":"vegetation",    
        "vegetated_surface":"vegetation",
        "vegtated_ground":"vegetation",
        "terrestrial_vegetation":"vegetation",
        "marsh_vegetation":"vegetation",
        "herbaceous vegetation":"vegetation",
        "herbaceous_veg":"vegetation",
        "woody vegetation":"vegetation",
        "woody_veg":"vegetation",
        "unknown":"other",
        "unusual":"other",
        "nodata":"other",
        "people": "other",
        "ice_snow": "other",
        "cloud": "other",
        "other":"other"
  },
  "classes": ["water", "whitewater", "sediment", "other"],
  "super_classes": ["water", "whitewater", "sediment","developed", "vegetation","natural_terrain", "other"],
  "direc": "/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetD_S2_4classes/npz"
}


for k in config.keys():
    exec(k+'=config["'+k+'"]')


###=============================================================


root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetA_NAIP'
example_image = root+'/images/chunk1_m_3211714_se_11_1_20100503_multiband_ID1.jpg'
example_label = root+'/labels_remap/chunk1_m_3211714_se_11_1_20100503_multiband_ID1_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('a)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('b)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('c)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_naip_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')

###============================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetJ_NAIP_6classes'
example_image = root+'/images/chunk9_m_3411936_se_11_1_20120505_multiband_ID3.jpg'
example_label = root+'/labels_remap/chunk9_m_3411936_se_11_1_20120505_multiband_ID3_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('d)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('e)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('f)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_naip6class_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')

###============================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetB_quadrangles'
example_image = root+'/images/crms0354_2012_ID5.jpg'
example_label = root+'/labels_remap/crms0354_2012_ID5_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('g)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('h)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('i)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_quads_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetG_madeira'
example_image = root+'/images/20180124_MadeiraBeachFL_ortho_5cm_09_11_ID3.jpg'
example_label = root+'/labels_remap/20180124_MadeiraBeachFL_ortho_5cm_09_11_ID3_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('j)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('k)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('l)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_madeira_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================


root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetH_dauphin'

example_image = root+'/images/2018-12-LittleDauphinIsland-ortho-rgb-5cm_03_03_ID3.jpg'
example_label = root+'/labels_remap/2018-12-LittleDauphinIsland-ortho-rgb-5cm_03_03_ID3_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('m)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('n)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('o)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_dauphin_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')



###============================================================


root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetI_sandwich'

example_image = root+'/images/20160921_SandwichTNB_Ortho_5cm_UTM19N_NAVD88_cog_5cm_clipped_05_03_ID2.jpg'
example_label = root+'/labels_remap/20160921_SandwichTNB_Ortho_5cm_UTM19N_NAVD88_cog_5cm_clipped_05_03_ID2_remap_label.jpg'
classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('p)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('q)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('r)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_sandwich_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')



###=========================================================
###=========================================================
###=========================================================
###=========================================================
###=========================================================
###=========================================================

###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetC_S2'
example_image = root+'/images/chunk1_20190716T183921_20190716T184625_T11SKT.TCI_RGB_site51_ID6.jpg'
example_label = root+'/labels_remap/chunk1_20190716T183921_20190716T184625_T11SKT.TCI_RGB_site51_ID6_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('a)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('b)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('c)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_s2_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')



###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetD_S2_4classes'
example_image = root+'/images/20200308T154101_20200308T154114_T18SVE_lr_ID1.jpg'
example_label = root+'/labels_remap/20200308T154101_20200308T154114_T18SVE_lr_ID1_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('d)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('e)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('f)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_s2_4class_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')




###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetE_L8'
example_image = root+'/images/galvestonwest_2020-04-30-16-50-30_L8_rgb_ID4.jpg'
example_label = root+'/labels_remap/galvestonwest_2020-04-30-16-50-30_L8_rgb_ID4_remap_label.jpg'

classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('g)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('h)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('i)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_l8_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')



###=========================================================

root = '/media/marda/TWOTB/USGS/SOFTWARE/Projects/UNets/coast_train_datasets_anonymous_served/datasetF_l8elwha'

example_image = root+'/images/2015-11-21-19-01-58_L8_rgb_ID2.jpg'
example_label = root+'/labels_remap/2015-11-21-19-01-58_L8_rgb_ID2_remap_label.jpg'
classes = ['null']+super_classes
NCLASSES = len(classes)
cmap = cm.get_cmap('tab20', NCLASSES)


plt.figure(figsize=(16,8))
plt.subplot(131)
plt.imshow(imread(example_image))
cb=plt.colorbar(shrink=0.5)
plt.title('j)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(132)
plt.imshow(imread(example_label),cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
cb.set_label('Classes')
cb.ax.set_yticklabels(['' for c in classes])
plt.title('k)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')

plt.subplot(133)
plt.imshow(imread(example_image))
plt.imshow(imread(example_label),alpha=0.4,cmap=cmap, vmin=0,vmax=NCLASSES)
cb=plt.colorbar(shrink=0.5, ticks=np.arange(NCLASSES))
# cb.set_label('Classes')
cb.ax.set_yticklabels(classes)
plt.title('l)', loc='left')
plt.xlabel('Number of pixels')
plt.ylabel('Number of pixels')
# plt.show()
plt.savefig('../script_plots/example_coasttrain_l8elwha_remapped.png', dpi=300, bbox_inches='tight')
plt.close('all')


#!montage -border 0 -geometry 4000x+0+0 -tile 1x6 example_coasttrain_naip_remapped.png example_coasttrain_naip6class_remapped.png example_coasttrain_quads_remapped.png example_coasttrain_madeira_remapped.png example_coasttrain_dauphin_remapped.png example_coasttrain_sandwich_remapped.png example_coasttrain_all_orthos_remapped.png 

#!montage -border 0 -geometry 4000x+0+0 -tile 1x6 example_coasttrain_s2_remapped.png example_coasttrain_s2_4class_remapped.png example_coasttrain_l8_remapped.png example_coasttrain_l8elwha_remapped.png example_coasttrain_all_satellites_remapped.png