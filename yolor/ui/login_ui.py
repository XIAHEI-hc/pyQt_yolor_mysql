# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowTitle("登录")
        Form.setObjectName("Form")
        Form.resize(466, 368)
        
        Form.setWindowIcon(QtGui.QIcon('ui_img/save1.ico'))
        Form.setStyleSheet("#Form{\n"
"    background:white;\n"
"    border-radius:10px;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 50, 311, 71))
        self.label.setStyleSheet("#label{\n"
"    text-align:right;\n"
"    font-family:;\n"
"    font: 28pt \"华文楷体\";\n"
"    font-size:30px;\n"
"    font-weight:bold;\n"
"    }")
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(110, 130, 241, 61))
        self.username.setStyleSheet("#username{\n"
"    border:0px;    \n"
"    margin:10px;\n"
"    margin-left:10px; \n"
"    margin-right:10px;\n"
"    border-bottom: 2px solid #B3B3B3;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:20px;\n"
"    font-weight:bold;\n"
"}")
        self.username.setObjectName("username")
        self.passward = QtWidgets.QLineEdit(Form)
        self.passward.setGeometry(QtCore.QRect(110, 190, 241, 61))
        self.passward.setStyleSheet("#passward{\n"
"    border:0px;    \n"
"    margin:10px;\n"
"    margin-left:10px; \n"
"    margin-right:10px;\n"
"    border-bottom: 2px solid #B3B3B3;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:20px;\n"
"    font-weight:bold;\n"
"}")
        self.passward.setInputMask("")
        self.passward.setText("")
        self.passward.setObjectName("passward")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(110, 280, 93, 28))
        self.login.setStyleSheet("#login{\n"
"    border:0px;\n"
"    height:30px;\n"
"    border-radius:15px;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:20px;\n"
"    color:white;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);\n"
"    }\n"
"#login:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
" \n"
"#login:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")
        self.login.setObjectName("login")
        self.resiger = QtWidgets.QPushButton(Form)
        self.resiger.setGeometry(QtCore.QRect(250, 280, 93, 28))
        self.resiger.setStyleSheet("#resiger{\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"    height:30px;\n"
"    border-radius:15px;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:20px;\n"
"    color:white;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);\n"
"    }\n"
"#resiger:hover{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
" }\n"
" \n"
"#resiger:pressed{\n"
"     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
"     }")
        self.resiger.setObjectName("resiger")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 329, 201, 31))
        self.label_2.setStyleSheet("#label_2{\n"
"    \n"
"\n"
"    font: 75 italic 14pt \"Times New Roman\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 72, 61))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "智慧火灾监控预警系统"))
        self.username.setPlaceholderText(_translate("Form", "用户名"))
        self.passward.setPlaceholderText(_translate("Form", "密码"))
        self.login.setText(_translate("Form", "登录"))
        self.resiger.setText(_translate("Form", "注册"))
        self.label_2.setText(_translate("Form", "Writed By Yang"))
