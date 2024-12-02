import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QPushButton, QWidget


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(circle[3])
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)

        self.circle_widget = CircleWidget()
        self.setCentralWidget(self.circle_widget)

        self.add_circle_button = QPushButton('Add Circle', self)
        self.add_circle_button.clicked.connect(self.circle_widget.add_circle)
        self.add_circle_button.setGeometry(10, 10, 100, 30)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())