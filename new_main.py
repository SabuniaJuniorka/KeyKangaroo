import sys
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

        self.window_width = int(primary_screen_width * 0.5)
        self.window_height = int(primary_screen_height * 0.6)

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
        header = QLabel("Welcome to KeyKangaroo!", parent_label)
        header.setAlignment(Qt.AlignCenter)
        parent_layout.addWidget(header)
        header.setObjectName("header")

        # lower label container (splits into 2 vertical labels)
        lower_label_container = QWidget(parent_label)
        lower_layout = QHBoxLayout(lower_label_container)

        # left and right vertical labels in the lower section
        input_widget_container = QWidget(lower_label_container)
        input_widget_layout = QVBoxLayout(input_widget_container)
        # set maximum width of input container
        input_widget_container.setMaximumWidth(self.window_width // 2)

        button_widget_container = QWidget(lower_label_container)
        button_widget_layout = QHBoxLayout(button_widget_container)

        # add input and append it to input container
        self.user_input_number = QLineEdit(input_widget_container)
        input_widget_layout.addWidget(self.user_input_number)
        self.user_input_number.setPlaceholderText("Enter length of password you want to generate")

        # add generate button and append it to input container
        generate_password_button = QPushButton("Generate new password", input_widget_container)
        input_widget_layout.addWidget(generate_password_button)


        # add submit and what is a secure password button and append them to button container

        submit_button = QPushButton("Submit", button_widget_container)
        button_widget_layout.addWidget(submit_button)

        what_makes_password_secure_button = QPushButton("What makes password secure?", button_widget_container)
        button_widget_layout.addWidget(what_makes_password_secure_button)

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
            QLabel {
                font-size: 24pt;
            }
            QLabel#header {
                font-size: 48pt;
            }
            QWidget {
                border: 2px solid red;
            }
            QPushButton, QLineEdit {
                font-size: 12pt;
                border: 2px solid blue;
            }
        """)

        # set layout for the central widget
        central_widget.setLayout(main_layout)

        generate_password_button.clicked.connect(self.take_input_from_text_box)

    def take_input_from_text_box(self):
        text_from_input = self.user_input_number.text()
        print(text_from_input)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
