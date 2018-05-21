# Clustering Brisbane CityBike stations

In this task the goal was to cluster Brisbane CityBike stations based on their static geographical information.
Clustering methods were proposed based on the location of the stations (latitude and longitude values).

In order to decide which clustering method to use for the task, a visualization of the data was performed (see 'Brisbane_CityBike_visualization.png' file). Based on the data distribution, the Spectral Clustering method[1] seems an appropriate method to use.

The Spectral Clustering method uses the K-means clustering method on relevant eigenvectors of a Laplacian matrix of the Affinity
matrix of the data. The affinity matrix is a similarity matrix representing a measure of similarity between data points. Here
the K-Neighbors connectivity matrix was used. The method was used to group the data in 2,3 or 4 clusters.

note on scalability:
Spectral Clustering's computational complexity restrict its applicability to very large datasets. Here as we have a small number of data this doesn't constitute an issue. Nevertheless there exist methods that can accelarate the Spectral Clustering method for such cases[3].

A hierarchical clustering method was also tested, specifically the Agglomerative Clustering method[2]. The latter uses a 'bottom-up' approach to cluster the data. At the beginning each observation starts in its own cluster and then the clusters are merged together. The merge strategy can differ, here the 'ward' strategy is used where the goal is to minimize the sum of squared differences within all clusters. This method was also used to group the data in 2,3, or 4 clusters.

The results are shown in 2 different formats:

- Plot showing the clustering results for the 2 different methods and for 3 different numbes of clusters (6 plots in total).
The data points sharing a color are the data points belonging to the same cluster. (see Clustering_Results/clustering_analysis_figure.png)
- Txt files containing the results in two columns separated by a space: station_name station_cluster
The station cluster is a number ranging from 0 to N-1 where N is the nmuber of clusters being used in the method. (see Clustering_Results/ClusteringResults_*_n_clusters=*.txt)

For the clustering problem, the most common method to choose the number of clusters by human input and insight.
Here the data were clustered in 2,3,4 clusters although the best method is to choose a purpose for which we want to divide our data in clusters and then think which is the number of clusters that serves said purpose.

To run the script type: python clustering_test.py /path/to/json/file

## Requirements
a. [Scikit-learn](http://scikit-learn.org/) Scikit-learn is an open source, BSD-licensed library providing tools for
data mining and data analysis.
b. [matplotlib](https://matplotlib.org/) Matplotlib is a plotting library for Python. 


## References

1. [Spectral Clustering](https://people.eecs.berkeley.edu/~malik/papers/SM-ncut.pdf)Shi, J., & Malik, J. (2000). Normalized cuts and image segmentation. IEEE Transactions on pattern analysis and machine intelligence, 22(8), 888-905.
2. [Agglomerative Clustering](https://academic.oup.com/comjnl/article/16/1/30/434805): Sibson, R. (1973). SLINK: an optimally efficient algorithm for the single-link cluster method. The computer journal, 16(1), 30-34. 
3. [CoreCluster](https://arxiv.org/abs/1607.02096) Giatsidis, C., Malliaros, F. D., Tziortziotis, N., Dhanjal, C., Kiagias, E., Thilikos, D. M., & Vazirgiannis, M. (2016). A k-core Decomposition Framework for Graph Clustering. arXiv preprint arXiv:1607.02096.