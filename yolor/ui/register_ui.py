# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
class Ui_Form2(object):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(412, 313)
        Form2.setWindowTitle("注册")
        Form2.setWindowIcon(QtGui.QIcon('ui_img/save1.ico'))
        Form2.setStyleSheet(u"#Form2{\n"
"	background:white;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.reg_label = QLabel(Form2)
        self.reg_label.setObjectName(u"reg_label")
        self.reg_label.setGeometry(QRect(130, 40, 171, 41))
        self.reg_label.setStyleSheet(u"#reg_label{\n"
"    text-align:right;\n"
"    font-family:'Microsoft YaHei';\n"
"    font-size:30px;\n"
"    font-weight:bold;\n"
"    }")
        self.username_2 = QLineEdit(Form2)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setGeometry(QRect(90, 100, 221, 51))
        self.username_2.setStyleSheet(u"#username_2{\n"
"	border:0px;    \n"
"    margin:10px;\n"
"	margin-left:10px; \n"
"	margin-right:10px;\n"
"    border-bottom: 2px solid #B3B3B3;\n"
"    font-family:'Microsoft YaHei';\n"
"    font-size:20px;\n"
"    font-weight:bold;\n"
"}")
        self.password_2 = QLineEdit(Form2)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(90, 160, 221, 51))
        self.password_2.setStyleSheet(u"#password_2{\n"
"	border:0px;    \n"
"    margin:10px;\n"
"	margin-left:10px; \n"
"	margin-right:10px;\n"
"    border-bottom: 2px solid #B3B3B3;\n"
"    font-family:'Microsoft YaHei';\n"
"    font-size:20px;\n"
"    font-weight:bold;\n"
"}")
        self.reg_but = QPushButton(Form2)
        self.reg_but.setObjectName(u"reg_but")
        self.reg_but.setGeometry(QRect(90, 240, 93, 28))
        self.reg_but.setStyleSheet(u"#reg_but{\n"
"	border:0px;\n"
"    height:30px;\n"
"    border-radius:15px;\n"
"    font-family:'Microsoft YaHei';\n"
"    font-size:20px;\n"
"	color:white;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);\n"
"    }\n"
"#reg_but:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
"#reg_but:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")
        self.cancel = QPushButton(Form2)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(210, 240, 93, 28))
        self.cancel.setStyleSheet(u"#cancel{\n"
"	border:0px;\n"
"    height:30px;\n"
"    border-radius:15px;\n"
"    font-family:'Microsoft YaHei';\n"
"    font-size:20px;\n"
"	color:white;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);\n"
"    }\n"
"#cancel:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
"#cancel:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")

        self.retranslateUi(Form2)

        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", "注册", None))
        self.reg_label.setText(QCoreApplication.translate("Form2", u"\u8d26\u53f7\u6ce8\u518c", None))
        self.username_2.setPlaceholderText(QCoreApplication.translate("Form2", u"\u7528\u6237\u540d", None))
        self.password_2.setPlaceholderText(QCoreApplication.translate("Form2", u"\u5bc6\u7801", None))
        self.reg_but.setText(QCoreApplication.translate("Form2", u"\u6ce8\u518c", None))
        self.cancel.setText(QCoreApplication.translate("Form2", u"\u53d6\u6d88", None))
    # retranslateUi

