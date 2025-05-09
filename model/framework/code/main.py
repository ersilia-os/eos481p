# imports
import os
import csv
import sys
from grover.predict import grover_predict


if __name__ == '__main__':
    # parse arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # current file directory
    root = os.path.dirname(os.path.abspath(__file__))

    #No need to read the smiles from the main.py , the model will read itself.
    outputs, read_smiles = grover_predict(input_txt_path=input_file, output_path=output_file)

    #check input and output have the same lenght
    input_len = len(read_smiles)
    output_len = len(outputs)
    assert input_len == output_len
    print(output_file)


    columns = []
    with open(os.path.join(root,'cols.txt'), 'r') as file:
        for line in file:
            columns.extend(line.strip().split(','))
    columns = [c.lower() for c in columns]

    # write output in a .csv file
    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(columns)  # header
        for o in outputs:
            writer.writerow(o)