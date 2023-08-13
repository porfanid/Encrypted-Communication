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
    QSizePolicy, QTextBrowser, QTextEdit, QWidget)

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
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
        self.textEdit.setGeometry(QRect(20, 330, 671, 221))
        self.email_receiver = QLineEdit(MainScreen)
        self.email_receiver.setObjectName(u"email_receiver")
        self.email_receiver.setGeometry(QRect(220, 290, 241, 26))
        self.label_2 = QLabel(MainScreen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 300, 66, 18))
        self.label_3 = QLabel(MainScreen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 290, 41, 18))
        self.send = QPushButton(MainScreen)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(330, 570, 87, 26))
        self.textBrowser = QTextBrowser(MainScreen)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(190, 50, 561, 231))
        self.label_4 = QLabel(MainScreen)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 10, 66, 18))

        self.retranslateUi(MainScreen)

        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"MainScreen", None))
        self.label.setText(QCoreApplication.translate("MainScreen", u"Email:", None))
        self.register_2.setText(QCoreApplication.translate("MainScreen", u"Start Chat", None))
        self.label_2.setText(QCoreApplication.translate("MainScreen", u"Message", None))
        self.label_3.setText(QCoreApplication.translate("MainScreen", u"Email", None))
        self.send.setText(QCoreApplication.translate("MainScreen", u"Send", None))
        self.label_4.setText(QCoreApplication.translate("MainScreen", u"Messages", None))
    # retranslateUi

