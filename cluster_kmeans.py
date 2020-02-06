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



def cluster(endereco_enc,origem_fotos, destino_fotos, num_clusters):

    print("[INFO] loading encodings...")
 
 
    #carrega os encodings do disco
    data = pickle.loads(open(endereco_enc, "rb").read())
    
    #os coloca em um vetor numpy
    data = np.array(data)

    #extrai os encodings, colocando-os em uma lista
    encodings = [d["encoding"] for d in data]
    
    
    #print(encodings)
    tam_encodings = len(encodings)
    
    #print(encodings)
    print("[INFO] Agrupando...")
    
    #função para medir tempo de execução
    inicio = time.time()

    #função para estimar o bandwidth
    bandwidth = estimate_bandwidth(encodings)
    
    #Numero de clusters é determinado pelo usuário
    clt = KMeans(n_clusters=num_clusters , init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto')
    
    #realiza o agrupamento
    clt.fit(encodings)
    
    #fim da função de tempo de execução
    fim = time.time()
    print("O tempo de execução da clusterização foi:" + str(fim - inicio))    
    
    #gera as etiquetas dos clusters
    labels = clt.labels_
    
    #identifica os centroides
    cluster_centers = clt.cluster_centers_

    #identifica os indivíduos únicos
    labels_unique = np.unique(labels)
    
    #quantidade de clusters
    n_clusters_ = len(labels_unique)
    
    #conversão para vetor(para mostrar graficamente)
    X=np.asarray(encodings)
    
    
    #auxiliar para mostrar graficamente (quando amostra)
    pca = sklearnPCA(n_components=2)
    X= pca.fit(encodings).transform(encodings)

    #auxiliar para mostrar graficamente (quando clusters)
    cluster_center = pca.fit(cluster_centers).transform(cluster_centers)
    
    #calcula o silhouette_score dos clusters feitos
    b = metrics.silhouette_score(encodings,labels)
    
    print("silhouette:")
    print(b)
    
    #identifica os labels únicos
    labels_unique =  np.unique(labels)
    
    #loop nos clusters
    for labelID in labels_unique:
        # Encontra todos os índices no vetor "data" que pertença ao ID atual

        idxs = np.where(clt.labels_ == labelID)[0]
       
        idxs = np.random.choice(idxs, size=min(25, len(idxs)),
            replace=False)

        # inicializa a lista de faces para incluir na montagem
        faces = []
        
        
        #função auxiliar para gerar endereço dos grupos
        endereco_pasta = os.path.join( destino_fotos, str(labelID))  
        
        #função para criar diretório com os grupos
        Cria_Pastas(endereco_pasta)


        # aqui loop nas imagens
        for i in idxs:
        

            # lê as imagens
            image = cv2.imread(data[i]["imagePath"])
            
            #função auxiliar: move as imagens que foram identificadas em cada cluster para seus respectivos diretórios
            Move_Fotos(data[i]["imagePath"],endereco_pasta)


            (top, right, bottom, left) = data[i]["loc"]
            face = image[top:bottom, left:right]

            # auxiliar para montagem de grupos 96x96 pixels
            face = cv2.resize(face, (96, 96))
            faces.append(face)
            
        # cria a montagem 
        montage = build_montages(faces, (96, 96), (5, 5))[0]
        
        
        # show the output montage
        #title = "Face ID #{}".format(labelID)
        #title = "Unknown Faces" if labelID == -1 else title
        #cv2.imshow(title, montage)
        #cv2.waitKey(0)
 
    #função que mostra os clusters (amostra, ou grupos completos)
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        
        #amostra
        #plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        
        #grupos completos
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Número de grupos estimado: %d' % n_clusters_)
    plt.show()


   
def Move_Fotos(origem, destino):
    
    #print("realizando copia de fotos")
    shutil.copy(origem, destino)
    
def Cria_Pastas(endereco):

        if not os.path.exists(endereco):
            os.mkdir(endereco)