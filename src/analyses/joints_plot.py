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
df_nn = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/nearest.csv")
df_gt = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/dataset_cleared_7.csv")
df_idw = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/idw.csv")
df_linear = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/linear.csv")
df_spline = pd.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/interpolated_datasets/spline_interpolated.csv")


n_row = 739

row_nn = df_nn.iloc[n_row]
row_gt = df_gt.iloc[n_row]
row_idw = df_idw.iloc[n_row]
row_linear = df_linear.iloc[n_row]
row_spline = df_spline.iloc[n_row]

#all the columns are x,y and c values, use the x and y values to create a point into a plot 

x_nn = row_nn[0:][:35:2]
y_nn = row_nn[1:][:35:2]
y_nn = 1 - y_nn

x_idw = row_idw[0:][:35:2]
y_idw = row_idw[1:][:35:2]
y_idw = 1 - y_idw

x_linear = row_linear[0:][:35:2]
y_linear = row_linear[1:][:35:2]
y_linear = 1 - y_linear

x_spline = row_spline[0:][:35:2]
y_spline = row_spline[1:][:35:2]
y_spline = 1 - y_spline


x_gt = row_gt[0:][:35:2]
y_gt = row_gt[1:][:35:2]
y_gt = 1 - y_gt


colors = plt.cm.jet(np.linspace(0, 1, 18))
plt.scatter(x_gt, y_gt, c=colors, label='Ground Truth')
#plt.scatter(x_nn, y_nn, c=colors, marker='x', s=100, label='Nearest Neighbour') 
#plt.scatter(x_idw, y_idw, c=colors, marker='x', s=100, label='IDW')
#plt.scatter(x_linear, y_linear, c=colors, marker='x', s=100, label='Linear')
plt.scatter(x_spline, y_spline, c=colors, marker='x', s=100, label='Spline')


plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.colorbar()

#save the plot as a png file 
plt.savefig('spline_joints_plot.png', dpi=300)







