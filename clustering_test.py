import sys
import json
import os
from sklearn import cluster
import matplotlib.pyplot as plt



if __name__ == "__main__":

    if not len(sys.argv) == 2:
        print ('Wrong arguments')
    else:
        data_file= sys.argv[1]