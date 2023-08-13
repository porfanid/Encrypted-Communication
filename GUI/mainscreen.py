# This Python file uses the following encoding: utf-8
import sys
sys.path.append("..")
from gen import Encrypted_Communication
from send_to_server import Database

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainScreen

class MainScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)

        # adding the base functions
        self.database=Database()
        self.client=Encrypted_Communication(self.database)
        self.key=None

        # adding the functions to the buttons
        self.ui.register_2.clicked.connect(self.register)

    def register(self):
        email_register=self.ui.email_register.text()
        self.database.set_email(email_register)
        self.key=self.client.generate_key(email_register)
        print("register clicked", email_register)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainScreen()
    widget.show()
    sys.exit(app.exec())
