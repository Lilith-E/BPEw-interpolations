import csv

# Variable to store the total count of zeros
total_zeros = 0

# Read the CSV file
with open('C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/zero_filled_latest.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip header row if present
    header = next(reader)
    
    # Determine the number of columns to consider (excluding the last two)
    num_columns = len(header) - 2
    
    # Iterate through each row
    for row in reader:
        for col_idx in range(num_columns):
            try:
                value = float(row[col_idx])
                if value == 0:
                    total_zeros += 1
            except ValueError:
                continue  # Skip non-numeric values

# Print the total count of zero values
print(f'Total number of zeros (excluding the last two columns): {total_zeros}')
