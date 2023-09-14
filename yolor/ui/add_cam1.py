# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_cam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addinfo(object):
    def setupUi(self, addinfo):
        addinfo.setObjectName("addinfo")
        addinfo.setWindowTitle("添加")

        addinfo.resize(456, 279)
        addinfo.setWindowIcon(QtGui.QIcon('ui_img/save1.ico'))
        addinfo.setStyleSheet("#addinfo{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.label = QtWidgets.QLabel(addinfo)
        self.label.setGeometry(QtCore.QRect(50, 50, 72, 21))
        self.label.setStyleSheet("font: 9pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addinfo)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 72, 15))
        self.label_2.setStyleSheet("font: 9pt \"Consolas\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(addinfo)
        self.pushButton.setGeometry(QtCore.QRect(90, 210, 93, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"}\n"
"/*悬停*/  \n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(234,244,252);\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"/*按下*/  \n"
"QPushButton:pressed\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"    background-color:rgb(235,246,247);\n"
"    /*左内边距为2像素，让按下时字向右移动2像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动2像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(addinfo)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 72, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(addinfo)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 100, 61, 28))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"}\n"
"/*悬停*/  \n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(234,244,252);\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"/*按下*/  \n"
"QPushButton:pressed\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"    background-color:rgb(235,246,247);\n"
"    /*左内边距为2像素，让按下时字向右移动2像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动2像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(addinfo)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 210, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"}\n"
"/*悬停*/  \n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(234,244,252);\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"/*按下*/  \n"
"QPushButton:pressed\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"    background-color:rgb(235,246,247);\n"
"    /*左内边距为2像素，让按下时字向右移动2像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动2像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(addinfo)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 271, 31))
        self.lineEdit.setStyleSheet("\n"
"QLineEdit{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"}\n"
"/*焦点样式*/\n"
"QLineEdit:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(addinfo)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 150, 271, 31))
        self.lineEdit_3.setStyleSheet("\n"
"QLineEdit{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"}\n"
"/*焦点样式*/\n"
"QLineEdit:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textBrowser = QtWidgets.QTextBrowser(addinfo)
        self.textBrowser.setGeometry(QtCore.QRect(140, 100, 191, 31))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"}\n"
"/*悬停*/  \n"
"QTextBrowser:hover\n"
"{\n"
"    background-color:rgb(234,244,252);\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"/*按下*/  \n"
"QTextBrowser:pressed\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"    background-color:rgb(235,246,247);\n"
"    /*左内边距为2像素，让按下时字向右移动2像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动2像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(addinfo)
        QtCore.QMetaObject.connectSlotsByName(addinfo)

    def retranslateUi(self, addinfo):
        _translate = QtCore.QCoreApplication.translate
        addinfo.setWindowTitle(_translate("addinfo", "添加"))
        self.label.setText(_translate("addinfo", "摄像头ID："))
        self.label_2.setText(_translate("addinfo", "本地文件："))
        self.pushButton.setText(_translate("addinfo", "添加"))
        self.label_4.setText(_translate("addinfo", "具体位置："))
        self.pushButton_3.setText(_translate("addinfo", "浏览"))
        self.pushButton_2.setText(_translate("addinfo", "取消"))
