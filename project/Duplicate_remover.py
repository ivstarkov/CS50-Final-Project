import sys
import deleting
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi


class MainWindow(QDialog):

    def __init__(self):

        super(MainWindow, self).__init__()
        loadUi(r"test.ui", self)
        
        self.browse_btn.clicked.connect(self.browse)
        self.analyze_btn.clicked.connect(self.analyze)
        self.delete_btn.clicked.connect(self.delete)


        



    def browse(self):
        global dir
        dir = QFileDialog.getExistingDirectory(self, "Chose Directory", r"D:\Games", QFileDialog.Option.DontUseNativeDialog) 
        self.dir_name.setText(dir)


    def analyze(self):
        global to_remove
        to_remove = deleting.analyze(dir)  
        self.listWidget.addItems(to_remove)


    def delete(self):
        deleting.remove(to_remove)


        
        




app = QApplication([])
main_window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedWidth(400)
widget.setFixedHeight(300)

widget.show()

sys.exit(app.exec())