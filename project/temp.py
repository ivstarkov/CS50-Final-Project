import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

class CreatePage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.homeBtn = QPushButton("Home") 

        self.frontLabel = QLabel("Front") 
        self.frontLabel.setFont(QFont("Decorative", 20))
        self.frontEdit = QTextEdit(placeholderText="frontEdit") 
        self.frontEdit.setFont(QFont("Decorative", 11))

        self.backLabel = QLabel("Back") 
        self.backLabel.setFont(QFont("Decorative", 20))
        self.backEdit = QTextEdit(placeholderText="backEdit") 
        self.backEdit.setFont(QFont("Decorative", 11))

        grid = QGridLayout()
        grid.addWidget(self.homeBtn,    0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)
        grid.addWidget(self.frontLabel, 1, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.frontEdit,  2, 0)
        grid.addWidget(self.backLabel,  3, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.backEdit,   4, 0)

        self.setLayout(grid)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myapp = CreatePage()
    myapp.show()
    sys.exit(app.exec_())