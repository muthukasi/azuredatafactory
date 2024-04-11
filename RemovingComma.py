import csv
import re

# Specify the path to your input file
#input_file_path = 'C:/Users/muthukasi/OneDrive - Microsoft/Documents/Sample_File_FieldStack_10.csv'
input_file_path = r'C:\Users\muthukasi\OneDrive - Microsoft\Documents\Sample_File_FieldStack_10.csv'
print(input_file_path)

# Read the input data from the file
with open(input_file_path, 'r') as file:
    input_data = file.read()
    print(input_data)
    
# Split the input data into fields
fields = re.split(',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', input_data)

# Replace commas with pipes within double-quoted fields
modified_fields = [field.replace(',', '|') if '"' in field else field for field in fields]

# Reshape modified fields into a list of lists for csv.writer
modified_rows = [modified_fields[i:i+25] for i in range(0, len(modified_fields), 25)]

# Specify the path for the output file
output_file_path = 'C:/Users/muthukasi/OneDrive - Microsoft/Documents/Output_File_FieldStack_10.csv'

# Write the modified CSV data to the output file
with open(output_file_path, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(modified_rows)

print(f'Modified CSV data written to {output_file_path}')
