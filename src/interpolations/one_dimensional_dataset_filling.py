import pandas as pd
import os
import sys
from spline_interpolation import spline_interpolation
from inverse_distance import inverse_distance_weighting_with_missing
from interp1d import interp1d_interpolation

# Get the current script's file path
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)
interpolations_directory = parent_directory + '/interpolations'
sys.path.insert(1, interpolations_directory)
g_parent_directory = os.path.dirname(parent_directory)
data_directory = g_parent_directory + '/dataset'

print("Interpolations directory: " + interpolations_directory)

print("Data directory: " + data_directory)





# Read the original CSV file
df = pd.read_csv(data_directory + 'C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/zero_filled_latest.csv')
header = df.columns.values.tolist()

# Initialize variables
current_sequence = []
column_interpolated = []
interpolated_df = pd.DataFrame()
threshold = 2
method = interp1d_interpolation
# Iterate through the columns
for i in range(0, len(header)):
    column_interpolated = []
    current_sequence = []   
    # Iterate through the rows
    print("Processing column " + str(i) + " of " + str(len(header)))
    if i >= 36:
        column_interpolated = df.iloc[:, i].tolist()
        interpolated_df[header[i]] = column_interpolated
        continue

    for j in range(0, len(df) - 1):  # Skip the last row to avoid an out-of-bounds error
        current_frame = df.iloc[j, 37]
        next_frame = df.iloc[j + 1, 37]
        current_video = df.iloc[j, 36]
        next_video = df.iloc[j + 1, 36]
        
        if next_frame - current_frame < 2 and current_video == next_video:
            current_sequence.append(df.iloc[j, i])
        else:
            current_sequence.append(df.iloc[j, i])
            interpolated_sequence = method(current_sequence)
            column_interpolated.extend(interpolated_sequence)
            current_sequence = []

    # Include the last row's value
    current_sequence.append(df.iloc[len(df) - 1, i])
    interpolated_sequence = method(current_sequence)
    column_interpolated.extend(interpolated_sequence)

    print("len(column_interpolated): " + str(len(column_interpolated)))


    interpolated_df[header[i]] = column_interpolated

# Save the interpolated data to a new CSV file
interpolated_df.to_csv(data_directory + '/interpolated_datasets/linear.csv', index=False)




 
