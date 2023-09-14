from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from lib.share import shareInfo
from ui.add_cam import Ui_addinfo


class win_addinfo(QDialog):
    
    mySignal = pyqtSignal(list)
    def __init__(self,parent = None):
        super(win_addinfo,self).__init__(parent)
        self.ui_addinfo = Ui_addinfo()
        self.ui_addinfo.setupUi(self)
        self.init_solts()
    def init_solts(self):
        self.ui_addinfo.pushButton_2.clicked.connect(self.exit_)
        self.ui_addinfo.pushButton_3.clicked.connect(self.select_video)
        self.ui_addinfo.pushButton.clicked.connect(self.get_info)
        pass
    def select_video(self):
        shareInfo.video_name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"打开视频","dataset/video","*.mp4;;*.avi;;Akk Files(*)")
        self.ui_addinfo.textBrowser.setText(shareInfo.video_name)
        pass
    def get_info(self):
        camID = self.ui_addinfo.lineEdit.text().strip()
        location = self.ui_addinfo.lineEdit_3.text().strip()
        self.mySignal.emit([camID,shareInfo.video_name,location])
        self.close()
    def exit_(self):
        self.close()
        print("success quit")
    