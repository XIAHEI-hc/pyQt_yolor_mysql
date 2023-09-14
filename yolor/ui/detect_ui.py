# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detect_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("检测界面")
        MainWindow.setWindowIcon(QtGui.QIcon('ui_img/save1.ico'))
        MainWindow.resize(1131, 713)
        MainWindow.setStyleSheet("#label3{\n"
"    text-align:right;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    font-size:30px;\n"
"    font-weight:bold;\n"
"   }\n"
"#MainWindow{\n"
"    background-color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 741, 71))
        self.label.setStyleSheet("#label{\n"
"    text-align:right;\n"
"    font-family:;\n"
"    font: ;\n"
"    font: 36pt \"华文楷体\";\n"
"    font-size:40px;\n"
"    font-weight:bold;\n"
"    }")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 16px \"华文楷体\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:black;\n"
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
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 90, 1091, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 120, 121, 31))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 16px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    font-family:\'Microsoft YaHei\';\n"
"    color:black;\n"
"    font-size: 18;\n"
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
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 120, 91, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
"    color:black;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 111, 41))
        self.label_2.setStyleSheet("#label_2{\n"
"    \n"
"    font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 111, 41))
        self.label_3.setStyleSheet("#label_3{\n"
"        font: 15pt \"华文楷体\";\n"
"    color:black;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(380, 110, 20, 561))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(135, 300, 231, 41))
        self.textBrowser_3.setStyleSheet("\n"
"QTextBrowser{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"    font-size:20px;\n"
"    border-radius:5px;\n"
"}\n"
"/*焦点样式*/\n"
"\n"
"QTextBrowser:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(135, 350, 231, 81))
        self.textBrowser_4.setStyleSheet("#textBrowser_4{\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"    font-size:20px;\n"
"    border-radius:5px;\n"
"}\n"
"/*焦点样式*/\n"
"\n"
"QTextBrowser:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 440, 341, 221))
        self.groupBox.setStyleSheet("#grouptBox{\n"
"      text-align:right;\n"
"    \n"
"    font: 15pt \"华文楷体\";\n"
"    \n"
"    font-weight:bold;\n"
"    color: black;\n"
"\n"
"}")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 321, 191))
        self.textBrowser_2.setStyleSheet("\n"
"QTextBrowser{\n"
"    background:rgba(253,253,253,1);\n"
"    border:1px solid rgba(0, 0, 0, 0.23);\n"
"    /*圆角5个像素*/\n"
"    border-radius:5px;\n"
"    font-size:12px;\n"
"    border-radius:5px;\n"
"}\n"
"/*焦点样式*/\n"
"\n"
"QTextBrowser:focus\n"
"{\n"
"    border:1px solid rgb(44,169,225);\n"
"}\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 170, 81, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 220, 341, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 20, 91, 31))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 20, 91, 31))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 110, 701, 541))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 170, 91, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 170, 91, 31))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.actionmodel_1 = QtWidgets.QAction(MainWindow)
        self.actionmodel_1.setObjectName("actionmodel_1")
        self.actionmodel_2 = QtWidgets.QAction(MainWindow)
        self.actionmodel_2.setObjectName("actionmodel_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_2.addAction(self.action_2)
        self.menu_3.addAction(self.action_3)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu_4.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "烟雾火焰检测"))
        self.comboBox.setItemText(0, _translate("MainWindow", "区域A"))
        self.pushButton.setText(_translate("MainWindow", "初始化模型"))
        self.label_2.setText(_translate("MainWindow", "具体位置："))
        self.label_3.setText(_translate("MainWindow", "检测结果："))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "检测信息"))
        self.pushButton_4.setText(_translate("MainWindow", "图片检测"))
        self.groupBox_2.setTitle(_translate("MainWindow", "视频控制"))
        self.pushButton_6.setText(_translate("MainWindow", "暂停"))
        self.pushButton_7.setText(_translate("MainWindow", "结束"))
        self.pushButton_5.setText(_translate("MainWindow", "视频检测"))
        self.pushButton_8.setText(_translate("MainWindow", "打开摄像头"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "添加"))
        self.menu_3.setTitle(_translate("MainWindow", "设置"))
        self.menu_4.setTitle(_translate("MainWindow", "日志"))
        self.action_2.setText(_translate("MainWindow", "摄像头"))
        self.action_4.setText(_translate("MainWindow", "退出"))
        self.actionmodel_1.setText(_translate("MainWindow", "model_1"))
        self.actionmodel_2.setText(_translate("MainWindow", "model_2"))
        self.action_3.setText(_translate("MainWindow", "选择模型"))
        self.action.setText(_translate("MainWindow", "查看"))
