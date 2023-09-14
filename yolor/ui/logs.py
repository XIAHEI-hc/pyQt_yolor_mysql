# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log(object):
    def setupUi(self, Form4):
        Form4.setObjectName("Form4")
        Form4.setWindowTitle("日志信息")

        Form4.resize(935, 562)
        Form4.setWindowIcon(QtGui.QIcon('ui_img/save1.ico'))
        Form4.setStyleSheet("#Form4{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label = QtWidgets.QLabel(Form4)
        self.label.setGeometry(QtCore.QRect(250, 50, 451, 41))
        self.label.setStyleSheet("#label{\n"
"    text-align:right;\n"
"\n"
"    font: 36pt \"华文楷体\";\n"
"    font-size:35px;\n"
"    font-weight:bold;\n"
"    color: black;\n"
"    }")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form4)
        self.line.setGeometry(QtCore.QRect(20, 100, 891, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(Form4)
        self.groupBox.setGeometry(QtCore.QRect(30, 440, 881, 91))
        self.groupBox.setStyleSheet("#groupBox{\n"
"    text-align:right;\n"
"    \n"
"    font: 15pt \"华文楷体\";\n"
"    \n"
"    font-weight:bold;\n"
"    color: black;\n"
"    }")
        self.groupBox.setObjectName("groupBox")
        self.sel_all = QtWidgets.QPushButton(self.groupBox)
        self.sel_all.setGeometry(QtCore.QRect(90, 30, 93, 41))
        self.sel_all.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"color: black;\n"
"font-family:\'Microsoft YaHei\';\n"
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
        self.sel_all.setObjectName("sel_all")
        self.return_bt = QtWidgets.QPushButton(self.groupBox)
        self.return_bt.setGeometry(QtCore.QRect(700, 30, 93, 41))
        self.return_bt.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"color: black;\n"
"font-family:\'Microsoft YaHei\';\n"
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
"\n"
"}\n"
"")
        self.return_bt.setObjectName("return_bt")
        self.clear_bt = QtWidgets.QPushButton(self.groupBox)
        self.clear_bt.setGeometry(QtCore.QRect(500, 30, 93, 41))
        self.clear_bt.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"color: black;\n"
"font-family:\'Microsoft YaHei\';\n"
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
        self.clear_bt.setObjectName("clear_bt")
        self.condit = QtWidgets.QPushButton(self.groupBox)
        self.condit.setGeometry(QtCore.QRect(290, 30, 93, 41))
        self.condit.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"color: black;\n"
"font-family:\'Microsoft YaHei\';\n"
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
        self.condit.setObjectName("condit")
        self.tableWidget = QtWidgets.QTableWidget(Form4)
        self.tableWidget.setGeometry(QtCore.QRect(20, 160, 901, 271))
        self.tableWidget.setStyleSheet("/*表格的一种美化方式*/\n"
"QHeaderView\n"
"{\n"
"    background:transparent;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    font-size:18px;\n"
"    font-family:\"Microsoft YaHei\";\n"
"    color:#FFFFFF;\n"
"    background:rgb(63, 63, 190);\n"
"    border:none;\n"
"    text-align:left;\n"
"    min-height:49px;\n"
"    max-height:49px;\n"
"    margin-left:0px;\n"
"    padding-left:0px;\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"    background:#FFFFFF;\n"
"    border:none;\n"
"\n"
"    font-size:20px;\n"
"    font-family:\"Microsoft YaHei\";\n"
"    color:#666666;\n"
"}\n"
"QTableWidget::item\n"
"{\n"
"    border-bottom:1px solid #EEF1F7 ;\n"
"}\n"
"\n"
"QTableWidget::item::selected\n"
"{\n"
"    color:black;\n"
"    background:#EFF4FF;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background: rgba(255,255,255,20%);\n"
"    border: 0px solid grey;\n"
"    border-radius:3px;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background:rgba(255,255,255,10%);\n"
"}\n"
"\n"
"\n"
"QScollBar::add-line:vertical, QScrollBar::sub-line:vertical\n"
"{\n"
"    background:transparent;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_2 = QtWidgets.QLabel(Form4)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 121, 31))
        self.label_2.setStyleSheet("#label_2{\n"
"    \n"
"    font: 16pt \"楷体\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form4)
        self.textBrowser.setGeometry(QtCore.QRect(160, 120, 131, 31))
        self.textBrowser.setStyleSheet("#textBrowser{    \n"
"    font: 11pt \"Eras Demi ITC\";\n"
"\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form4)
        self.label_3.setGeometry(QtCore.QRect(380, 120, 91, 31))
        self.label_3.setStyleSheet("#label_3{\n"
"    \n"
"    font: 16pt \"楷体\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form4)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 120, 61, 31))
        self.textBrowser_2.setStyleSheet("#textBrowser{    \n"
"    font: 11pt \"Eras Demi ITC\";\n"
"\n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        _translate = QtCore.QCoreApplication.translate
        Form4.setWindowTitle(_translate("Form4", "Form"))
        self.label.setText(_translate("Form4", "智慧火灾监控预警系统日志"))
        self.groupBox.setTitle(_translate("Form4", "功能区"))
        self.sel_all.setText(_translate("Form4", "查询全部"))
        self.return_bt.setText(_translate("Form4", "返回"))
        self.clear_bt.setText(_translate("Form4", "清空"))
        self.condit.setText(_translate("Form4", "条件查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form4", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form4", "地区"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form4", "摄像头ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form4", "具体位置"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form4", "日志信息"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form4", "日期"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form4", "时间"))
        self.label_2.setText(_translate("Form4", "数据库IP"))
        self.textBrowser.setHtml(_translate("Form4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Demi ITC\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">127.0.0.1</span></p></body></html>"))
        self.label_3.setText(_translate("Form4", "端口号"))
        self.textBrowser_2.setHtml(_translate("Form4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">3306</span></p></body></html>"))
