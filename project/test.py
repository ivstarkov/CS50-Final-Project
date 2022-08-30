import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog, QPushButton
from PyQt6.uic import loadUi



class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"main_window.ui", self)
        self.delete_btn.clicked.connect(lambda:message_window.show())


class MessageWindow(QDialog):
    def __init__(self):
        super(MessageWindow, self).__init__()
        loadUi(r"message_window.ui", self)
        self.ok_btn.clicked.connect(lambda:self.close())



app = QApplication([])

message_window = MessageWindow()
main_window = MainWindow()


main_window.show()


sys.exit(app.exec())