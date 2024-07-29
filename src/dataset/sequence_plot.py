import matplotlib.pyplot as plt
import csv

# Initialize dictionary to track sequence lengths
sequence_lengths_count = {i: 0 for i in range(1, 51)}  # Initialize counts for sequence lengths 1 to 10

# Read the CSV file and count sequences of zeros vertically in each column
with open('C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/zero_filled_latest.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    data = list(reader)
    
    num_columns = len(data[0]) - 2  
    for col_idx in range(0,num_columns,2):
        current_sequence_length = 0
        
        for row_idx in range(len(data)):
            try:
                value = float(data[row_idx][col_idx])
                if value == 0:
                    current_sequence_length += 1
                else:
                    if current_sequence_length > 0:
                        if current_sequence_length <= 50:
                            sequence_lengths_count[current_sequence_length] += 1
                    current_sequence_length = 0
            except ValueError:
                continue 

        if current_sequence_length > 0:
            if current_sequence_length <= 10:
                sequence_lengths_count[current_sequence_length] += 1

plt.figure(figsize=(10, 6))
plt.bar(sequence_lengths_count.keys(), sequence_lengths_count.values(), width=0.8, align='center', edgecolor='black', color='purple')
plt.xlabel('Length of Sequences of Zeros')
plt.ylabel('Occurrences')
plt.title('Histogram of Sequence Lengths of Zeros')
plt.xticks(range(1, 51))
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.savefig('length_occurrences.png', dpi=300)
