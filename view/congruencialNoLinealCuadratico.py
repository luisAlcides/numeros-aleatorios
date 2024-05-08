import os
from PyQt6.QtGui import QIcon, QFont

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
    QMainWindow, QPushButton, QHBoxLayout

from utils.util import add_to_table

script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')
ico_clean = os.path.join(script_directory, 'icons', 'clean.png')

class CongruencialNoLinealCuadraticoView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Congruencial No Lineal Cuadratico')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()

        self.label_x0 = QLabel('x0')
        self.input_x0 = QLineEdit()

        self.label_a = QLabel('a')
        self.input_a = QLineEdit()

        self.label_b = QLabel('b')
        self.input_b = QLineEdit()

        self.label_c = QLabel('c')
        self.input_c = QLineEdit()

        self.label_m = QLabel('m')
        self.input_m = QLineEdit()

        self.label_number_random = QLabel('Cuantas variables aleatorias deseas:')
        self.input_number_random = QLineEdit()

        self.btn_calc = QPushButton(QIcon(ico_solve), 'Calcular')
        self.btn_clean = QPushButton(QIcon(ico_clean), 'Limpiar')

        self.layout_buttons = QHBoxLayout()

        self.btn_calc.clicked.connect(self.quadraticCongruentialMethod)
        self.btn_clean.clicked.connect(self.clean)

        self.layout_buttons.addWidget(self.btn_calc)
        self.layout_buttons.addWidget(self.btn_clean)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['x', 'r'])

        self.layout.addWidget(self.label_x0)
        self.layout.addWidget(self.input_x0)
        self.layout.addWidget(self.label_a)
        self.layout.addWidget(self.input_a)
        self.layout.addWidget(self.label_b)
        self.layout.addWidget(self.input_b)
        self.layout.addWidget(self.label_c)
        self.layout.addWidget(self.input_c)
        self.layout.addWidget(self.label_m)
        self.layout.addWidget(self.input_m)
        self.layout.addWidget(self.label_number_random)
        self.layout.addWidget(self.input_number_random)
        self.layout.addLayout(self.layout_buttons)
        self.layout.addWidget(self.table)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def quadraticCongruentialMethod(self):
        try:
            randomNums = []
            Xo = int(self.input_x0.text().strip())
            a = int(self.input_a.text().strip())
            b = int(self.input_b.text().strip())
            c = int(self.input_c.text().strip())
            m = int(self.input_m.text().strip())

            noOfRandomNums = int(self.input_number_random.text().strip())
            r = Xo / m
            randomNums.append([Xo, r])

            for i in range(1, noOfRandomNums):
                X = ((randomNums[i - 1][0] ** 2 * a) + (randomNums[i - 1][0] * b) + c) % m
                r = X / m
                randomNums.append([X,r])

            add_to_table(self.table, randomNums)
        except Exception as e:
            print(e)

    def clean(self):
        self.input_x0.setText('')
        self.input_m.setText('')
        self.input_b.setText('')
        self.input_a.setText('')
        self.input_c.setText('')
        self.input_number_random.setText('')
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setHorizontalHeaderLabels(['x', 'r'])
