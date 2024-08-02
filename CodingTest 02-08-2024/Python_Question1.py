#1. Write a Python program to read a CSV file and display its contents.

def read_csv(file_path):
    # To Open the CSV file
    with open("C:\\Demo\\abc.csv", mode='r') as file:
        # To Read the contents of the file
        contents = file.readlines()

        # To Iterate over the lines in the file and print each line
        for line in contents:
            #To Strip newline characters and split by commas
            row = line.strip().split(',')
            print(row)

# Replace 'abc.csv' with the path to your CSV file
read_csv('C:\\Demo\\abc.csv')

"""
Output:
['abc']
['1254']
['hjd']
['456']
['11224']
"""
