import sys
import deleting
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"main_window.ui", self)
        
        self.browse_btn.clicked.connect(self.browse)
        self.analyze_btn.clicked.connect(self.analyze)
        self.delete_btn.clicked.connect(self.delete)


    def browse(self):
        global dir
        dir = QFileDialog.getExistingDirectory(self, "Chose Directory", r"D:\Games", QFileDialog.Option.DontUseNativeDialog) 
        self.dir_name.setText(dir)


    def analyze(self):
        global to_remove
        if to_remove := deleting.analyze(dir):
            self.listWidget.addItems(to_remove)
        else:
            self.listWidget.addItem("There are no duplicates to remove in current directory")


    def delete(self):
        deleting.remove(dir, to_remove)
        message_window.show()
        self.listWidget.clear()


class MessageWindow(QDialog):
    def __init__(self):
        super(MessageWindow, self).__init__()
        loadUi(r"message_window.ui", self)
        self.ok_btn.clicked.connect(lambda:self.close())      
        





app = QApplication([])
main_window = MainWindow()
message_window = MessageWindow()
main_window.show()
sys.exit(app.exec())