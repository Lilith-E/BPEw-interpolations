import numpy as np
import pandas as pd
import random 
import os



df = pd.read_csv('C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/dataset_cleared_7.csv')


# Define parameters
max_sequence_length = 7
step = 2

#i need to iterate all the rows and all the columns with a step equal to 3

# Iterate through the columns

for i in range(0, len(df.columns)-2, step):
    # Iterate through the rows
    print("column: ", i)
    for j in range(1, len(df) - 1):  # Skip the last row to avoid an out-of-bounds error

        current_frame = df.iloc[j, 37]
        current_video = df.iloc[j, 36]

        
        previous_frame = df.iloc[j - 1, 37]
        previous_video = df.iloc[j - 1, 36]

        if j < len(df) - 1:
            next_frame = df.iloc[j + 1, 37]
            next_video = df.iloc[j + 1, 36]


        #if next_frame - current_frame < 2 and current_video == next_video:
        
        if j < 3 or j >= len(df) - 1 or current_video != previous_video or current_video != next_video or current_frame - previous_frame > 1 or next_frame - current_frame > 1: 
            
            continue
        else:
            
            if random.random() < 0.6:
            #define a random sequence of numbers to be set to 0
                sequence_length = np.random.randint(1, max_sequence_length)
            #define the index where the sequence will start
            
                index = np.random.randint(2, len(df) - sequence_length)

                while df.iloc[index, 36] != df.iloc[index-1, 36] or df.iloc[index, 36] != df.iloc[index+1, 36] or df.iloc[index, 37] - df.iloc[index-1, 37] > 1 or df.iloc[index+1, 37] - df.iloc[index, 37] > 1:
                    index = np.random.randint(2, len(df) - sequence_length)
                    

                
            #Set the sequence to 0 and the corrisponding values of the next 2 columns
            #and count how many elements are next until the next frame
                
                count = 0
                while index+count < len(df)-1 and df.iloc[index, 36] == df.iloc[index+count, 36] and df.iloc[index+count, 37] - df.iloc[index, 37] <= count:
                    count += 1
                
                sequence_length = min(sequence_length, count-1)

                df.iloc[index:index + sequence_length, i:i + step] = 0

                j += sequence_length
    


# Save the modified DataFrame to a new CSV file
df.to_csv('zero_filled_latest.csv', index=False)
