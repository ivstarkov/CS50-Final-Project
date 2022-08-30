import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QSlider,
    QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt


class QButtonExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 200, 150)
        self.button = QPushButton(self, text="Ты не сможешь на меня нажать!")
        self.button.setEnabled(False)
        self.button.clicked.connect(self.handleButton)

        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.changeValue)

        boxLayout = QVBoxLayout(self)
        # boxLayout.addStretch(1)
        boxLayout.addWidget(self.button)
        boxLayout.addWidget(slider)


    def changeValue(self, value):
        if value > 50:
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def handleButton(self):
        QMessageBox.information(None, 'Сообщение от программы', "Да ладно! у тебя получилось!")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    myApplication = QButtonExample()
    myApplication.show()
    sys.exit(app.exec_())