# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
 

def encode(metodo,endereco_fotos, nome_enc, endereco_destino):
    
	#print("cheguei aqui")
	imagePaths = list(paths.list_images(endereco_fotos))
	print("AAAAA" + endereco_destino)
	#print(nome_enc)

	data = []
	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		print(imagePath)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
        
		#print(metodo)
		boxes = face_recognition.face_locations(rgb,
			model=metodo)    #model=args["detection_method"]

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# build a dictionary of the image path, bounding box location,
		# and facial encodings for the current image
        #este é o dicionario da imagem
		d = [{"imagePath": imagePath, "loc": box, "encoding": enc}
			for (box, enc) in zip(boxes, encodings)]
		data.extend(d)

	# dump the facial encodings data to disk
	print("[INFO] serializing encodings...")
    
	#aux =str(endereco ./ teste3))   
	endereco_final = Concatena(endereco_destino, nome_enc)   
	
	f = open(endereco_final, "wb")  #f = open(args["encodings"], "wb")
	pickle.dump(data,f)        
	#f.write(pickle.dumps(data))
   	#print( endereco_final)
	f.close()
	print("Encodings salvos em: " + endereco_final)	


def alo():
        print("cheguei no outro arquivo")
        
        
     #O segundo \ é para aceitar o primeiro \   
def Concatena(endereco,arquivo):
        return(str(endereco + "\\" + arquivo))
        




