import os
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, \
    QTableWidgetItem, QComboBox, QToolBar, QMainWindow

from utils import message

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

        self.label_x0 = QLabel('X0:')
        self.input_x0 = QLineEdit()
        self.layout.addWidget(self.label_x0)
        self.layout.addWidget(self.input_x0)

        self.label_x1 = QLabel('X1:')
        self.input_x1 = QLineEdit()
        self.layout.addWidget(self.label_x1)
        self.layout.addWidget(self.input_x1)

        self.label_funcion = QLabel('Función:')
        self.input_funcion = QComboBox()
        self.input_funcion.addItem('x0 * x1')
        self.input_funcion.addItem('x0 **2')
        self.layout.addWidget(self.label_funcion)
        self.layout.addWidget(self.input_funcion)

        self.label_number_random = QLabel('Numeros de variables aleatorias:')
        self.input_number_random = QLineEdit()
        self.input_number_random.setText('5')
        self.layout.addWidget(self.label_number_random)
        self.layout.addWidget(self.input_number_random)


        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(40, 40))
        self.addToolBar(self.toolbar)

        self.solver_action = QAction(QIcon(ico_solve), 'Resolver', self)
        self.solver_action.triggered.connect(self.solver)
        self.toolbar.addAction(self.solver_action)

        self.clean_action = QAction(QIcon(ico_clean), 'Limpiar celdas', self)
        self.clean_action.triggered.connect(self.clear_inputs)
        self.toolbar.addAction(self.clean_action)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def solver(self):
        try:
            x0 = int(self.input_x0.text().strip())

            if self.input_x1.text().strip() == '':
                self.input_x1.setText('0')
            else:
                x1 = int(self.input_x1.text().strip())

            fun = self.input_funcion.currentText()
            quantity_random = int(self.input_number_random.text().strip())

            if fun is None:
                message('Función no válida')
            elif fun == 'x0 * x1':
                self.multiply(x0, x1, quantity_random)
            elif fun == 'x0 **2':
                self.elevate(x0, quantity_random)
        except Exception as e:
            message('No has llenado ningun campo')

    def add_to_table(self, data):
        self.table.setRowCount(0)

        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0

        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)

        for i, row_data in enumerate(data):
            for j, (key, value) in enumerate(row_data.items()):
                item_text = f'{key}: {value}'
                item = QTableWidgetItem(item_text)
                self.table.setItem(i, j, item)


    def number_divide(self, number):
        number = [int(i) for i in str(number)]
        half = len(number) // 2
        half_number = number[half - 2: half + 2]
        number_str = ''.join(map(str, half_number))
        return number_str

    def multiply(self, x0, x1, quantity_random):
        result = []
        result.append({'x0': x0, 'x1': x1, 'r': x0 / 10000})
        for i in range(quantity_random):
            if i == 0:
                y = x0 * x1
                x = self.number_divide(y)
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 2}': x, f'r{i}': r})
                x0 = x1
                x1 = x
            else:
                y = int(x0) * int(x1)
                x = self.number_divide(y)
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 2}': x, f'r{i}': r})
                x0 = int(x1)
                x1 = int(x)
        self.add_to_table(result)

    def elevate(self, x0, quantity_random):
        result = []
        result.append({'y': 0, 'x0': x0, 'r': x0 / 10000})
        for i in range(quantity_random):
            if i == 0:
                y = int(x0) ** 2
                x = self.number_divide(y)
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 1}': x, f'r{i}': r})
                x0 = x
            else:
                y = int(x0) ** 2
                x = self.number_divide(y)
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 1}': x, f'r{i}': r})
                x0 = x
        self.add_to_table(result)

    def clear_inputs(self):
        self.input_x1.clear()
        self.input_x0.clear()
        self.input_funcion.setCurrentIndex(-1)
        self.input_number_random.clear()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
