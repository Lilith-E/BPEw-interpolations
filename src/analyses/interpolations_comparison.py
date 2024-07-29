import numpy as np
import pandas as pd
import os
from downsampling import downsample_dataset
from evaluation_metrics import evaluation_metrics

# Function to read a dataset and flatten all columns into a list
def flatten_dataset(file_path):
    df = pd.read_csv(file_path)
    flat_list = df.values.flatten().tolist()
    return flat_list


# Define dataset paths
gt_dataset = "C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/dataset_cleared_7.csv"
zero_filled_dataset ="C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/zero_filled_latest.csv"
idw_dataset = "C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/idw.csv"
linear_dataset = "C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/linear.csv"
spline_dataset = "C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/spline_interpolated.csv"
nn_dataset = "C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/nearest.csv"

# Downsample datasets
gt_list = downsample_dataset(zero_filled_dataset, gt_dataset)
idw_list = downsample_dataset(zero_filled_dataset, idw_dataset)
linear_list = downsample_dataset(zero_filled_dataset, linear_dataset)
spline_list = downsample_dataset(zero_filled_dataset, spline_dataset)
nn_list = downsample_dataset(zero_filled_dataset, nn_dataset)

# Define your lists (gt_list, idw_list, linear_list, etc.)
datasets = {
    "IDW": idw_list,
    "Linear": linear_list,
    "Spline": spline_list,
    "Nearest": nn_list
}

for dataset_name, dataset_list in datasets.items():
    euclid, rmse, bhattacharyya = evaluation_metrics(gt_list, dataset_list)
    # Multiply RMSE, Bhattacharyya, and Cross Entropy values by 1000 to get a better understanding of the values
    rmse *= 1000
    bhattacharyya *= 1000
    
    print("Dataset:", dataset_name)
    print("Euclidean Distance:", euclid)
    print("Root Mean Squared Error (scaled):", rmse)
    print("Bhattacharyya Distance (scaled):", bhattacharyya)
    print("\n")
