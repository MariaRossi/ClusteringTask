import sys
import json
import os
from sklearn import cluster
import matplotlib.pyplot as plt


def read_json_data(input_file):

	"""
	Reads data from json file.

	Takes as input the json file and returns a Python list of all the entries.

	"""

	with open(input_file) as json_data:

		data = json.load(json_data)
	
	return data

def get_location_data(data):

    """
	Gets the location data from all the entries.

	Takes as input a list containing all entries and returns a list of (latitude,longitude) pairs.

	"""
    geo_coordinates=[]
    for entry in data:

    	latitude=entry['latitude']
    	longitude=entry['longitude']
    	geo_coordinates.append([latitude,longitude])

    return geo_coordinates



if __name__ == "__main__":

    if not len(sys.argv) == 2:
        print ('Wrong arguments')
    else:
        data_file= sys.argv[1]

    # read data
    data=read_json_data(data_file)
    geo_coordinates=get_location_data(data)

	# plot data points based on the location of each entry
    plt.scatter([x for x,y in geo_coordinates],[y for x,y in geo_coordinates])
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Brisbane_CityBike')
    plt.savefig('Brisbane_CityBike_visualization.png', format="png")
    plt.close()

    # create directory for clsutering results

    if not os.path.exists('Clustering_Results'):

    	os.makedirs('Clustering_Results')
	
	os.chdir('Clustering_Results')

