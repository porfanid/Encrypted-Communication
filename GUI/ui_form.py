# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"Chat")
        MainScreen.resize(800, 600)
        self.email_register = QLineEdit(MainScreen)
        self.email_register.setObjectName(u"email_register")
        self.email_register.setGeometry(QRect(70, 20, 113, 26))
        self.label = QLabel(MainScreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 28, 61, 20))
        self.register_2 = QPushButton(MainScreen)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setGeometry(QRect(40, 60, 87, 26))
        self.textEdit = QTextEdit(MainScreen)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 160, 671, 221))
        self.email_receiver = QLineEdit(MainScreen)
        self.email_receiver.setObjectName(u"email_receiver")
        self.email_receiver.setGeometry(QRect(220, 110, 241, 26))
        self.label_2 = QLabel(MainScreen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 140, 66, 18))
        self.label_3 = QLabel(MainScreen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 120, 41, 18))
        self.send = QPushButton(MainScreen)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(280, 390, 87, 26))

        self.retranslateUi(MainScreen)

        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"MainScreen", None))
        self.label.setText(QCoreApplication.translate("MainScreen", u"Email:", None))
        self.register_2.setText(QCoreApplication.translate("MainScreen", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("MainScreen", u"Message", None))
        self.label_3.setText(QCoreApplication.translate("MainScreen", u"Email", None))
        self.send.setText(QCoreApplication.translate("MainScreen", u"Send", None))
    # retranslateUi

