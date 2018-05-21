import sys
import json
import os
from sklearn import cluster
import matplotlib.pyplot as plt


def read_json_data(input_file):

	"""
	Reads data from json file.

	Takes as input the json file and returns a Python list of dictionaries.
	Each dictionary describes an entry.

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

def add_attribute_to_entry(data,attribute_list):

	"""
	Addition of the cluster attribute to each entry.

	Takes as input the data (as a list of dictionaries) and a list containing the values of the new attribute to be added.
	Adds a new attribute 'cluster' to each entry which is the result of a clustering method. Returns all entries as a list
	of dictionaries.

	"""

	attribute_index=0
	for entry in data:

		entry['cluster']=attribute_list[attribute_index]
		attribute_index+=1

	return data

def print_results(data,results_file_name):
	
	"""

	Printing of results in .txt files.

	Takes as input the data (as a list of dictionaries) and the name of the file to be created and
	prints the results of the clustering method. The output file contains two columns separated by a space.
	First column contains the name of the station and second column indicates the cluster that the station
	belongs to according to the clustering method being used.

	"""
	
	with open(results_file_name,'w') as outputfile:
		
		for entry in data:

			outputfile.write(str(entry['name']) +' '+str(entry['class'])+'\n')

def clustering_analysis(data):

	"""
	Clustering of unlabeled data using Spectral and Agglomerative Clustering.

	Takes as input the entry data and provides scatter plots that depict the clustering
	results of the Spectral and Agglomerative Clustering methods. Here the data are grouped
	in 2,3 and 4 clusters.
	"""

	geo_coordinates=get_location_data(data)
	index=0
	clustering_analysis_figure=plt.figure(figsize=(14, 14))

	for n_clusters in (2,3,4):

		spectral = cluster.SpectralClustering(n_clusters=n_clusters,affinity="nearest_neighbors")
		agglomerative = cluster.AgglomerativeClustering(n_clusters=n_clusters)

		clustering_algorithms=( ('Spectral Clustering', spectral),('Agglomerative Clustering', agglomerative) )

		for name,algorithm in clustering_algorithms:
    
		    algorithm.fit(geo_coordinates)
		    y_pred = algorithm.labels_
		    
		    # get results in a scatter plot format
		    index+=1
		    plt.subplot(3,2,index)
		    plt.scatter([x for x,y in geo_coordinates], [y for x,y in geo_coordinates], c=y_pred)
		    plt.title(str(name)+', '+'n_clusters='+str(n_clusters)+'\n')
		    plt.xlabel('Latitude')
		    plt.ylabel('Longitude')
	
	plt.subplots_adjust(hspace=0.5)
	plt.savefig('clustering_analysis_figure.png', format="png")
	plt.close()

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

    # create directory for clustering results

    if not os.path.exists('Clustering_Results'):

    	os.makedirs('Clustering_Results')

    os.chdir('Clustering_Results')

	# perform clustering
    clustering_analysis(data)




