import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("test.ui", self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        f_name = QFileDialog.getExistingDirectory(self, "Chose Directory", r"D:\Games", QFileDialog.Option.DontUseNativeDialog) 
        print(f_name)
        self.file_name.setText(f_name)


app = QApplication(sys.argv)
main_window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedWidth(400)
widget.setFixedHeight(200)

widget.show()

sys.exit(app.exec())