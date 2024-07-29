import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/data.csv')

# Filter the dataframe for rows where the 36th column has a value of 0
zero_values_df = df[df.iloc[:, 35] == 0]

# Count the occurrences of each class
zero_class_counts = zero_values_df.iloc[:, 36].value_counts()

total_class_counts = df.iloc[:, 36].value_counts()

percentage_zero_values = (zero_class_counts / total_class_counts) * 100

# Print the results
print("Number of Zero Values and their Percentage per Class:")
print("----------------------------------------------------")
for class_label in zero_class_counts.index:
    zero_count = zero_class_counts[class_label]
    total_count = total_class_counts[class_label]
    percentage = percentage_zero_values[class_label]
    print(f"Class {class_label}:")
    print(f"  Zero Values Count: {zero_count}")
    print(f"  Total Frames Count: {total_count}")
    print(f"  Percentage of Zero Values: {percentage:.2f}%")
    print()

# Prepare data for plotting
labels = percentage_zero_values.index
normalized_values = percentage_zero_values.values

# Plotting the normalized histogram
plt.figure(figsize=(10, 6))
plt.bar(labels, normalized_values, color='purple')
plt.title('Normalized Number of Zero Values for Each Class')
plt.xlabel('Class')
plt.ylabel('Normalized Count of Zero Values (%)')
plt.savefig('init_normalized_histogram.png', dpi=300)
plt.show()