import os
import cv2
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

    def get_images_classes(self):
        class_files = []
        for c in self.get_classes_infos():
            files = os.listdir(c['train_path'])
            class_files.extend([{"image": file, "class": c["class"]} for file in files])
        return pd.DataFrame(class_files)