import sys
import json
import os
from sklearn import cluster
import matplotlib.pyplot as plt


def read_json_data(input_file):

	"""
	Read data from json file.

	Takes as input the json file and returns a Python list of all the entries.

	"""

	with open(input_file) as json_data:

		data = json.load(json_data)
	
	return data


if __name__ == "__main__":

    if not len(sys.argv) == 2:
        print ('Wrong arguments')
    else:
        data_file= sys.argv[1]