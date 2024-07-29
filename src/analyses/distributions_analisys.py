import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde
import os 

# Get the current script's file path
script_path = os.path.abspath(__file__)
# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)
g_parent_directory = os.path.dirname(parent_directory)
data_directory = g_parent_directory + '/data/'


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y

def plotting_ecdf(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    plt.figure()
    plt.plot(x1, y1, '-', label='IDW')
    plt.plot(x2, y2, '-', label='Linear')
    plt.plot(x3, y3, '-.', label='Nearest')
    plt.plot(x4, y4, '-', label='Spline')
    plt.plot(x5, y5, '-', label='Ground Truth')

    plt.xlabel('X Values')
    plt.ylabel('ECDF')
    plt.xlim(0.00040, 0.0005)
    plt.ylim(0.32, 0.48)
    plt.legend()
    plt.savefig('ecdf_zoomed.png', dpi=300)
    plt.close()


data_directory = g_parent_directory + '/dataset/'

# Load datasets
df_gt = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/dataset_cleared_7.csv")
df_nearest = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/nearest.csv")
df_idw = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/idw.csv")
df_linear = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/linear.csv")
df_spline = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/spline_interpolated.csv")


joint = 8
x_gt_values = df_gt.iloc[1:, joint]
y_gt_values = 1 - df_gt.iloc[1:, joint+1]

x_idw_values = df_idw.iloc[1:, joint]
y_idw_values = 1 - df_idw.iloc[1:, joint+1]

x_linear_values = df_linear.iloc[1:, joint]
y_linear_values = 1 - df_linear.iloc[1:, joint+1]

x_spline_values = df_spline.iloc[1:, joint]
y_spline_values = 1 - df_spline.iloc[1:, joint+1]

x_nearest_values = df_nearest.iloc[1:, joint]
y_nearest_values = 1 - df_nearest.iloc[1:, joint+1]

frames = np.linspace(0, len(x_gt_values), len(x_gt_values))

plt.figure()
plt.plot(frames, y_gt_values, '--', label='Ground Truth')
plt.plot(frames, y_idw_values, '-', label='IDW')
plt.plot(frames, y_linear_values, '-.', label='Linear')
plt.plot(frames, y_spline_values, '-', label='Spline')
plt.plot(frames, y_nearest_values, '-', label='Nearest')

# Add labels and a legend
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.xlim(1600, 1790)
plt.ylim(0.55, 0.77)
plt.savefig('scatter_zoomed.png', dpi=300)
plt.close()

# Normalize the x and y values
def normalize(values):
    return np.array(values) / np.sum(values)

x_gt_values = normalize(x_gt_values)
y_gt_values = normalize(y_gt_values)

x_idw_values = normalize(x_idw_values)
y_idw_values = normalize(y_idw_values)

x_linear_values = normalize(x_linear_values)
y_linear_values = normalize(y_linear_values)

x_spline_values = normalize(x_spline_values)
y_spline_values = normalize(y_spline_values)

x_nearest_values = normalize(x_nearest_values)
y_nearest_values = normalize(y_nearest_values)

# Calculate the ECDF for all the interpolations
x_gt, y_gt = ecdf(x_gt_values)
x_idw, y_idw = ecdf(x_idw_values)
x_linear, y_linear = ecdf(x_linear_values)
x_spline, y_spline = ecdf(x_spline_values)
x_nearest, y_nearest = ecdf(x_nearest_values)

# Plot ECDFs
plotting_ecdf(x_idw, y_idw, x_linear, y_linear, x_nearest, y_nearest, x_spline, y_spline, x_gt, y_gt)

# Plot KDE for all the interpolations
plt.figure()
kde1 = gaussian_kde(x_gt_values, bw_method='silverman')
kde3 = gaussian_kde(x_idw_values, bw_method='silverman')
kde4 = gaussian_kde(x_linear_values, bw_method='silverman')
kde5 = gaussian_kde(x_spline_values, bw_method='silverman')
kde7 = gaussian_kde(x_nearest_values, bw_method='silverman')

dist_space = np.linspace(min(x_gt_values), max(x_gt_values), 100)

plt.plot(dist_space, kde1(dist_space), '-', label='Ground Truth')
plt.plot(dist_space, kde3(dist_space), '-', label='IDW')
plt.plot(dist_space, kde4(dist_space), '-.', label='Linear')
plt.plot(dist_space, kde5(dist_space), '-', label='Spline')
plt.plot(dist_space, kde7(dist_space), '-', label='Nearest')

plt.xlabel('X Values')
plt.ylabel('Density')
plt.legend()
plt.xlim(0.0004, 0.00055)
plt.ylim(1350, 1700)
plt.savefig('kde2_zoomed.png', dpi=300)
plt.close()
