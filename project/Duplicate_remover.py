import sys
import deleting
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog
from PyQt6.uic import loadUi


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"main_window.ui", self)
        self.initUI()


    def initUI(self):
        # Disable buttons
        self.analyze_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        
        self.browse_btn.clicked.connect(self.browse)
        self.analyze_btn.clicked.connect(self.analyze)
        self.delete_btn.clicked.connect(self.delete)


    def browse(self): 
        global directory
        if directory := QFileDialog.getExistingDirectory(self, "Chose Directory", r"D:\Games", QFileDialog.Option.DontUseNativeDialog):
            self.dir_name.setText(directory)
            self.analyze_btn.setEnabled(True)


    def analyze(self):
        global remove_list
        if remove_list := deleting.analyze(directory):
            self.listWidget.addItems(remove_list)
            self.delete_btn.setEnabled(True)
        else:
            self.listWidget.addItem("There are no duplicates to remove in current directory")


    def delete(self):
        deleting.remove(directory, remove_list)
        self.listWidget.clear()
        QMessageBox.information(None, "Done!", "Duplicate Files were Deleted ")
        

       





app = QApplication([])
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())

