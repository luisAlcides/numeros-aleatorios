import os
import random
from re import S
from PyQt6.QtGui import QAction, QIcon, QFont

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QToolBar, QMainWindow, QPushButton, QHBoxLayout, QMenu

from utils.util import add_to_table

script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')
ico_clean = os.path.join(script_directory, 'icons', 'clean.png')

class CongruencialLinealView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Multiplicador Constante')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()

        self.Label_x0 = QLabel('X0')
        self.input_x0 = QLineEdit()

        self.label_m = QLabel('m')
        self.input_m = QLineEdit()
        self.label_a = QLabel('a')
        self.input_a = QLineEdit()

        self.label_c = QLabel('c')
        self.input_c = QLineEdit()

        self.label_number_random = QLabel('Numeros de variables aleatorias:')
        self.input_number_random = QLineEdit()

        self.btn_calc = QPushButton(QIcon(ico_solve), 'Calcular')
        self.btn_clean = QPushButton(QIcon(ico_clean), 'Limpiar')

        self.layout_buttons = QHBoxLayout()

        self.btn_calc.clicked.connect(self.linearCongruentialMethod)
        self.btn_clean.clicked.connect(self.clean)

        self.layout_buttons.addWidget(self.btn_calc)
        self.layout_buttons.addWidget(self.btn_clean)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['X', 'm', 'a', 'c', 'r'])

        self.layout.addWidget(self.Label_x0)
        self.layout.addWidget(self.input_x0)
        self.layout.addWidget(self.label_m)
        self.layout.addWidget(self.input_m)
        self.layout.addWidget(self.label_a)
        self.layout.addWidget(self.input_a)
        self.layout.addWidget(self.label_c)
        self.layout.addWidget(self.input_c)
        self.layout.addWidget(self.label_number_random)
        self.layout.addWidget(self.input_number_random)
        self.layout.addLayout(self.layout_buttons)
        self.layout.addWidget(self.table)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def linearCongruentialMethod(self):
        try:
            randomNums = []
            Xo = int(self.input_x0.text().strip())
            m = int(self.input_m.text().strip())
            a = int(self.input_a.text().strip())
            c = int(self.input_c.text().strip())
            noOfRandomNums = int(self.input_number_random.text().strip())

            randomNums.append({'X0': Xo, 'm': m, 'a': a, 'c': c, 'r': Xo / m})

            for i in range(1, noOfRandomNums):
                X = ((randomNums[i - 1]['X0'] * a) + c) % m
                r = X / m
                randomNums.append([X, m, a, c, r])

            add_to_table(self.table, randomNums)
        except Exception as e:
            print(e)

    def clean(self):
        self.input_x0.setText('')
        self.input_m.setText('')
        self.input_a.setText('')
        self.input_c.setText('')
        self.input_number_random.setText('')
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setHorizontalHeaderLabels(['X', 'm', 'a', 'c', 'r'])
