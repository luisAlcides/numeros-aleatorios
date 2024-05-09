import os
import random
from re import S

import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QFont

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QToolBar, QMainWindow, QPushButton, QHBoxLayout, QMenu

from utils.util import add_to_table

script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')
ico_clean = os.path.join(script_directory, 'icons', 'clean.png')


class EsperanzaView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Esperanza y Varianza')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()

        self.label_info = QLabel('Ingrese los valores de x,y separados por coma')
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_x = QLabel('x')
        self.input_x = QLineEdit()

        self.label_y = QLabel('y')
        self.input_y = QLineEdit()

        self.btn_calc = QPushButton(QIcon(ico_solve), 'Calcular')
        self.btn_clean = QPushButton(QIcon(ico_clean), 'Limpiar')

        self.layout_buttons = QHBoxLayout()

        self.btn_calc.clicked.connect(self.calc_esperanza)
        self.btn_clean.clicked.connect(self.clean)

        self.layout_buttons.addWidget(self.btn_calc)
        self.layout_buttons.addWidget(self.btn_clean)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['x', 'y', 'P', 'E(x)', 'Var'])
        self.label_ex_sum = QLabel('')
        self.label_varianza_sum = QLabel('')
        self.label_desviacion = QLabel('')
        self.label_mean = QLabel('')

        self.layout.addWidget(self.label_info)
        self.layout.addWidget(self.label_x)
        self.layout.addWidget(self.input_x)
        self.layout.addWidget(self.label_y)
        self.layout.addWidget(self.input_y)
        self.layout.addLayout(self.layout_buttons)
        self.layout.addWidget(self.label_ex_sum)
        self.layout.addWidget(self.label_varianza_sum)
        self.layout.addWidget(self.label_desviacion)
        self.layout.addWidget(self.label_mean)
        self.layout.addWidget(self.table)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def esperanza(self, x, probabilidad):
        esp = []
        for g, p in zip(x, probabilidad):
            esp.append(g * p)
        return esp

    def varianza(self, xi, exsum, prob):
        res = []
        for x, p in zip(xi, prob):
            formula = ((x - exsum) ** 2) * p
            res.append(formula)
        return res

    def calc_esperanza(self):

        try:
            x_input = self.input_x.text().strip().split(',')
            x = list(map(float, x_input))

            y_input = self.input_y.text().strip().split(',')
            y = list(map(float, y_input))

            probabilidad = [yi / sum(y) for yi in y]
            ex = self.esperanza(x, probabilidad)

            ex_sum = sum(ex)
            varianza = self.varianza(x, ex_sum, probabilidad)
            varianza_sum = sum(varianza)
            desviacion_standar = np.sqrt(varianza_sum)
            mean = np.mean(x)

            data = []
            i = 0
            for xi, yi, p, e, var in zip(x, y, probabilidad, ex, varianza):
                data.append([xi, yi, p, e, var])
                i += 1
            self.label_ex_sum.setText(f'suma E(x) = {ex_sum}')
            self.label_varianza_sum.setText(f'suma Varianza = {varianza_sum}')
            self.label_desviacion.setText(f'Desviacion estandar = {desviacion_standar}')
            self.label_mean.setText(f'Media = {mean}')
            add_to_table(self.table, data)
            self.table.setHorizontalHeaderLabels(['x', 'y', 'P', 'E(x)', 'Var'])
        except Exception as e:
            print(e)

    def clean(self):
        self.input_x.setText('')
        self.input_y.setText('')
        self.label_ex_sum.setText('')
        self.label_varianza_sum.setText('')
        self.label_desviacion.setText('')
        self.label_mean.setText('')
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setHorizontalHeaderLabels(['x', 'y', 'P', 'E(x)', 'Var'])
