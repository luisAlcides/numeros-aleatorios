from PyQt6.QtWidgets import QTableWidgetItem

from PyQt6.QtWidgets import QMessageBox


def message(message):
    mBox = QMessageBox()
    mBox.setText(message)
    mBox.exec()

def add_to_table(table, data):
        table.setRowCount(0)

        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0

        table.setRowCount(rows)
        table.setColumnCount(cols)

        for i, row_data in enumerate(data):
            for j, (key, value) in enumerate(row_data.items()):
                item_text = f'{key}: {value}'
                item = QTableWidgetItem(item_text)
                table.setItem(i, j, item)
                

def number_divide(number):
        size = 8
        number = str(number)
        if len(number) < size:
            number = number.zfill(8)
        number = [int(i) for i in str(number)]
        half = len(number) // 2
        half_number = number[half - 2: half + 2]
        number_str = ''.join(map(str, half_number))

        return number_str