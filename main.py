import sys
import sqlite3
from PyQt6 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.coffeeList.itemClicked.connect(self.display_coffee_info)
        self.updateButton.clicked.connect(self.load_coffee_data)
        self.searchLineEdit.textChanged.connect(self.filter_coffee_list)

        self.load_coffee_data()

    def load_coffee_data(self):
        self.coffeeList.clear()

        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM coffee')
        self.coffee_data = cursor.fetchall()

        for row in self.coffee_data:
            self.coffeeList.addItem(f"{row[1]} - {row[2]}")

        conn.close()

    def display_coffee_info(self, item):
        coffee_name = item.text().split(" - ")[0]

        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM coffee WHERE name = ?', (coffee_name,))
        row = cursor.fetchone()

        if row:
            self.nameLabel.setText(row[1])
            self.roastLabel.setText(row[2])
            self.typeLabel.setText(row[3])
            self.descriptionLabel.setText(row[4])
            self.priceLabel.setText(f"${row[5]:.2f}")
            self.packageLabel.setText(row[6])

        conn.close()

    def filter_coffee_list(self):
        search_text = self.searchLineEdit.text().lower()
        self.coffeeList.clear()

        for row in self.coffee_data:
            if search_text in row[1].lower():
                self.coffeeList.addItem(f"{row[1]} - {row[2]}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())