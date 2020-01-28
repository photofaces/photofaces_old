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


def cluster(endereco_enc,origem_fotos, destino_fotos):

    print("[INFO] loading encodings...")
 
 
    #carrega os encodings do disco
    data = pickle.loads(open(endereco_enc, "rb").read())
    
    #os coloca em um vetor numpy
    data = np.array(data)
    
    #print(data)
    
    
    #extrai os encodings, colocando-os em uma lista
    encodings = [d["encoding"] for d in data]
    
    
    #print(encodings)
    AAAA = len(encodings)
    #print(AAAA)

    
    
    #print(encodings)
    print("[INFO] clustering...")
    
    inicio = time.time()

    #num correto de clusters = 8
    #clt = KMeans(n_clusters=6 , init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto')
    #print(clt)

    
    #X, Y = make_blobs()
    
 
    #clt = DBSCAN(metric='euclidean')    
    
    
    
    # retirou um parâmetro...

    
    bandwidth = estimate_bandwidth(encodings)
    #print("nsamples:")
    #print(AAAA)
    
    print("bandwidth: ")
    print(bandwidth)
    
    
    clt = MeanShift(bandwidth = 0.49) #0.49
    
    clt.fit(encodings)
    
    
    fim = time.time()
    
    print("O tempo de execução da clusterização foi:" + str(fim - inicio))    
    
    
    labels = clt.labels_
    cluster_centers = clt.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    
    
    X=np.asarray(encodings)
    
    print(len(X))
    
    
    pca = sklearnPCA(n_components=2)
    X= pca.fit(encodings).transform(encodings)

    
    print(X)
    print(len(X))
    
    
    
    cluster_center = pca.fit(cluster_centers).transform(cluster_centers)
    
    b = metrics.silhouette_score(encodings,labels)
    print("silhouette:")
    print(b)
    


    # determine the total number of unique faces found in the dataset
    
    #labels = clt.labels_
    
    labels_unique =  np.unique(labels)
    
    #labelIDs = np.unique(clt.labels_)
    #labelIDs = clt.labels_
    

    #print(sample_silhouette_values)
    

        
    
    
    
    # aqui loop nos clusters
    for labelID in labels_unique:
        # find all indexes into the `data` array that belong to the
        # current label ID, then randomly sample a maximum of 25 indexes
        # from the set
        print("[INFO] faces for face ID: {}".format(labelID))
        

        idxs = np.where(clt.labels_ == labelID)[0]
       
        idxs = np.random.choice(idxs, size=min(25, len(idxs)),
            replace=False)

        # initialize the list of faces to include in the montage
        faces = []
        
        
        #endereco_pasta = os.path.join(data[i]["imagePath"], destino_fotos, str(labels_unique))
          
        endereco_pasta = os.path.join( destino_fotos, str(labelID))  
        
        Cria_Pastas(endereco_pasta)


        # aqui loop nas imagens
        for i in idxs:
        

            # load the input image and extract the face ROI
            image = cv2.imread(data[i]["imagePath"])
            
            #então, coloca as fotos lá dentro
            Move_Fotos(data[i]["imagePath"],endereco_pasta)


            (top, right, bottom, left) = data[i]["loc"]
            face = image[top:bottom, left:right]

            # force resize the face ROI to 96x96 and then add it to the
            # faces montage list
            face = cv2.resize(face, (96, 96))
            faces.append(face)
                    
                    
                    #testando os algoritmos acuracia


           # print("o número de clusters é: " + str(n_clusters_))           
            

        # create a montage using 96x96 "tiles" with 5 rows and 5 columns
        
        montage = build_montages(faces, (96, 96), (5, 5))[0]
        
        # show the output montage
        #title = "Face ID #{}".format(labelID)
        #title = "Unknown Faces" if labelID == -1 else title
        #cv2.imshow(title, montage)
        #cv2.waitKey(0)
 
 
 
 
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        #plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Número de grupos estimado: %d' % n_clusters_)
    plt.show()


    
     
     #origem
     #destino     
def Move_Fotos(origem, destino):
    
    print("realizando copia de fotos")
    shutil.copy(origem, destino)
    
def Cria_Pastas(endereco):

        if not os.path.exists(endereco):
            os.mkdir(endereco)
   
