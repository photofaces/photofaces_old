# USAGE
# python cluster_faces.py --encodings encodings.pickle

# import the necessary packages
from sklearn.cluster import DBSCAN, KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, OPTICS,Birch
from sklearn.metrics import accuracy_score
from imutils import build_montages
import numpy as np
import argparse
import pickle
import cv2
import time #medir tempo
import os
import shutil


# construct the argument parser and parse the arguments
def teste():
	print('testando')

#ap = argparse.ArgumentParser()
#ap.add_argument("-e", "--encodings", required=True,
#	help="path to serialized db of facial encodings")
#ap.add_argument("-j", "--jobs", type=int, default=-1,
#	help="# of parallel jobs to run (-1 will use all CPUs)")
#args = vars(ap.parse_args())

def cluster(endereco_enc,origem_fotos, destino_fotos):
    # load the serialized face encodings + bounding box locations from
    # disk, then extract the set of encodings to so we can cluster on
    # them
    #print("AAAA")    
    #print(destino_fotos)     
    print("[INFO] loading encodings...")
    #pickle.loads(open(args["encodings"], "rb").read())  
    data = pickle.loads(open(endereco_enc, "rb").read())
    data = np.array(data)
    #print("This is the data")    
    #print(data)       
    encodings = [d["encoding"] for d in data]
    #print(encodings)
    data = np.array(data)
    #print("This is the encoding")        
    # cluster the embeddings
    print("[INFO] clustering...")

    inicio = time.time()

    #num correto de clusters = 8
    clt = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto')
    #print(clt)


    #clt = AffinityPropagation(damping=0.5, max_iter=200, convergence_iter=15, copy=True, preference=None, affinity='euclidean', verbose=False)

    # retirou um parâmetro...
    #clt = MeanShift(bandwidth=0.5, seeds=None, bin_seeding=False, min_bin_freq=1, cluster_all=True, n_jobs=None)

    # retirou o parâmetro n_components = none
    #clt =SpectralClustering(n_clusters=8, eigen_solver=None, random_state=None, n_init=10, gamma=1.0, affinity='rbf', n_neighbors=10, eigen_tol=0.0, assign_labels='kmeans', degree=3, coef0=1, kernel_params=None, n_jobs=None)


    #clt = AgglomerativeClustering(n_clusters=10, affinity='euclidean', memory=None, connectivity=None, compute_full_tree='auto', linkage='ward', distance_threshold=None)

    #clt = DBSCAN(metric="euclidean", n_jobs= -1)

    #print(type(clt))

    #retirou parâmetro max_eps=inf, min_samples = 2 foi um bom resultado

    #clt = OPTICS(min_samples=2, max_eps = 99999999999, metric='minkowski', p=2, metric_params=None, cluster_method='xi', eps=None, xi=0.05, predecessor_correction=True, min_cluster_size=None, algorithm='auto', leaf_size=30, n_jobs=None)

    # ??
    #clt = Birch(threshold=0.2, branching_factor=50, n_clusters=3, compute_labels=True, copy=True)
    
    #Aqui que realmente acontece a clusterização
    clt.fit(encodings)

    fim = time.time()

    #depois de arrumar as funcionalidades, VOLTAR
    #print("O tempo de execução foi:" + str(fim - inicio))


    # y_true é um array com os verdadeiros, y_pred, é o resultado
    #accuracy = accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)


    # determine the total number of unique faces found in the dataset
    labelIDs = np.unique(clt.labels_)
    #print(labelIDs)    
    #print(clt.labels_)# determine the total number of unique faces found in the dataset    
    numUniqueFaces = len(np.where(labelIDs > -1)[0])
    print("[INFO] # unique faces: {}".format(numUniqueFaces))

    
    #print( "esta é a lista GGGGGGGGGGGGGGGGGGGGGGGGG:" )
    #endereco_fotos_dataset = Identifica_fotos(origem_fotos, destino_fotos)     
    
    #print(endereco_fotos_dataset)
    
    #print(g)
    #print(type(g))
    # loop over the unique face integers
    for labelID in labelIDs:
        # find all indexes into the `data` array that belong to the
        # current label ID, then randomly sample a maximum of 25 indexes
        # from the set
        print("[INFO] faces for face ID: {}".format(labelID))
        #print("AAA" +str(labelID))
        idxs = np.where(clt.labels_ == labelID)[0]
        #print("clt label:"+ str(clt.labels_))
        #print("idx: " +str(idxs))        
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

            # ALASSSS I FOUND YA MUAHAHAHAHAHAHAHAHA
            #print(data[i]["imagePath"])            
            
           
           
            #então, coloca as fotos lá dentro
            Move_Fotos(data[i]["imagePath"],endereco_pasta)


            (top, right, bottom, left) = data[i]["loc"]
            face = image[top:bottom, left:right]

            # force resize the face ROI to 96x96 and then add it to the
            # faces montage list
            face = cv2.resize(face, (96, 96))
            faces.append(face)

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
   
    
        
        

 