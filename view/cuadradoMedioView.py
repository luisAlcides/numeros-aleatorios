import os

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QToolBar, QMainWindow, QPushButton, QHBoxLayout, QMenu

from utils.util import add_to_table, number_divide

script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')
ico_clean = os.path.join(script_directory, 'icons', 'clean.png')

class CuadradoMedioView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cuadrado Medio')
        self.setFont(QFont('Arial', 16))
        self.showMaximized()

        self.layout = QVBoxLayout()

        self.label_x0 = QLabel('X0')
        self.input_x0 = QLineEdit()

        self.label_number_random = QLabel('Numeros de variables aleatorias:')
        self.input_number_random = QLineEdit()
        self.input_number_random.setText('5')

        self.btn_calc = QPushButton(QIcon(ico_solve), 'Calcular')
        self.btn_clean = QPushButton(QIcon(ico_clean), 'Limpiar')

        self.layout_buttons = QHBoxLayout()

        self.btn_calc.clicked.connect(self.elevate)
        self.btn_clean.clicked.connect(self.clean)

        self.layout_buttons.addWidget(self.btn_calc)
        self.layout_buttons.addWidget(self.btn_clean)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['y', 'x', 'r'])

        self.layout.addWidget(self.label_x0)
        self.layout.addWidget(self.input_x0)
        self.layout.addWidget(self.label_number_random)
        self.layout.addWidget(self.input_number_random)
        self.layout.addLayout(self.layout_buttons)
        self.layout.addWidget(self.table)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def elevate(self):
        try:
            x0 = self.input_x0.text().strip()
            quantity_random = self.input_number_random.text().strip()

            x0 = int(x0)
            quantity_random = int(quantity_random)
            result = []
            result.append({'y': 0, 'x0': x0, 'r': x0 / 10000})
            for i in range(quantity_random):
                if i == 0:
                    y = int(x0) ** 2
                    x = int(number_divide(y))
                    r = int(x) / 10000
                    result.append([y, x, r])
                    x0 = x
                else:
                    y = int(x0) ** 2
                    x = int(number_divide(y))
                    r = int(x) / 10000
                    result.append([y, x, r])
                    x0 = x
            add_to_table(self.table, result)
        except Exception as e:
            print(e)

    def clean(self):
        self.input_x0.clear()
        self.input_number_random.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setHorizontalHeaderLabels(['y', 'x', 'r'])
