import os

from PyQt6.QtGui import QAction, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMainWindow

from view.esperanzaView import EsperanzaView
from view.productoMedioView import ProductoMedioView
from view.cuadradoMedioView import CuadradoMedioView
from view.multiplicadorConstanteView import MultiplicadorConstanteView
from view.congruencialLinealView import CongruencialLinealView
from view.transformadaInversaExponencialView import TransformadaInversaExponencial




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
        transformada_inversa_exponencial_action = QAction('Transformada Inversa Exponencial', self)
        esperanza_action = QAction('Esperanza y Varianza', self)

        producto_medio_action.triggered.connect(self.openProductoMedio)
        cuadrado_medio_action.triggered.connect(self.openCuadradoMedio)
        multiplicador_constante_action.triggered.connect(self.openMultiplicadorConstante)
        congruencial_lineal_action.triggered.connect(self.openCongruencialLineal)
        transformada_inversa_exponencial_action.triggered.connect(self.openTransformadaInversaExponencial)
        esperanza_action.triggered.connect(self.openEsperanza)

        algoritmos_menu.addAction(producto_medio_action)
        algoritmos_menu.addAction(cuadrado_medio_action)
        algoritmos_menu.addAction(multiplicador_constante_action)
        algoritmos_menu.addAction(congruencial_lineal_action)
        algoritmos_menu.addAction(transformada_inversa_exponencial_action)
        algoritmos_menu.addAction(esperanza_action)

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

    def openTransformadaInversaExponencial(self):
        self.ui = TransformadaInversaExponencial()
        return self.ui

    def openEsperanza(self):
        self.ui = EsperanzaView()
        return self.ui