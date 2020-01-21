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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clusterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clusterBtn.setGeometry(QtCore.QRect(120, 290, 75, 23))
        self.clusterBtn.setObjectName("clusterBtn")
        self.datasetLbl = QtWidgets.QLabel(self.centralwidget)
        self.datasetLbl.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.datasetLbl.setObjectName("datasetLbl")
        self.metodoLbl = QtWidgets.QLabel(self.centralwidget)
        self.metodoLbl.setGeometry(QtCore.QRect(0, 230, 131, 20))
        self.metodoLbl.setObjectName("metodoLbl")
        self.datasetBtn = QtWidgets.QToolButton(self.centralwidget)
        self.datasetBtn.setGeometry(QtCore.QRect(10, 30, 25, 19))
        self.datasetBtn.setObjectName("datasetBtn")
        self.comboMethods = QtWidgets.QComboBox(self.centralwidget)
        self.comboMethods.setGeometry(QtCore.QRect(0, 250, 181, 22))
        self.comboMethods.setObjectName("comboMethods")
        self.comboMethods.addItem("")
        self.comboMethods.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 250, 41, 21))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lblEnderecoDataset = QtWidgets.QLabel(self.centralwidget)
        self.lblEnderecoDataset.setGeometry(QtCore.QRect(50, 30, 471, 21))
        self.lblEnderecoDataset.setObjectName("lblEnderecoDataset")
        self.encodingBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encodingBtn.setGeometry(QtCore.QRect(100, 160, 91, 23))
        self.encodingBtn.setObjectName("encodingBtn")
        self.encodingResultlbl = QtWidgets.QLabel(self.centralwidget)
        self.encodingResultlbl.setGeometry(QtCore.QRect(50, 140, 491, 16))
        self.encodingResultlbl.setObjectName("encodingResultlbl")
        self.lblResultAgrupar = QtWidgets.QLabel(self.centralwidget)
        self.lblResultAgrupar.setGeometry(QtCore.QRect(210, 290, 47, 13))
        self.lblResultAgrupar.setObjectName("lblResultAgrupar")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(-100, 470, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.nomeEncLe = QtWidgets.QLineEdit(self.centralwidget)
        self.nomeEncLe.setGeometry(QtCore.QRect(10, 90, 161, 20))
        self.nomeEncLe.setObjectName("nomeEncLe")
        self.lblresultNomeEnc = QtWidgets.QLabel(self.centralwidget)
        self.lblresultNomeEnc.setGeometry(QtCore.QRect(180, 90, 111, 16))
        self.lblresultNomeEnc.setObjectName("lblresultNomeEnc")
        self.nomeEnclbl = QtWidgets.QLabel(self.centralwidget)
        self.nomeEnclbl.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.nomeEnclbl.setObjectName("nomeEnclbl")
        self.encodingEnderecoBtn = QtWidgets.QToolButton(self.centralwidget)
        self.encodingEnderecoBtn.setGeometry(QtCore.QRect(10, 210, 25, 19))
        self.encodingEnderecoBtn.setObjectName("encodingEnderecoBtn")
        self.encodingEnderecoLbl = QtWidgets.QLabel(self.centralwidget)
        self.encodingEnderecoLbl.setGeometry(QtCore.QRect(0, 190, 47, 13))
        self.encodingEnderecoLbl.setObjectName("encodingEnderecoLbl")
        self.lblEncodingSelecionado = QtWidgets.QLabel(self.centralwidget)
        self.lblEncodingSelecionado.setGeometry(QtCore.QRect(40, 210, 811, 16))
        self.lblEncodingSelecionado.setObjectName("lblEncodingSelecionado")
        self.encodingsDestinoBtn = QtWidgets.QToolButton(self.centralwidget)
        self.encodingsDestinoBtn.setGeometry(QtCore.QRect(10, 140, 25, 19))
        self.encodingsDestinoBtn.setObjectName("encodingsDestinoBtn")
        self.encodingsDestinoLbl = QtWidgets.QLabel(self.centralwidget)
        self.encodingsDestinoLbl.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.encodingsDestinoLbl.setObjectName("encodingsDestinoLbl")
        self.testebtn = QtWidgets.QPushButton(self.centralwidget)
        self.testebtn.setGeometry(QtCore.QRect(340, 290, 75, 23))
        self.testebtn.setObjectName("testebtn")
        self.testelbl = QtWidgets.QLabel(self.centralwidget)
        self.testelbl.setGeometry(QtCore.QRect(430, 290, 47, 13))
        self.testelbl.setObjectName("testelbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        #Quando aperta "..."
        self.datasetBtn.clicked.connect(self.enderecoDataset)

        #Quando aperta "criar encoding"
        self.encodingBtn.clicked.connect(self.CriaEmbedding)
        
        #Quando aperta "Agrupar"
        self.clusterBtn.clicked.connect(self.CriaCluster)
        
        #Quando aperta no segundo "..."
        self.encodingsDestinoBtn.clicked.connect(self.enderecoDestinoEnc)
        
        #Quando aperta o terceiro "..."
        self.encodingEnderecoBtn.clicked.connect(self.enderecoEnc)
        
        #Quando aperta o "teste"
        self.testebtn.clicked.connect(self.teste1)        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clusterBtn.setText(_translate("MainWindow", "Agrupar"))
        self.datasetLbl.setText(_translate("MainWindow", "Dataset"))
        self.metodoLbl.setText(_translate("MainWindow", "Método de Agrupamento"))
        self.datasetBtn.setText(_translate("MainWindow", "..."))
        self.comboMethods.setItemText(0, _translate("MainWindow", "Não-Supervisionado (DBSCAN)"))
        self.comboMethods.setItemText(1, _translate("MainWindow", "Supervisionado (K-Means)"))
        self.label.setText(_translate("MainWindow", "!!!"))
        self.lblEnderecoDataset.setText(_translate("MainWindow", "Docs/FotosVerão2020"))
        self.encodingBtn.setText(_translate("MainWindow", "Criar encoding"))
        self.encodingResultlbl.setText(_translate("MainWindow", "????"))
        self.lblResultAgrupar.setText(_translate("MainWindow", "¿¿¿¿¿¿¿¿"))
        self.nomeEncLe.setText(_translate("MainWindow", "digite aqui..."))
        self.lblresultNomeEnc.setText(_translate("MainWindow", "Ex: Enc_fotos_verao"))
        self.nomeEnclbl.setText(_translate("MainWindow", "Nome do arquivo"))
        self.encodingEnderecoBtn.setText(_translate("MainWindow", "..."))
        self.encodingEnderecoLbl.setText(_translate("MainWindow", "Encoding"))
        self.lblEncodingSelecionado.setText(_translate("MainWindow", "Docs/Encodings/Enc_verao"))
        self.encodingsDestinoBtn.setText(_translate("MainWindow", "..."))
        self.encodingsDestinoLbl.setText(_translate("MainWindow", "Pasta Destino"))
        self.testebtn.setText(_translate("MainWindow", "Teste"))
        self.testelbl.setText(_translate("MainWindow", "¿¿¿¿¿¿¿¿"))

    def teste1(self):
        #aux = self.datasetLbl.text
        #print("z")
        
        
        #pega o texto da line edit ( onde o usuario digita o nome do encoding)
        texto_lineEdit = self.nomeEncLe.text()
        
        #faz ele aparecer em um label especifico
        self.testelbl.setText(texto_lineEdit)
    
        #print(str(aux))
        

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
        
        print(h)        
        print(type(h))   
        cls.cluster(h)

    	

		


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
