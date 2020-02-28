# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 08:49:34 2018

@author: Tiago Ibacache
"""

from TDA_Arboles import insertar, eliminar, crear_arbolbinario, buscarArbol
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget,QTableWidgetItem,QAbstractItemView, QComboBox
from PyQt5.uic import loadUi

def __init__(self):  
    super().__init__()
    loadUi("mainguia.ui", self)
    self.setWindowTitle("Guia Rey de copas")

   
class guiaArbol(): #Creamos el árbol con las caractéristicas 1, 2,3 
    def __init__(self):
        self.izq = None
        self.der = None
        self.dato = None
    
class telefono: #Creamos el objeto teléfono
    def __init__(self, ap=None, nom=None, tel=None):
        self.ap = ap
        self.nom= nom
        self.tel = tel
        
def cargar_tel (): #Lo cargamos con sus datos con
        Nombre = []
        Apellido = []
        Numero = []
        archtel = open("ListaDeTelefono.txt", "w")
        nume=telefono()    
        print("Ingrese el apellido de la persona")
        nume.ap= input()
        Apellido.append(nume.ap)
        archtel.write('Apellido=%s' %Apellido)
        print("Ingrese el nombre de la persona")
        nume.nom= input()
        Nombre.append(nume.nom)
        archtel.write('Nombre=%s' %Nombre)
        print("Ingrese el numero telefonico de la persona (nnn-nnnnnn)")
        nume.tel= input()
        Numero.append(nume.tel)
        archtel.write('Numero=%s' %Numero)
        archtel.close()
        return nume
        
class Principal1(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainguia.ui", self)
        self.setWindowTitle("Guia Rey de copas")
        #self.setupUi(self)
        self.BotonInsertar.clicked.connect(self.ent)
        self.BotonEliminar.clicked.connect(self.Eliminar)
        self.comboBox = QComboBox(self)
        self.comboBox.addItems([str(x) for x in range(3)])
        self.comboBox.activated.connect(self.Buscar)

    def ent(self):
        VentanaInsert = self.textEdit.toPlainText()
        with open(Principal1.Cargar()) as f:
            f.write(VentanaInsert)
        
    def Cargar ():
        atel = crear_arbolbinario()
        aape = crear_arbolbinario()
        anom = crear_arbolbinario()
        num = cargar_tel()
        aux = buscarArbol(atel,num.tel)
        if (aux is None):
            atel = insertar(atel, num.tel, 0)
            aape = insertar(aape, num.ap, 0)
            anom = insertar(anom, num.nom, 0)
            print('se inserto con exito el telefono')
        else: 
            print('ya existe')
    
    def Eliminar():
        atel = crear_arbolbinario()
        aape = crear_arbolbinario()
        anom = crear_arbolbinario()
        num = cargar_tel()
        aux=telefono()
        print("Ingrese el numero telefonico de la persona (nnn-nnnnnn) que desea eliminar")
        aux.telefono= input()
        x = buscarArbol(atel,num.tel)
        if (x != None):
            eliminar(atel,num.tel, 0)
            eliminar(aape, num.ap, 0)
            eliminar(anom, num.nom, 0)
            print('se elimino con exito el telefono')
        else:
            print('no existe el telefono')
        
    def Buscar(self):
        atel = crear_arbolbinario()
        aape = crear_arbolbinario()
        anom = crear_arbolbinario()
        num = cargar_tel()
        aux=telefono()
        print('1- Buscar por telefono')
        print('2- Buscar por Apellido y Nombre')
        opc=input()
        aux1 = None
        if(opc=='1'):
            print("Ingrese el numero telefonico de la persona (nnn-nnnnnn) que desea eliminar")
            aux.telefono= input()
            aux1 = buscarArbol(atel,num.tel)
            if(opc=='2'):
                print("Ingrese el apellido")
                aux.ap= input()
                aux1 = buscarArbol(aape,num.ap)
            if (aux1 is None):
                print('no existe')
            else: 
                print('Los datos de la persona buscada son: ')
                print('El apellido es: ',aape, num.ap)
                print('El nombre es: ',anom, num.nom)
                print('El telefono es: ',atel, num.tel)
        
                
def Menu():
        if (Principal1.BotonInsertar.clicked.connect()): #Primero busca si existe, si no lo encuentra; lo inserta en el arch
            Principal1.Cargar()  
             
        if (Principal1.BotonEliminar.clicked.connect()): #Busca si existe, si es así: lo elimina.
            Principal1.Eliminar()
                                      
        if (Principal1.BotonBuscar.clicked.connect()): #Lo busca y muestra sus datos
            Principal1.Buscar()           
            
if __name__ == "__main__":
    app = QApplication(sys.argv) #QtGui.
    main_window = Principal1()
    main_window.show()
    sys.exit(app.exec_())           
Menu()
