import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(x, y, width. height) - set the coordinate of the app and it's size
        self.setGeometry(960, 540, 2000, 1500)
        self.setWindowTitle("KeyKangaroo Password Manager")
        self.initUI()
        self.setWindowIcon(QIcon("kangaroo.png")) # set the small icon near title
        """
        # label = QLabel("Hello", self) - create new label, first arg is a text, second is the parent widget
        label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 50)) - set font of the label (font family, font size)
        label.setFont(QFont("Arial", 50))
        label.setGeometry(0,0, 500, 500)
        # label.setStyleSheet("css-prop;") - set the style of the label
        label.setStyleSheet("color: blue;"
                            "background-color: red;"
                            "font-weight: bold;")

        # label.setAlignment(Qt.AlignCenter) - set the position of the label, uses one of 9 arguments
        label.setAlignment(Qt.AlignCenter)

        #create new label and set it's geometry
        label2 = QLabel(self)
        label2.setGeometry(0, 500, 500, 500)

        # create the pixmap object storing the picture
        pixmap = QPixmap("kangaroo2.png")
        # "append" the pic to the label
        label2.setPixmap(pixmap)
        # the method below makes picture scale with size og the label
        label2.setScaledContents(True)

        #label2.setGeometry((self.width() - label.width()) // 2,
                           self.height() - label.height(),
                           label2.width(),
                           label2.height())
        """
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        welcomeLabel = QLabel("Welcome!", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)

        welcomeLabel.setStyleSheet("background-color: red;")
        label3.setStyleSheet("background-color: yellow;")
        label4.setStyleSheet("background-color: brown;")

        vbox = QVBoxLayout()

        # grid = QGridLayout()
        # grid.addWidget(label, row, colum)

        vbox.addWidget(welcomeLabel)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()