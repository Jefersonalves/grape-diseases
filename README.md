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

>## how to obtain the data

For this work, a subset of [kaggle new plant deseases](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset) dataset containing images of grape leaves will be used.

To prepare the dataset, follow the instructions below:

1. Visit [kaggle new plant deseases](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset) and download the dataset.
The dataset will be downloaded as `new-plant-diseases-dataset.zip` file.

2. Unzip the dataset and its subfolder
>```sh
>unzip new-plant-diseases-dataset.zip
>unzip 'New Plant Diseases Dataset(Augmented).zip'
>```


3. Create folders that will contain prepared data
>```sh
>mkdir grape-dataset
>mkdir grape-dataset/train
>mkdir grape-dataset/valid
>```

4. Copy the train images to the prepared folder
>```sh
>cp -r "New Plant Diseases Dataset(Augmented)/train/Grape___Black_rot" grape-dataset/train/black_rot/
>cp -r "New Plant Diseases Dataset(Augmented)/train/Grape___Esca_(Black_Measles)" grape-dataset/train/black_measles/
>cp -r "New Plant Diseases Dataset(Augmented)/train/Grape___healthy" grape-dataset/train/healthy/
>cp -r "New Plant Diseases Dataset(Augmented)/train/Grape___Leaf_blight_(Isariopsis_Leaf_Spot)" grape-dataset/train/leaf_blight/
>```

5. Copy the valid images to the prepared folder
>```sh
>cp -r "New Plant Diseases Dataset(Augmented)/valid/Grape___Black_rot" grape-dataset/valid/black_rot/
>cp -r "New Plant Diseases Dataset(Augmented)/valid/Grape___Esca_(Black_Measles)" grape-dataset/valid/black_measles/
>cp -r "New Plant Diseases Dataset(Augmented)/valid/Grape___healthy" grape-dataset/valid/healthy/
>cp -r "New Plant Diseases Dataset(Augmented)/valid/Grape___Leaf_blight_(Isariopsis_Leaf_Spot)" grape-dataset/valid/leaf_blight/
>```

6. Remove unused folders and files
>```sh
>rm -r "New Plant Diseases Dataset(Augmented)"
>rm test.zip
>rm "New Plant Diseases Dataset(Augmented).zip"
>rm new-plant-diseases-dataset.zip
>```

The final dataset will be the images inside grape-dataset folder