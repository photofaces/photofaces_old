# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\r2d3\Desktop\Interface TCc_TESTANDOCOMBOBOX\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
import encode_faces as enc
import cluster_faces as cls
import os
from datetime import datetime
import pathlib


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clusterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clusterBtn.setGeometry(QtCore.QRect(690, 20, 75, 23))
        self.clusterBtn.setObjectName("clusterBtn")
        self.datasetLbl = QtWidgets.QLabel(self.centralwidget)
        self.datasetLbl.setGeometry(QtCore.QRect(40, 0, 201, 16))
        self.datasetLbl.setObjectName("datasetLbl")
        self.metodoLbl = QtWidgets.QLabel(self.centralwidget)
        self.metodoLbl.setGeometry(QtCore.QRect(500, 0, 131, 20))
        self.metodoLbl.setObjectName("metodoLbl")
        self.datasetBtn = QtWidgets.QToolButton(self.centralwidget)
        self.datasetBtn.setGeometry(QtCore.QRect(10, 20, 25, 19))
        self.datasetBtn.setObjectName("datasetBtn")
        self.comboMethods = QtWidgets.QComboBox(self.centralwidget)
        self.comboMethods.setGeometry(QtCore.QRect(500, 20, 181, 22))
        self.comboMethods.setObjectName("comboMethods")
        self.comboMethods.addItem("")
        self.comboMethods.addItem("")
        self.lblEnderecoDataset = QtWidgets.QLabel(self.centralwidget)
        self.lblEnderecoDataset.setGeometry(QtCore.QRect(40, 20, 381, 16))
        self.lblEnderecoDataset.setObjectName("lblEnderecodataset")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(-100, 470, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        #Quando aperta "..."
        self.datasetBtn.clicked.connect(self.enderecoDataset)
        
        #Quando aperta no segundo "..."
        #self.encodingsDestinoBtn.clicked.connect(self.enderecoDestinoEnc)        

        #Quando aperta "criar encoding"
        #self.encodingBtn.clicked.connect(self.CriaEmbedding)
        
        #Quando aperta o terceiro "..."
        #self.encodingEnderecoBtn.clicked.connect(self.enderecoEnc)        
        
        #Quando aperta o quarto "..."
        #self.destinoFotosBtn.clicked.connect(self.enderecoDestinoFotos)
        
        #Quando aperta "Agrupar"
        self.clusterBtn.clicked.connect(self.teste1)   

        #Quando aperta o "teste"
        #self.testebtn.clicked.connect(self.teste1)        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clusterBtn.setText(_translate("MainWindow", "Agrupar"))
        self.datasetLbl.setText(_translate("MainWindow", "Biblioteca de Fotos"))
        self.metodoLbl.setText(_translate("MainWindow", "Método de Agrupamento"))
        self.datasetBtn.setText(_translate("MainWindow", "..."))
        self.comboMethods.setItemText(0, _translate("MainWindow", "Não-Supervisionado (DBSCAN)"))
        self.comboMethods.setItemText(1, _translate("MainWindow", "Supervisionado (K-Means)"))
        self.lblEnderecoDataset.setText(_translate("MainWindow", "????"))
        
    def teste1(self):
        #pega o texto da line edit ( onde o usuario digita o nome do encoding)
        #texto_lineEdit = self.nomeEncLe.text()
        
        #faz ele aparecer em um label especifico
        #self.testelbl.setText(texto_lineEdit)
        
        
        #pega o endereco do label
        endereco_dataset  = self.lblEnderecoDataset.text()
        
        #endereco de onde criar a pasta com seu nome
        pasta_config = os.path.join(endereco_dataset, str("config"))
        
        #o nome do encoding vai ser o do dia-minuto....
        nome_enc = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_")    
  
        #se ja nao existe um config
        if not os.path.exists(pasta_config):
            
            #cria um
            os.mkdir(pasta_config)          
           
        enc.encode('hog',endereco_dataset, nome_enc, pasta_config)
        
        #salva o numero do ultimo encoding, para usar no agrupamento
        ultimo_encoding = pasta_config + "\\" +nome_enc    
        print(ultimo_encoding)
        
        ## ---~~~---~~~~----~~~~
        print("**********************************************************************")
        #cria a pasta Resultado_Encoding na mesma do dataset
        
        print("#########################")
        
        #pegando o endereco antes do dataset para colocar a pasta de resultados
        endereco_antes_dataset  =  pathlib.Path().absolute()
        
        #print(endereco_antes_dataset)        

        pasta_resultados = os.path.join(endereco_antes_dataset, str("resultados"))
        
        if not os.path.exists(pasta_resultados):
            os.mkdir(pasta_resultados)       

       
        nome_resultado_encoding = "Resultado_ " + nome_enc
        pasta_resultado_atual = os.path.join(pasta_resultados, nome_resultado_encoding)
        print(pasta_resultado_atual)
        
        if not os.path.exists(pasta_resultado_atual):
            os.mkdir(pasta_resultado_atual)
            
        cls.cluster(ultimo_encoding, endereco_dataset, pasta_resultado_atual)      
            
            
            
        #resultado_ultimo_encoding = str("Resultado:" + ultimo_encoding)
        #print(resultado_ultimo_encoding)
        
        #endereco_resultado_ultimo_encoding = os.path.join(pasta_resultado, str(resultado_ultimo_encoding))
        #print(endereco_resultado_ultimo_encoding)
        
        #if not os.path.exists(endereco_resultado_ultimo_encoding):
         #   os.mkdir(endereco_resultado_ultimo_encoding)
        
        

            
            #os.path past_config/config" +"/" "nome do encoding"
        
        

    def Apertacombo(self):
    	x = self.comboMethods.currentText()

    	self.label.setText("Tst"+ " " + str(x))

    def enderecoDataset(self):
    	#função para pegar o endereço do direcotry
    	path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
    	caminho = str(path)
    	#print(caminho)
    	self.lblEnderecoDataset.setText(caminho)

    def enderecoDestinoEnc(self):
    	#função para pegar o endereço do direcotry
    	path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
    	caminho = str(path)
    	#print(caminho)
    	self.encodingResultlbl.setText(caminho)        
    
    def enderecoEnc(self):
    	#função para pegar o endereço do ARQUIVO **getOpenFileName, porém ela o retorna em uma tupla, é preciso tratar a string
    	caminho = str(QtWidgets.QFileDialog.getOpenFileName(None, "Select Directory"))   
    	#print(type(caminho))           
       	#print(type(caminho)) hrs, mins, secs = tim.split(':')
    	a = caminho          
    	#b=a.split()       
    	x, y = a.split(',')        
    	#print(x)
    	#z é o endereço já tratado, [2:-1] é para tirar (' e  ' respectivamente.       
    	z = x[2:-1]
    	#print(z)
    	#print()         
    	#caminho = QtWidgets.QFileDialog.getOpenFileName(None);        
    	#caminho = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
    	self.lblEncodingSelecionado.setText(z)   

    def enderecoDestinoFotos(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        caminho = str(path)
        self.pastaDestinoLbl.setText(caminho)

    def getCaminhoDataset(self):
    	#retorna o texto do label, uma vez que ficou gravado lá o resultado da função em enderecoDataset
    	x = self.lblEnderecoDataset.text()
    	return x


    def CriaEmbedding(self):
    
        #texto da line edit
        a = self.nomeEncLe.text()
        
        #endereço do dataset
        x = self.lblEnderecoDataset.text()
        
        #endereço pasta destino
        y= self.encodingResultlbl.text()
        
        #print(x)
        enc.encode('hog',x,a,y)
    	#enc.alo()

    def CriaCluster(self):
    
        #texto referente a oendereco do encoding
        h = self.lblEncodingSelecionado.text()
        
        #pasta origem
        o = self.lblEnderecoDataset.text()        
        #pasta destino
        i = self.pastaDestinoLbl.text()
        
        #print(h)        
        #print(type(h))   
        cls.cluster(h,o,i)

    	

		


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
