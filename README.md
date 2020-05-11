# plant-diseases

Crop diseases can cause various damages and economic losses for the
farmer. In addition to the degradation of plants, they are also responsible for
food infections. In this perspective, agricultural producers can benefit from
advances in computer vision and machine learning aimed at detecting diseases
in plants.
In particular, grape plantations are commonly affected by three diseases, the Black measles, the Black rot and the Isariopsis leaf spot.
This repository contains a model to analyze leaf images of vines and identify whether the leaf is healthy
or has any of these diseases. It is desired to correctly identify and classify
leaf images in three classes of diseases and an absent class of diseases.

# dataset

The [PlantVillage Dataset](https://github.com/spMohanty/PlantVillage-Dataset) contains images of leaves from different
healthy and diseased plant species. An [augmented version](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset) of the dataset was
published on the Kaggle platform, in this version transformations of the original dataset images were added.
For this work, a subset of this augmented dataset containing images
of grape leaves will be used. The base contains a total of 7222 vine leaf images
for training and 1805 for validation. The images are grouped into 4 distinct
classes: healthy leaves (`healthy`), leaves with Black rot desease (`black_rot`),
leaves with Black measles desease (`black_measles`) and leaves with Leaf blight
desease (`leaf_blight`).