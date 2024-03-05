# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'esp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        Form.setMinimumSize(QSize(400, 200))
        Form.setMaximumSize(QSize(400, 200))
        icon = QIcon()
        icon.addFile(u"kb.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(60, 20, 68, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 41, 22))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 15, 60, 30))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 20, 71, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 20, 71, 21))
        self.label_3.setFont(font)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 15, 60, 30))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 60, 20, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 60, 20, 20))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 60, 20, 20))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(340, 60, 20, 20))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 160, 20, 20))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 160, 20, 20))
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(260, 160, 20, 20))
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(340, 160, 20, 20))
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 60, 54, 20))
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 160, 54, 20))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 110, 60, 20))
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 110, 60, 20))
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(240, 110, 60, 20))
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(320, 110, 60, 20))
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 100, 50, 40))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"espKeyBoard", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3 : ", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#9a0000;\">\u8fde\u63a5\u5931\u8d25</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00a126;\">\u8fde\u63a5\u6210\u529f</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">A</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">B</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">C</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">D</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00a126;\">OK</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00a126;\">OK</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00a126;\">OK</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#00a126;\">OK</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6309\u952e\u5e8f\u53f7\uff1a</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d4b\u8bd5\uff1a</p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"A", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"B", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"C", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"D", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49", None))
    # retranslateUi

