import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KeyKangaroo Password Manager")
        self.setWindowIcon(QIcon("kangaroo.png")) # set the small icon near title
        # self.setGeometry(x, y, width. height) - set the coordinate of the app and it's size
        self.setGeometry(960, 540, 2000, 1500)
        # self.button = QPushButton("Click me", self)
        # self.label = QLabel("OK", self)
        # self.checkbox = QCheckBox("Text of the checkbox", self) # ("text, parent widget)

        """
        self.radio1 = QRadioButton("Hasło literowe", self)
        self.radio2 = QRadioButton("Hasło wyrazowe", self)
        self.radio3 = QRadioButton("Hasło mieszane", self)

        self.radio4 = QRadioButton("Losowe", self)
        self.radio5 = QRadioButton("Nielosowe", self)

        # make groups of buttons
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        
        """

        """
        # create input box and submit button
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        """

"""
        # create 3 push buttons
        self.button1 = QPushButton("#1", self)
        self.button2 = QPushButton("#2", self)
        self.button3 = QPushButton("#3", self)
"""


        self.initUI()

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


"""

        # add central widget so you can set the layout method
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # make layout
        hbox = QHBoxLayout()

        # add things to the widget
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # append the layout to widget
        central_widget.setLayout(hbox)

        # set name for the objects so you can use them in CSS like styling later
        self.button1.setObjectName("b1")
        self.button2.setObjectName("b2")
        self.button3.setObjectName("b3")

        # the syntax of CSS like styling
        self.setStyleSheet("ex""
            QPushButton{
                font-size: 40px;
                font-family: Roboto;
                padding: 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 40px;
            }
            QPushButton#b1{
                background-color: red;
            }
            QPushButton#b2{
                background-color: yellow;
            }
            QPushButton#b3{
                background-color: blue;
            }
        """)
        
"""

"""
        # style the input box and submit button
        self.line_edit.setGeometry(50, 50, 500, 100)
        self.line_edit.setStyleSheet("font-size: 50px;"
                                     "font-family: Roboto;")
        self.line_edit.setPlaceholderText("Enter your password")

        self.button.setGeometry(600, 50, 250, 100)
        self.button.setStyleSheet("font-size: 50px;"
                                  "font-family: Roboto;")

        self.button.clicked.connect(self.submit)

    # make the button take input from the textbox into var
    def submit(self):
        text_from_button = self.line_edit.text()
        print(text_from_button)



"""

"""

        self.radio1.setGeometry(0, 0, 500, 100)
        self.radio2.setGeometry(0, 100, 500, 100)
        self.radio3.setGeometry(0, 200, 500, 100)
        self.radio4.setGeometry(0, 300, 500, 100)
        self.radio5.setGeometry(0, 400, 500, 100)

        # change stylesheet of all types
        self.setStyleSheet("QRadioButton{"
                           "font-size: 50px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")

        # add buttons to the groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)

    def radio_button_change(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected ")

"""

        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        #
        # welcomeLabel = QLabel("Welcome!", self)
        # label3 = QLabel("#3", self)
        # label4 = QLabel("#4", self)
        #
        # welcomeLabel.setStyleSheet("background-color: red;")
        # label3.setStyleSheet("background-color: yellow;")
        # label4.setStyleSheet("background-color: brown;")
        #
        # vbox = QVBoxLayout()
        #
        # # grid = QGridLayout()
        # # grid.addWidget(label, row, colum)
        #
        # vbox.addWidget(welcomeLabel)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        #
        # central_widget.setLayout(vbox)

"""
        creating button and label after click
        self.button.setGeometry(500, 0, 1000, 500)
        self.button.setStyleSheet("font-size: 50px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(500, 500, 1000, 500)
        self.label.setStyleSheet("font-size: 30px;")
"""

"""
        # styling checkbox
        self.checkbox.setGeometry(50, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 50px;")
    
        # connecting checkbox to the function signal
        self.checkbox.setChecked(False) # True makes checkbox checked by default
        self.checkbox.stateChanged.connect(self.checkbox_changed)
"""



"""
    # checking the state of checkbox and printing the value based of it
    def checkbox_changed(self, state):
        print(state)
        if state == Qt.Checked:
            print("True")
        else:
            print("False")
"""


"""
    def on_click(self):
        # creating button and label after click
        self.label.setText("COOL")
        print("Button clicked")
        self.button.setText("Clicked")
"""
"""


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()