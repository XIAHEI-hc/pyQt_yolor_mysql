from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.logs import Ui_log

from info_mysql import MySql
from select_condit import win_select

class win_logs(QDialog):
    def __init__(self,parent = None):
        super(win_logs,self).__init__(parent)
        self.ui_logs = Ui_log()
        self.ui_logs.setupUi(self)
        self.db = MySql()
        self.init_slots()
        
    def init_slots(self):

        self.ui_logs.return_bt.clicked.connect(self.quit_)
        self.ui_logs.sel_all.clicked.connect(self.select_all)
        self.ui_logs.clear_bt.clicked.connect(self.clear_all)

        self.ui_logs.condit.clicked.connect(self.win_condit)
    def win_condit(self):
        self.win_con = win_select()
        self.win_con.show()
        self.win_con.mySignal.connect(self.get_sel_info)
    def get_sel_info(self,lt):
        self.clear_all()
        data = self.db.search_record(lt)
        print(data)
        self.ui_logs.sel_all.setDisabled(False)
        self.ui_logs.clear_bt.setDisabled(False)
        self.ui_logs.condit.setDisabled(False)
        self.show_all(data)
        
        pass
    def select_all(self):
        self.clear_all()
        data = self.db.select_all()
        self.ui_logs.sel_all.setDisabled(True)
        self.ui_logs.clear_bt.setDisabled(False)
        self.show_all(data)
    def show_all(self,data):
        
        try:
            for item in data:
                self.show_one(item)
        except:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"查询结果为空", buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)

    def clear_all(self):
        self.ui_logs.tableWidget.clearContents()
        row_cnt = self.ui_logs.tableWidget.rowCount()
        for i in range(row_cnt):
            self.ui_logs.tableWidget.removeRow(0)

        self.ui_logs.sel_all.setDisabled(False)
        self.ui_logs.clear_bt.setDisabled(True)
        self.ui_logs.condit.setDisabled(False)
        print("clear all")

    def show_one(self,item):
        
        row_cnt = self.ui_logs.tableWidget.rowCount()
        #print(row_cnt)
        self.ui_logs.tableWidget.insertRow(row_cnt)       # 尾部插入一行新行表格
        column_cnt = self.ui_logs.tableWidget.columnCount()   # 返回当前列数
        
        #for item in data:
        for col in range(len(list(item))):
            item1 = QTableWidgetItem(str(item[col]))
            self.ui_logs.tableWidget.setItem(row_cnt, col, item1) #最后，将(行，列，内容)配置
            
        #self.ui_logs.tableWidget.resizeColumnsToContents()  # 设置列宽高按照内容自适应   
        #self.ui_logs.tableWidget.setTextAlignment(Qt.AlignHCenter | QtCore.AlignVCenter)
    
    def quit_(self):
        self.close()
