import sys

from view import MainWindow
from PyQt6.QtWidgets import QApplication

class Aleatorios:
    def __init__(self):
        self.app = QApplication([])
        self.ui = MainWindow()
        self.app.exec()