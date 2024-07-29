import csv
import os
import matplotlib.pyplot as plt
import pandas as pd

def process_and_save_sequences(input_csv, output_csv, defined_sequence):
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

        sequences = []
        current_sequence = []

        previous_frame = None 
        previous_video = None 

        for row in reader:
            # Check if all values in the first 35 columns are different from zero
            if all(float(val) != 0.0 for val in row[:35]):
                current_frame = int(row[37]) 
                current_video = row[36] 

                if previous_frame is not None:
                
                    frame_difference = current_frame - previous_frame
                    
                    # Check if the frame difference is less than 2
                    if frame_difference < 2 and current_video == previous_video:
                        current_sequence.append(row)
                    else:
                        if len(current_sequence) >= defined_sequence:
                            sequences.extend(current_sequence)
                        current_sequence = []

                previous_frame = current_frame
                previous_video = current_video

        if len(current_sequence) >= defined_sequence:
            sequences.extend(current_sequence)

    
    with open(output_csv, 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        
        writer.writerow(header)
        
        # Write the selected sequences
        writer.writerows(sequences)

    print(f"Selected sequences have been saved to '{output_csv}'.")

    return len(sequences)

def plot_row_counts(sequence_lengths, row_counts):
    
    plt.plot(sequence_lengths, row_counts, marker='o')
    plt.title('Number of Rows as a Function of sequence length')
    plt.xlabel('Sequence Length')
    plt.ylabel('Number of Rows')
    plt.grid(True)
    plt.savefig('row_counts.png', dpi=300)

input_csv = 'C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/dataset_w_frames.csv'
output_csv_base = 'dataset_cleared_'

sequence_lengths = list(range(3, 11))
row_counts = []

for defined_sequence in sequence_lengths:
    output_csv = f'{output_csv_base}{defined_sequence}.csv'
    num_rows = process_and_save_sequences(input_csv, output_csv, defined_sequence)
    row_counts.append(num_rows)

plot_row_counts(sequence_lengths, row_counts)
