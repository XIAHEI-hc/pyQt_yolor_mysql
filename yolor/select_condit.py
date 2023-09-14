import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from ui.select_ui import Ui_sel_Form



class win_select(QDialog):
    mySignal = pyqtSignal(list)
    def __init__(self,parent = None):
        super(win_select,self).__init__(parent)
        self.ui_sel = Ui_sel_Form()
        self.ui_sel.setupUi(self)
        self.init_slots()
    def init_slots(self):
        self.ui_sel.cancel.clicked.connect(self.exit_)
        self.ui_sel.finish.clicked.connect(self.get_info)

    def get_info(self):
        loc = self.ui_sel.sel_loc.currentText()
        camid = self.ui_sel.camID_2.text().strip()
        loc_pos = self.ui_sel.camID_4.text().strip()
        year = self.ui_sel.year.text().strip()
        month = self.ui_sel.month.text().strip()
        day = self.ui_sel.day.text().strip()
        if year=='' or month == ''or day=='':
            date_ = ''
        else:
            date_ = year+'-'+month+'-'+day
        
        # if re.findall("\d+", camid) == re.findall("\d+", loc_pos):
        #     print(True)
        # else:
        #     QtWidgets.QMessageBox.information(self, u"Notice", u"筛选条件错误！", buttons=QtWidgets.QMessageBox.Ok,
        #                                 defaultButton=QtWidgets.QMessageBox.Ok)

        lt = [loc,camid,loc_pos,date_]
        print(lt)
        self.mySignal.emit(lt)
        self.close()


    def exit_(self):
        self.close()
