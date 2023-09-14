# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sel_Form(object):
    def setupUi(self, sel_Form):
        sel_Form.setObjectName("sel_Form")
        sel_Form.resize(379, 366)
        sel_Form.setWindowTitle("查找")
        sel_Form.setWindowIcon(QtGui.QIcon('ui_img/save1.ico'))
        sel_Form.setStyleSheet("#sel_Form{\n"
"    background:white;\n"
"    border-radius:10px;\n"
"}")
        self.camID = QtWidgets.QLabel(sel_Form)
        self.camID.setGeometry(QtCore.QRect(20, 140, 131, 31))
        self.camID.setStyleSheet("#camID{\n"
"    font: 15pt \"华文楷体\";\n"
"    \n"
"    color:black;\n"
"}")
        self.camID.setObjectName("camID")
        self.Date = QtWidgets.QLabel(sel_Form)
        self.Date.setGeometry(QtCore.QRect(20, 260, 71, 41))
        self.Date.setStyleSheet("#Date{\n"
"    font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.Date.setObjectName("Date")
        self.location = QtWidgets.QLabel(sel_Form)
        self.location.setGeometry(QtCore.QRect(30, 80, 71, 31))
        self.location.setStyleSheet("#location{\n"
"    \n"
"    font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.location.setObjectName("location")
        self.sel_loc = QtWidgets.QComboBox(sel_Form)
        self.sel_loc.setGeometry(QtCore.QRect(150, 80, 201, 41))
        self.sel_loc.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: 15pt \"华文楷体\";\n"
"    \n"
"    color: #555555;\n"
"    background: transparent;\n"
"    \n"
"\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox::drop-down{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"}\n"
" \n"
"QComboBox::down-arrow {\n"
"    image: url(:/common/combobox_arrow);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on {\n"
"    image: url(:/common/combobox_arrow_up);\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 32px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.sel_loc.setObjectName("sel_loc")
        self.sel_loc.addItem("")
        self.sel_loc.addItem("")
        self.sel_loc.addItem("")
        self.label_4 = QtWidgets.QLabel(sel_Form)
        self.label_4.setGeometry(QtCore.QRect(180, 260, 31, 31))
        self.label_4.setStyleSheet("#label_4{\n"
"    font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(sel_Form)
        self.label_5.setGeometry(QtCore.QRect(260, 260, 21, 31))
        self.label_5.setStyleSheet("#label_5{\n"
"    font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(sel_Form)
        self.label_6.setGeometry(QtCore.QRect(330, 260, 21, 31))
        self.label_6.setStyleSheet("#label_6{\n"
"    font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.finish = QtWidgets.QPushButton(sel_Form)
        self.finish.setGeometry(QtCore.QRect(70, 320, 93, 28))
        self.finish.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"font-family:\'Microsoft YaHei\';\n"
"    color:black;\n"
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
        self.finish.setObjectName("finish")
        self.cancel = QtWidgets.QPushButton(sel_Form)
        self.cancel.setGeometry(QtCore.QRect(220, 320, 93, 28))
        self.cancel.setStyleSheet("QPushButton{\n"
"    /*灰色背景*/\n"
"    background:rgba(220,221,221,1);\n"
"    /*渐变白灰背景*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(238, 238, 238, 255));\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    border-radius:5px;\n"
"font-family:\'Microsoft YaHei\';\n"
"    color:black;\n"
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
        self.cancel.setObjectName("cancel")
        self.year = QtWidgets.QLineEdit(sel_Form)
        self.year.setGeometry(QtCore.QRect(110, 260, 61, 41))
        self.year.setStyleSheet("\n"
"QLineEdit{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"    font-size:20px;\n"
"    border-radius:5px;\n"
"}\n"
"/*焦点样式*/\n"
"QLineEdit:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.year.setObjectName("year")
        self.month = QtWidgets.QLineEdit(sel_Form)
        self.month.setGeometry(QtCore.QRect(210, 260, 41, 41))
        self.month.setStyleSheet("\n"
"QLineEdit{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"font-size:20px;\n"
"}\n"
"/*焦点样式*/\n"
"QLineEdit:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.month.setObjectName("month")
        self.day = QtWidgets.QLineEdit(sel_Form)
        self.day.setGeometry(QtCore.QRect(290, 260, 41, 41))
        self.day.setStyleSheet("\n"
"QLineEdit{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"font-size:20px;\n"
"}\n"
"/*焦点样式*/\n"
"QLineEdit:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.day.setObjectName("day")
        self.camID_2 = QtWidgets.QLineEdit(sel_Form)
        self.camID_2.setGeometry(QtCore.QRect(150, 140, 201, 41))
        self.camID_2.setStyleSheet("\n"
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
        self.camID_2.setObjectName("camID_2")
        self.camID_3 = QtWidgets.QLabel(sel_Form)
        self.camID_3.setGeometry(QtCore.QRect(20, 200, 121, 31))
        self.camID_3.setStyleSheet("#camID_3{\n"
"    font: 15pt \"华文楷体\";\n"
"    \n"
"    color:black;\n"
"}")
        self.camID_3.setObjectName("camID_3")
        self.camID_4 = QtWidgets.QLineEdit(sel_Form)
        self.camID_4.setGeometry(QtCore.QRect(150, 200, 201, 41))
        self.camID_4.setStyleSheet("\n"
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
        self.camID_4.setObjectName("camID_4")
        self.label = QtWidgets.QLabel(sel_Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 171, 51))
        self.label.setStyleSheet("#label{\n"
"    \n"
"    font: 25pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.label.setObjectName("label")

        self.retranslateUi(sel_Form)
        QtCore.QMetaObject.connectSlotsByName(sel_Form)

    def retranslateUi(self, sel_Form):
        _translate = QtCore.QCoreApplication.translate
        sel_Form.setWindowTitle(_translate("sel_Form", "Form"))
        self.camID.setText(_translate("sel_Form", "摄像头ID："))
        self.Date.setText(_translate("sel_Form", "日期："))
        self.location.setText(_translate("sel_Form", "地区："))
        self.sel_loc.setItemText(0, _translate("sel_Form", "地区A"))
        self.sel_loc.setItemText(1, _translate("sel_Form", "地区B"))
        self.sel_loc.setItemText(2, _translate("sel_Form", "地区C"))
        self.label_4.setText(_translate("sel_Form", "年"))
        self.label_5.setText(_translate("sel_Form", "月"))
        self.label_6.setText(_translate("sel_Form", "日"))
        self.finish.setText(_translate("sel_Form", "完成"))
        self.cancel.setText(_translate("sel_Form", "取消"))
        self.camID_3.setText(_translate("sel_Form", "具体位置："))
        self.label.setText(_translate("sel_Form", "条件查询"))
