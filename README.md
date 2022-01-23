# 📦 CoastTrain Metadata Plots
[![Last Commit](https://img.shields.io/github/last-commit/dbuscombe-usgs/CoastTrainMetaPlots)](
https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/commits/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/graphs/commit-activity)
[![Wiki](https://img.shields.io/badge/wiki-documentation-forestgreen)](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/wiki)
![GitHub](https://img.shields.io/github/license/dbuscombe-usgs/CoastTrainMetaPlots)
[![Wiki](https://img.shields.io/badge/discussion-active-forestgreen)](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/discussions)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 🌟 Highlights
- jupyter notebooks for visualizing Coast Train data and metadata
- scripts for computing inter-labeler agreement and make montage figures
- works with [Doodler](https://github.com/dbuscombe-usgs/dash_doodler), and [Segmentation Zoo](https://github.com/dbuscombe-usgs/segmentation_zoo)

## ℹ️ Overview
This repository contains jupyter notebooks and python scripts to create the analyses and plots in Buscombe et al. (j prep) "'Coast Train', a 1.2 Billion Pixel Human-Labeled Dataset for Data-Driven Classification of Coastal Environments"


### ✍️ Authors

Package maintainers:
* [@dbuscombe-usgs](https://github.com/dbuscombe-usgs)

## 🚀 Usage

Notebooks that read metadata files in the `metadata` folder can be run by launching a jupyter server in your terminal

```
jupyter notebook
```

Scripts for computing inter-labeler agreement and make montage figures are run from the command line and require modification to point the paths to the locations where you have downloaded the Coast Train npz files to on your local filesystem.



## ⬇️ Installation

We advise creating the [Doodler](https://github.com/dbuscombe-usgs/dash_doodler) conda environment to run the programs. See the [installation instructions](https://github.com/dbuscombe-usgs/dash_doodler#%EF%B8%8F-installation)

