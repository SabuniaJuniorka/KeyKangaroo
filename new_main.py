import sys
import pyperclip
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLineEdit)
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        primary_screen = QGuiApplication.primaryScreen()
        primary_screen_resolution = primary_screen.geometry()
        primary_screen_width = primary_screen_resolution.width()
        primary_screen_height = primary_screen_resolution.height()

        self.window_width = int(primary_screen_width * 0.6)
        self.window_height = int(primary_screen_height * 0.8)

        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.setWindowTitle("KeyKangaroo Password Manager")
        self.setWindowIcon(QIcon("kangaroo.png"))  # Set the small icon near title

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        # parent label container
        parent_label = QWidget(self)
        parent_layout = QVBoxLayout(parent_label)
        parent_label.setLayout(parent_layout)

        # upper label
        self.header = QLabel("Welcome to KeyKangaroo!", parent_label)
        self.header.setAlignment(Qt.AlignCenter)
        parent_layout.addWidget(self.header)
        self.header.setObjectName("header")

        # lower label container (splits into 2 vertical labels)
        lower_label_container = QWidget(parent_label)
        lower_layout = QHBoxLayout(lower_label_container)

        # left and right vertical labels in the lower section
        input_widget_container = QWidget(lower_label_container)
        input_widget_layout = QVBoxLayout(input_widget_container)
        # set maximum width of input container
        input_widget_container.setMaximumWidth(self.window_width // 2)
        input_widget_container.setObjectName("input_container")

        button_widget_container = QWidget(lower_label_container)
        button_widget_layout = QHBoxLayout(button_widget_container)
        button_widget_container.setObjectName("button_container")

        # add input and append it to input container
        self.user_input_number = QLineEdit(input_widget_container)
        input_widget_layout.addWidget(self.user_input_number)
        self.user_input_number.setPlaceholderText("Enter length of password")

        # add generate button and append it to input container
        generate_password_button = QPushButton("Generate new password", input_widget_container)
        input_widget_layout.addWidget(generate_password_button)


        # add copy to clipboard and what is a secure password button and append them to button container

        self.copy_to_clipboard_button = QPushButton("Copy password to clipboard", button_widget_container)
        button_widget_layout.addWidget(self.copy_to_clipboard_button)
        self.copy_to_clipboard_button.hide()

        self.what_makes_password_secure_button = QPushButton("What makes password secure?", button_widget_container)
        button_widget_layout.addWidget(self.what_makes_password_secure_button)
        self.what_makes_password_secure_button.setObjectName("secure_password")

        # add left and right labels to the lower layout
        lower_layout.addWidget(input_widget_container)
        lower_layout.addWidget(button_widget_container)

        # add lower container to the parent layout
        parent_layout.addWidget(lower_label_container)

        # add parent label to the main layout
        main_layout.addWidget(parent_label)

        # styling
        self.setStyleSheet("""
            * {
            font-family: Roboto Mono;
            }
            QWidget{
                background-color: #FBE5B6;
            }
            QLabel {
                font-size: 24pt;
            }
            QLabel#header {
                font-size: 48pt;
                border: 2px solid black;
            }
            QWidget {
                border: 2px solid red;
            }
            QWidget#input_container {
                background-color: #FB6A75;
            }
            QWidget#button_container {
                background-color: #00C7B7;
            }
            QLineEdit{
                background-color: #2C6E63;
                color: white;
            }
            QPushButton, QLineEdit {
                font-size: 12pt;
                border: 2px solid blue;
                height: 100px;
                min-width: 10em;
                max-width: 30em;
            }
            QPushButton {
                background-color: #CE9865;
            }
            QPushButton::hover {
                background-color: #F38218;
            }
            QPushButton#secure_password {
                background-color: #F8B735;
            }
            QPushButton#secure_password::hover {
                background-color: #faca69;
            }

        """)

        # set layout for the central widget
        central_widget.setLayout(main_layout)

        generate_password_button.clicked.connect(self.generate_password)
        generate_password_button.clicked.connect(self.show_copy_button)

        self.copy_to_clipboard_button.clicked.connect(self.copy_password_to_clipboard)
        self.what_makes_password_secure_button.clicked.connect(self.what_makes_password_secure)

    # function which generates password based on user input
    def generate_password(self):
        import string
        import random

        # take the input from user_input

        length_of_password = self.user_input_number.text()

        # get all characters needed to create secure password

        ascii_lowercase = list(string.ascii_lowercase)
        ascii_uppercase = list(string.ascii_uppercase)
        digits = list(string.digits)
        special_chars = list(string.punctuation)
        special_chars.remove("`")
        special_chars.remove("|")

        length_of_password = int(length_of_password)

        # check the length of the input and inform the user if the password is too short to be secure

        if length_of_password < 12:
            print("password is too short")
            self.header.setText(f"Password is too short!\nShould be at least 12 characters")
        elif length_of_password > 32:
            print("password is too long")
            self.header.setText(f"Password is too long!\nShould be at most 32 characters")
        else:

            # shuffle lists of characters

            random.shuffle(ascii_lowercase)
            random.shuffle(ascii_uppercase)
            random.shuffle(digits)
            random.shuffle(special_chars)

            # part the length of password in 2
            password_part_1 = round(length_of_password * 0.3)
            password_part_2 = round(length_of_password * 0.2)

            generated_signs = []

            # append the number of signs to the list of signs

            for sign in range(password_part_1):
                generated_signs.append(ascii_lowercase[sign])
                generated_signs.append(ascii_uppercase[sign])

            for sign in range(password_part_2):
                generated_signs.append(digits[sign])
                generated_signs.append(special_chars[sign])

            # shuffle generated signs once again

            random.shuffle(generated_signs)

            # make a password from random signs by joining them

            password = "".join(generated_signs)

            self.header.setText(f"Your password:\n{password}")


    def show_copy_button(self):

        # check the length of password and show/hide button to copy generated password
        length_of_password = int(self.user_input_number.text())
        if length_of_password >= 12:
            self.copy_to_clipboard_button.show()
        else:
            self.copy_to_clipboard_button.hide()

    def copy_password_to_clipboard(self):

        # get the header text and extract password from it
        text = self.header.text()
        text_splited = text.split()
        password = text_splited[2]

        # copy password to system clipboard

        pyperclip.copy(password)
        self.header.setText("Password copied to clipboard!")

        #clear the input field

        self.user_input_number.clear()

    def what_makes_password_secure(self):
        secure_password_text = """
        A password should be <b>at least 12 characters long</b>.<br>
        A password <b>should include a combination of letters, both uppercase and lowercase, numbers, and characters.</b><br>
        You must have a <b>unique password</b> for each online account.<br>
        A password <b>shouldn’t include any of your personal information</b> like your birthday or address.<br>
        A password <b>shouldn’t contain any consecutive letters or numbers</b> <i>(i.e. ABCD, 1234, etc.)</i><br>
        A password <b>shouldn’t be the word “password” or the same letter or number repeated.</b><br>
        """
        self.header.setText(secure_password_text)
        self.header.setStyleSheet("font-size: 14pt;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
