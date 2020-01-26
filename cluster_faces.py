# USAGE
# python cluster_faces.py --encodings encodings.pickle

# import the necessary packages
from sklearn.cluster import DBSCAN, KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, OPTICS,Birch
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



def cluster(endereco_enc,origem_fotos, destino_fotos):

    print("[INFO] loading encodings...")
 
 
    #carrega os encodings do disco
    data = pickle.loads(open(endereco_enc, "rb").read())
    
    #os coloca em um vetor numpy
    data = np.array(data)
    
    #extrai os encodings, colocando-os em uma lista
    encodings = [d["encoding"] for d in data]

    print("[INFO] clustering...")
    
    #inicio = time.time()

    #num correto de clusters = 8
    #clt = KMeans(n_clusters=6 , init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto')
    #print(clt)

    
    #X, Y = make_blobs()
    
    # retirou um parâmetro...
    #clt = MeanShift(bandwidth=0.5, seeds=None, bin_seeding=False, min_bin_freq=1, cluster_all=True, n_jobs=None).fit(X)

    
    #print("AAAAA")
    #print(labels)
    
    clt = DBSCAN(metric='euclidean')
    
    #Aqui que realmente acontece a clusterização

    
    l = clt.fit(encodings)
    laabels = l.labels_

    n =  metrics.silhouette_score(encodings, laabels)

    print(n)

    #fim = time.time()
    
    #print("O tempo de execução foi:" + str(fim - inicio))

    # determine the total number of unique faces found in the dataset
    labelIDs = np.unique(clt.labels_)
    

    #print(clt.labels_)# determine the total number of unique faces found in the dataset    
    numUniqueFaces = len(np.where(labelIDs > -1)[0])
    print("[INFO] # unique faces: {}".format(numUniqueFaces))


    
    # loop over the unique face integers
    for labelID in labelIDs:
        # find all indexes into the `data` array that belong to the
        # current label ID, then randomly sample a maximum of 25 indexes
        # from the set
        print("[INFO] faces for face ID: {}".format(labelID))
        
        



        idxs = np.where(clt.labels_ == labelID)[0]
       
        idxs = np.random.choice(idxs, size=min(25, len(idxs)),
            replace=False)

        # initialize the list of faces to include in the montage
        faces = []
        
        
        #endereco_pasta = os.path.join(data[i]["imagePath"], destino_fotos, str(labelIDS))
          
        endereco_pasta = os.path.join( destino_fotos, str(labelID))  
        
        Cria_Pastas(endereco_pasta)


        

        # loop over the sampled indexes
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
        title = "Face ID #{}".format(labelID)
        title = "Unknown Faces" if labelID == -1 else title
        cv2.imshow(title, montage)
        cv2.waitKey(0)
 
 
 #origem
 #destino
 
def Move_Fotos(origem, destino):
    
    print("realizando copia de fotos")
    shutil.copy(origem, destino)
    
def Cria_Pastas(endereco):

        if not os.path.exists(endereco):
            os.mkdir(endereco)
   



        

 