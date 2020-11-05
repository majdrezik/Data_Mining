# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:49:38 2020

@author: ravros
"""
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
from sklearn.metrics import silhouette_samples, silhouette_score

#load file dist1.npy(from lab3_ex011.py)
dist1=np.load('dist1.npy')

#finction clust
def clust(dist,n_cl):
 
#cluster the data into k clusters, specify the k  
    kmeans = KMeans(n_clusters = n_cl)
    kmeans.fit(dist)
    labels = kmeans.labels_ + 1
#show the clustering results  
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(range(len(labels)),labels)
    plt.show()

# calculate the silhouette values  
    silhouette_avg_ = silhouette_score(dist, labels)
    sample_silhouette_values_ = silhouette_samples(dist, labels)
# show the silhouette values 
    plt.plot(sample_silhouette_values_) 
    plt.plot(silhouette_avg_, 'r--')
    plt.title("The silhouette plot for the various clusters.")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")
    y=silhouette_avg_
    xmin=0
    xmax=len(labels)
# The vertical line for average silhouette score of all the values
    plt.hlines(y, xmin, xmax, colors='red', linestyles="--") 
    plt.show()

    print("For n_clusters =", n_cl,
      "The average silhouette_score is:", silhouette_avg_)
    return labels


#K-Means on Dist1 with 2 clusters
labels2 = clust(dist1, 2)

#K-Means on Dist1 but this time, with 3 clusters
labels3 = clust(dist1, 3)

#K-Means on Dist1 but this time, with 4 clusters
labels3 = clust(dist1, 4)



######################### 17 #########################

# K=2 gives a higher average silhouette_score, thus its better than K=3.



######################### 18 #########################
### Done in the other .py file


######################### 19 #########################
# For n_clusters = 2 The average silhouette_score is: 0.3930581688497115
# For n_clusters = 3 The average silhouette_score is: 0.46958267242826374
# For n_clusters = 4 The average silhouette_score is: 0.3197853949784816
 #we can see that 3 number of clusters give us the biggest silhouette_score among the candidate clusters
