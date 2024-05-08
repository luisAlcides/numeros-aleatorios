import os
import sys

from PyQt6.QtGui import QIcon

from view.randomNumberView import MainWindow
from PyQt6.QtWidgets import QApplication

script_directory = os.path.dirname(os.path.abspath(__file__))
ico_solve = os.path.join(script_directory, 'icons', 'solve.png')

class Aleatorios:
    def __init__(self):
        self.app = QApplication([])
        self.app.setWindowIcon(QIcon(ico_solve))
        self.ui = MainWindow()
        self.app.exec()
