import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from utils import message


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Interfaz con PyQt6')
        self.setGeometry(100, 100, 400, 200)  # Posición y tamaño de la ventana
        self.showMaximized()
        self.layout = QVBoxLayout(self)

        # Etiquetas y campos de entrada
        self.label_x0 = QLabel('X0:')
        self.input_x0 = QLineEdit()
        self.layout.addWidget(self.label_x0)
        self.layout.addWidget(self.input_x0)

        self.label_x1 = QLabel('X1:')
        self.input_x1 = QLineEdit()
        self.layout.addWidget(self.label_x1)
        self.layout.addWidget(self.input_x1)

        self.label_funcion = QLabel('Función:')
        self.input_funcion = QLineEdit()
        self.layout.addWidget(self.label_funcion)
        self.layout.addWidget(self.input_funcion)

        self.label_number_random = QLabel('Numeros de variables aleatorias:')
        self.input_number_random = QLineEdit()
        self.layout.addWidget(self.label_number_random)
        self.layout.addWidget(self.input_number_random)

        # Botón para imprimir respuestas
        self.button = QPushButton('Imprimir respuestas')
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.solver)

        # Espacio para imprimir respuestas
        self.label_respuestas = QLabel('Respuestas:')
        self.layout.addWidget(self.label_respuestas)
        self.label_respuestas_texto = QLabel('')
        self.layout.addWidget(self.label_respuestas_texto)

    def solver(self):
        x0 = int(self.input_x0.text().strip())
        x1 = int(self.input_x1.text().strip())
        fun = self.input_funcion.text().strip().split()
        quantity_random = int(self.input_number_random.text().strip())

        if fun is None:
            message('Función no válida')
        elif fun[1] == '*':
            self.multiply(x0, x1, quantity_random)
        elif fun[1] == '**2':
            self.elevate(fun[0])
        print(fun)

        answer = None
        self.label_respuestas_texto.setText(answer)

    def number_divide(self, number, quantity_random):
        number = [int(i) for i in str(number)]
        return number[1:quantity_random]

    def multiply(self, x0, x1, quantity_random):
        result = {}
        for i in range(quantity_random):
            y0 = x0 * x1
            x2 = self.number_divide(y0, quantity_random)
        self.label_respuestas.setText(str(2))

    def elevate(self, x0):
        pass
