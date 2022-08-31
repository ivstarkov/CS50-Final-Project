import sys
from deleting import analyze, remove, rename
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog, QLineEdit
from PyQt6.uic import loadUi


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"main_window.ui", self)
        self.directory = ""
        self.remove_list = []
        self.rename_list = []
        self.initUI()


    def initUI(self):
        # Disable buttons
        self.analyze_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        
        self.browse_btn.clicked.connect(self.browse)
        self.analyze_btn.clicked.connect(self.analyze)
        self.delete_btn.clicked.connect(self.delete)


    def browse(self): 
        path = self.dir_name.text()
        if not path:
            path = "C:\\"
        self.directory = QFileDialog.getExistingDirectory(self, "Chose Directory", path, QFileDialog.Option.DontUseNativeDialog)
        if self.directory:
            self.dir_name.setText(self.directory)

            self.analyze_btn.setEnabled(True)


    def analyze(self):
        self.remove_list, self.rename_list = analyze(self.directory)
        if self.remove_list:
            self.listWidget.addItems(self.remove_list)
            self.delete_btn.setEnabled(True)
        else:
            self.listWidget.addItem("There are no duplicates to remove in current directory")


    def delete(self):
        remove(self.directory, self.remove_list)
        rename(self.directory, self.rename_list)
        self.listWidget.clear()
        QMessageBox.information(None, "Done!", "Duplicate Files were Deleted ")



app = QApplication([])
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())

