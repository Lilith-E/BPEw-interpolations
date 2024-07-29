import csv 
import pandas 


with open('C:/Users/eleno/Desktop/BodyPoseDigital/BPEw-interpolations/dataset/zero_filled_latest.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    #retrieve the index of the row that has all zeros
    for row in reader:
        if all(float(i) == 0 for i in row[:-2]):
            print(f'Row with all zeros: {row}')
            break
    
    