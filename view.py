import os

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget, \
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

        self.label_funcion = QLabel('Algoritmo:')
        self.input_funcion = QComboBox()
        self.input_funcion.addItem('Producto Medio')
        self.input_funcion.addItem('Cuadrado Medio')
        self.input_funcion.addItem('Multiplicador constante')
        self.input_funcion.currentTextChanged.connect(self.check_function)
        self.layout.addWidget(self.label_funcion)
        self.layout.addWidget(self.input_funcion)

        self.label_x0 = QLabel('X0:')
        self.input_x0 = QLineEdit()
        self.layout.addWidget(self.label_x0)
        self.layout.addWidget(self.input_x0)

        self.label_x1 = QLabel('X1:')
        self.input_x1 = QLineEdit()
        self.layout.addWidget(self.label_x1)
        self.layout.addWidget(self.input_x1)

        self.label_constant = QLabel('A')
        self.input_constant = QLineEdit()
        self.input_constant.setEnabled(False)
        self.layout.addWidget(self.label_constant)
        self.layout.addWidget(self.input_constant)

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

    def check_function(self):
        current_text = self.input_funcion.currentText()
        if current_text == 'Producto Medio':
            self.input_x1.setEnabled(True)
            self.input_constant.setEnabled(False)
        elif current_text == 'Cuadrado Medio':
            self.input_x1.setEnabled(False)
            self.input_constant.setEnabled(False)
        elif current_text == 'Multiplicador constante':
            self.input_constant.setEnabled(True)
            self.input_x1.setEnabled(False)

    def solver(self):
        try:
            fun = self.input_funcion.currentText()
            quantity_random = int(self.input_number_random.text().strip())

            if fun is None:
                message('Función no válida')
            elif fun == 'Producto Medio':
                x0 = self.input_x0.text().strip()
                x1 = self.input_x1.text().strip()
                self.multiply(x0, x1, quantity_random)
            elif fun == 'Cuadrado Medio':
                x0 = self.input_x0.text().strip()
                self.elevate(x0, quantity_random)
            elif fun == 'Multiplicador constante':
                x0 = self.input_x0.text().strip()
                A = self.input_constant.text().strip()
                self.multiply_constant(x0, A, quantity_random)

        except Exception as e:
            print(e)

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
        size = 8
        number = str(number)
        if len(number) < size:
            number = number.zfill(8)
        number = [int(i) for i in str(number)]
        half = len(number) // 2
        half_number = number[half - 2: half + 2]
        number_str = ''.join(map(str, half_number))

        return number_str

    def multiply(self, x0, x1, quantity_random):
        x0 = int(x0)
        x1 = int(x1)
        result = []
        result.append({'x0': x0, 'x1': x1, 'r': x0 / 10000})
        for i in range(quantity_random):
            if i == 0:
                y = x0 * x1
                x = int(self.number_divide(y))
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 2}': x, f'r{i}': r})
                x0 = x1
                x1 = x
            else:
                y = int(x0) * int(x1)
                x = int(self.number_divide(y))
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 2}': x, f'r{i}': r})
                x0 = int(x1)
                x1 = int(x)
        self.add_to_table(result)

    def elevate(self, x0, quantity_random):
        x0 = int(x0)
        result = []
        result.append({'y': 0, 'x0': x0, 'r': x0 / 10000})
        for i in range(quantity_random):
            if i == 0:
                y = int(x0) ** 2
                x = int(self.number_divide(y))
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 1}': x, f'r{i}': r})
                x0 = x
            else:
                y = int(x0) ** 2
                x = int(self.number_divide(y))
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 1}': x, f'r{i}': r})
                x0 = x
        self.add_to_table(result)

    def multiply_constant(self, x0, A, quantity_random):
        x0 = int(x0)
        A = int(A)
        result = []
        result.append({'x0': x0, 'A': A, 'r': x0 / 10000})
        for i in range(quantity_random):
            if i == 0:
                y = x0 * A
                x = int(self.number_divide(y))
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i + 1}': x, f'r{i}': r})
                x0 = x
            else:
                y = x0 * A
                x = int(self.number_divide(y))
                r = int(x) / 10000
                result.append({f'y{i}': y, f'x{i+1}': x, f'r{i}': r})
                x0 = x
        self.add_to_table(result)

    def clear_inputs(self):
        self.input_x1.clear()
        self.input_x0.clear()
        self.input_constant.clear()
        self.input_funcion.setCurrentIndex(-1)
        self.input_number_random.clear()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
