import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt 
import os 
# Get the current script's file path
script_path = os.path.abspath(__file__)
# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)
g_parent_directory = os.path.dirname(parent_directory)
data_directory = g_parent_directory + '/dataset/'

# Load the dataset
df_nn = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/interpolated_datasets/nearest.csv")
df_gt = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/dataset_cleared_7.csv")
df_idw = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/interpolated_datasets/idw.csv")
df_linear = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/interpolated_datasets/linear.csv")
df_spline = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/interpolated_datasets/spline_interpolated.csv")

#731 - 738 - 739 - 740 - 746 - 747 - 750

# Specify the row and column indices
n_row = 739

col_x = 18  
col_y = 19  

# Extract the values for the specified row and columns
x_gt_current = df_gt.iloc[n_row, col_x]
y_gt_current = 1 - df_gt.iloc[n_row, col_y]

x_nn = df_nn.iloc[n_row, col_x]
y_nn = 1 - df_nn.iloc[n_row, col_y]

x_idw = df_idw.iloc[n_row, col_x]
y_idw = 1 - df_idw.iloc[n_row, col_y]

x_linear = df_linear.iloc[n_row, col_x]
y_linear = 1 - df_linear.iloc[n_row, col_y]

x_spline = df_spline.iloc[n_row, col_x]
y_spline = 1 - df_spline.iloc[n_row, col_y]

colors = plt.cm.jet(np.linspace(0, 1, 6))

plt.scatter(x_gt_current, y_gt_current, color='black', marker='o', s=100, label='Ground Truth')
plt.scatter(x_nn, y_nn, color=[colors[5]], marker='x', s=100, label='Nearest')
plt.scatter(x_idw, y_idw, color=[colors[1]], marker='x', s=100, label='Idw')
plt.scatter(x_linear, y_linear, color=[colors[2]], marker='x', s=100, label='Linear')
plt.scatter(x_spline, y_spline, color=[colors[3]], marker='x', s=100, label='Spline')

plt.legend()
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Scatter Plot of 18th and 19th Column (Row 739)')
plt.grid(True)
plt.savefig('single_point_plot.png', dpi=300)






