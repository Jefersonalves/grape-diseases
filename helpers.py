import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataExplorator:
    def __init__(self):
        self.grape_dataset_path_ = os.path.join("grape-dataset")
        self.grape_dataset_train_path_ = os.path.join(self.grape_dataset_path_, "train")
        self.grape_dataset_valid_path_ = os.path.join(self.grape_dataset_path_, "valid")
        self.classes_ = ["black_measles", "black_rot", "healthy", "leaf_blight"]

    def get_classes_infos(self):
        classes_infos = []
        for c in self.classes_:
            train_path = os.path.join(self.grape_dataset_train_path_, c)
            valid_path = os.path.join(self.grape_dataset_valid_path_, c)
            train_size = len(os.listdir(train_path))
            valid_size = len(os.listdir(valid_path))
            classes_infos.append({
                "class": c,
                "train_path": train_path,
                "valid_path": valid_path,
                "train_size": train_size,
                "valid_size": valid_size}
            )

        return classes_infos

    def get_train_images(self):
        class_files = []
        for c in self.get_classes_infos():
            files = os.listdir(c['train_path'])
            class_files.extend([{"image": os.path.join(c['train_path'], file), "class": c["class"]} for file in files])
        return pd.DataFrame(class_files)

    def get_valid_images(self):
        class_files = []
        for c in self.get_classes_infos():
            files = os.listdir(c['valid_path'])
            class_files.extend([{"image": os.path.join(c['valid_path'], file), "class": c["class"]} for file in files])
        return pd.DataFrame(class_files)

class ImagePloter:
    def __init__(self):
        pass

    def plot_rgb(self, img_path):
        img = cv2.imread(img_path)

        B = img[:,:,0]
        G = img[:,:,1]
        R = img[:,:,2]

        plt.figure(figsize=(16,16))
        plt.subplot(1,4,1)
        plt.title('Image')
        plt.imshow(img[:,:,::-1])

        plt.gray()

        plt.subplot(1,4,4)
        plt.title('Channel R')
        plt.imshow(R)

        plt.subplot(1,4,3)
        plt.title('Channel G')
        plt.imshow(G)

        plt.subplot(1,4,2)
        plt.title('Channel B')
        plt.imshow(B)
        
        plt.show()
        plt.close('all')

    def plot_hsv(self, img_path):
        img = cv2.imread(img_path)

        plt.figure(figsize=(16,16))
        plt.subplot(1,4,1)
        plt.title('Image')
        plt.imshow(img[:,:,::-1])
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
        H = img[:,:,0]
        S = img[:,:,1]
        V = img[:,:,2]

        plt.gray()
        plt.subplot(1,4,2)
        plt.title('Channel H')
        plt.imshow(H)

        plt.subplot(1,4,3)
        plt.title('Channel S')
        plt.imshow(S)

        plt.subplot(1,4,4)
        plt.title('Channel V')
        plt.imshow(V)
        
        plt.show()
        plt.close('all')