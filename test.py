from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sygnal and Slots")
        #self.setWindowIcon(QIcon("qt.png"))
        #self.setFixedHeight(300)
        #self.setFixedWidth(300)
        #self.setGeometry(100,200,100,200)
        #self.setStyleSheet("background-color:green")

        self.create_widgets()


    def create_widgets(self):
        bttn = QPushButton("Harder!", self)
        #bttn.move(150, 150)
        bttn.setGeometry(150, 150, 50, 50)
        bttn.setStyleSheet("background-color:green")
        bttn.setIcon(QIcon(".png"))
        bttn.clicked.connect(self.clicked)

        self.label = QLabel("Label", self)
        self.label.setGeometry(150, 100, 50, 20)
        self.label.setStyleSheet("background-color:green")


    def clicked(self):
        self.label.setText("Presed")
        self.label.setStyleSheet("background-color:red")



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
