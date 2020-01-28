# USAGE
# python cluster_faces.py --encodings encodings.pickle

# import the necessary packages
from sklearn.cluster import DBSCAN, KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, OPTICS,Birch, estimate_bandwidth
from sklearn import metrics
from sklearn.metrics import accuracy_score
from imutils import build_montages
import numpy as np
import argparse
import pickle
import cv2
import time #medir tempo
import os
import shutil
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from itertools import cycle
from sklearn.decomposition import PCA as sklearnPCA


#carrega os encodings do disco
data = pickle.loads(open("28_01_2020_15_57_36_", "rb").read())

#os coloca em um vetor numpy
data = np.array(data)

#print(data)


#extrai os encodings, colocando-os em uma lista
encodings = [d["encoding"] for d in data]
centers = [[1, 1], [-1, -1], [1, -1]]
AAAA = len(encodings)
print(AAAA)





bandwidth = estimate_bandwidth(encodings, quantile=0.1, n_samples=AAAA)

print(bandwidth)
ms = MeanShift(bandwidth=0.48)
ms.fit(encodings)

labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)




plt.figure(1)
plt.clf()

X=np.asarray(encodings)

#print(cluster_centers)
#print(type(cluster_centers))


pca = sklearnPCA(n_components=2)
X= pca.fit(encodings).transform(encodings)

cluster_center = pca.fit(cluster_centers).transform(cluster_centers)

#print(X)
print (cluster_center)



h = metrics.silhouette_score(encodings, labels)

#b = metrics.silhouette_samples(encodings,labels)


print("silhouette score: ")
print(h)

#print("silhouette_samples:")

#print(b)


colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    #plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
plt.title('Número de grupos estimado: %d' % n_clusters_)
plt.show()




