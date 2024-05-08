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
        self.setWindowTitle('Congruencial lineal')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()

        self.Label_x0 = QLabel('X0')
        self.input_x0 = QLineEdit()

        self.label_k = QLabel('k')
        self.input_k = QLineEdit()
        self.label_g = QLabel('g')
        self.input_g = QLineEdit()

        self.label_c = QLabel('c')
        self.input_c = QLineEdit()

        self.label_a = QLabel('')
        self.label_m = QLabel('')

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
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['X', 'r'])

        self.layout.addWidget(self.Label_x0)
        self.layout.addWidget(self.input_x0)
        self.layout.addWidget(self.label_k)
        self.layout.addWidget(self.input_k)
        self.layout.addWidget(self.label_g)
        self.layout.addWidget(self.input_g)
        self.layout.addWidget(self.label_c)
        self.layout.addWidget(self.input_c)
        self.layout.addWidget(self.label_number_random)
        self.layout.addWidget(self.input_number_random)
        self.layout.addLayout(self.layout_buttons)
        self.layout.addWidget(self.label_a)
        self.layout.addWidget(self.label_m)
        self.layout.addWidget(self.table)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def linearCongruentialMethod(self):
        try:
            randomNums = []
            Xo = int(self.input_x0.text().strip())
            k = int(self.input_k.text().strip())
            g = int(self.input_g.text().strip())
            c = int(self.input_c.text().strip())
            noOfRandomNums = int(self.input_number_random.text().strip())

            m = 2 ** g
            a = 1 + 4 * k

            for i in range(noOfRandomNums):
                X = ((a * Xo) + c) % m
                print(f'x = (({a} * {Xo}) + {c}) % {m} = {X}')
                r = X / (m - 1)
                print(f'r = {X} / ({m} - 1) = {r}')
                randomNums.append([X, r])
                Xo = X

            self.label_a.setText(f'a = {a}')
            self.label_m.setText(f'm = {m}')

            add_to_table(self.table, randomNums)
        except Exception as e:
            print(e)

    def clean(self):
        self.input_x0.setText('')
        self.input_k.setText('')
        self.input_g.setText('')
        self.input_c.setText('')
        self.label_a.setText('')
        self.label_m.setText('')
        self.input_number_random.setText('')
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setHorizontalHeaderLabels(['X', 'r'])
