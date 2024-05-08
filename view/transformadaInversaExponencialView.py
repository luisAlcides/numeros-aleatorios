import os

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QToolBar, QMainWindow, QPushButton, QHBoxLayout, QMenu

import numpy as np

from utils.util import add_to_table, number_divide

script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')
ico_clean = os.path.join(script_directory, 'icons', 'clean.png')

class TransformadaInversaExponencial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Transformada Inversa Exponencial')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()

        self.label_random_number = QLabel('Cuantos numeros aleatorios desea generar?')
        self.input_random_number = QLineEdit()

        self.label_ri = QLabel('ri')
        self.input_ri = QLineEdit()

        self.label_lam = QLabel('Lambda:')
        self.input_lam = QLineEdit()

        self.btn_calc = QPushButton(QIcon(ico_solve), 'Calcular')
        self.btn_clean = QPushButton(QIcon(ico_clean), 'Limpiar')

        self.layout_buttons = QHBoxLayout()
        self.btn_calc.clicked.connect(self.transformadaInversaExponencial)
        self.btn_clean.clicked.connect(self.clean)

        self.layout_buttons.addWidget(self.btn_calc)
        self.layout_buttons.addWidget(self.btn_clean)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ri', 'Xi'])

        self.layout.addWidget(self.label_random_number)
        self.layout.addWidget(self.input_random_number)
        self.layout.addWidget(self.label_ri)
        self.layout.addWidget(self.input_ri)
        self.layout.addWidget(self.label_lam)
        self.layout.addWidget(self.input_lam)
        self.layout.addLayout(self.layout_buttons)
        self.layout.addWidget(self.table)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def transformadaInversaExponencial(self):
        try:
            random_number = int(self.input_random_number.text().strip())
            ri_input = self.input_ri.text().strip().split(',')
            ri_input = [r for r in ri_input if r]
            ri = [float(r) for r in ri_input] if ri_input else []
            lam = -1 * float(self.input_lam.text().strip())
            xi = []
            result = []

            for x in range(random_number):
                if x < len(ri):
                    if ri[x] is None:
                        ri.extend([np.random.rand()])
                    else:
                        a = 1 - ri[x]
                        res = lam * np.log(a)
                        xi.append(res)
                        result.append([ri[x], res])
                else:
                    ri.extend([np.random.rand()])
                    a = 1 - ri[x]
                    res = lam * np.log(a)
                    xi.append(res)
                    result.append([ri[x], res])

            add_to_table(self.table, result)

        except ValueError as e:
            print("Error al convertir a entero:", e)
        except Exception as e:
            print("Error:", e)

    def clean(self):
        self.input_random_number.clear()
        self.input_ri.clear()
        self.input_lam.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setHorizontalHeaderLabels(['ri', 'Xi'])
