from PyQt6.QtWidgets import QMessageBox


def message(message):
    mBox = QMessageBox()
    mBox.setText(message)
    mBox.exec()