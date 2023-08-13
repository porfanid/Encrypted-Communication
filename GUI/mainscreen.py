# This Python file uses the following encoding: utf-8
import sys
sys.path.append("..")
from gen import Encrypted_Communication
from send_to_server import Database

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

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
        self.ui.send.clicked.connect(self.send_message)

    def register(self):
        email_register=self.ui.email_register.text()
        self.database.set_email(email_register)
        self.key=self.client.generate_key(email_register)
        self.show_message("You can successfully chat")
    
    def send_message(self):
        email_receiver=self.ui.email_receiver.text()
        message = self.ui.textEdit.toPlainText()
        key = open("../keys/"+email_receiver+".asc").read()
        encrypted_message = self.client.encrypt_message(message, key)
        self.database.send_message(email_receiver, encrypted_message)
        self.show_message("Message has been sent successfully")
    
    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Chat Message")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainScreen()
    widget.show()
    sys.exit(app.exec())
