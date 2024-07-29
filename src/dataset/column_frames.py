import pandas

#usage
df = pandas.read_csv("C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/data.csv")

df['frame'] = 0
frame_number = 0

for i in range(len(df)):
    df.loc[i, 'frame'] = frame_number
    if i < len(df) - 1 and df.loc[i, 'class'] != df.loc[i + 1, 'class']:
        frame_number = 0  # Reset frame number at class change
    else:
        frame_number += 1

# Save the updated dataframe
df.to_csv('dataset_w_frames.csv', index=False)
