import os

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QToolBar, QMainWindow, QPushButton, QHBoxLayout, QMenu

from utils.util import message
from view.productoMedioView import ProductoMedioView
from view.cuadradoMedioView import CuadradoMedioView
from view.multiplicadorConstanteView import MultiplicadorConstanteView
from view.congruencialLinealView import CongruencialLinealView



script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')
ico_clean = os.path.join(script_directory, 'icons', 'clean.png')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Numeros Aleatorios')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()
        
        self.create_menu_bar()


        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        algoritmos_menu = menubar.addMenu('Algoritmos')
        
        producto_medio_action = QAction('Producto Medio', self)
        cuadrado_medio_action = QAction('Cuadrado Medio', self)
        multiplicador_constante_action = QAction('Multiplicador constante', self)
        congruencial_lineal_action = QAction('Congruencial lineal', self)
        
        producto_medio_action.triggered.connect(self.openProductoMedio)
        cuadrado_medio_action.triggered.connect(self.openCuadradoMedio)
        multiplicador_constante_action.triggered.connect(self.openMultiplicadorConstante)
        congruencial_lineal_action.triggered.connect(self.openCongruencialLineal)
        
        algoritmos_menu.addAction(producto_medio_action)
        algoritmos_menu.addAction(cuadrado_medio_action)
        algoritmos_menu.addAction(multiplicador_constante_action)
        algoritmos_menu.addAction(congruencial_lineal_action)
        
    
    def openProductoMedio(self):
        self.ui = ProductoMedioView()
        return self.ui
        
    
    def openCuadradoMedio(self):
        self.ui = CuadradoMedioView()
        return self.ui
        
    def openMultiplicadorConstante(self):
        self.ui = MultiplicadorConstanteView()
        return self.ui
    
    def openCongruencialLineal(self):
        self.ui = CongruencialLinealView()
        return self.ui
        
        
    
    



    

    