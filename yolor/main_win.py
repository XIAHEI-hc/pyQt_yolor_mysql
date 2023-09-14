import sys
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.pyplot import show

from utils.id_process import get_id_info, sava_id_info # 账号信息工具函数

from lib.share import shareInfo # 公共变量名
import os

from ui.login_ui import Ui_Form
from ui.register_ui import Ui_Form2

from detect_logic import UI_Logic_Window
from PyQt5 import QtGui

import csv

os.chdir(os.getcwd())


#界面登录

class win_login(QMainWindow):
    def __init__(self,parent = None):
        super(win_login,self).__init__(parent)
        self.ui_login = Ui_Form()
        self.ui_login.setupUi(self)
        self.init_slots()
        self.hidden_pwd()
        pixmap = QtGui.QPixmap("ui_img/save.jpeg")  # 按指定路径找到图片
        self.ui_login.label_3.setPixmap (pixmap)  # 在label上显示图片
        self.ui_login.label_3.setScaledContents (True)  # 让图片自适应label大小
    #隐藏密码输入
    def hidden_pwd(self):
        self.ui_login.passward.setEchoMode(QLineEdit.Password)
    #绑定信号槽
    def init_slots(self):
        self.ui_login.login.clicked.connect(self.onSignIn)#点击登录
        self.ui_login.passward.returnPressed.connect(self.onSignIn)#回车登录
        self.ui_login.resiger.clicked.connect(self.create_id) 
    #跳转注册页面
    def create_id(self):
        shareInfo.createWin = win_Register()
        shareInfo.createWin.show()       
    #保存登录日志
    def save_login_log(self,username):
        with open('login_log.txt','a',encoding='utf-8') as f:
            f.write(username+'\t log in at'+datetime.now().strftimestrftime+'\r' )
    def onSignIn(self):

        print("you pressed sign in")
        username = self.ui_login.username.text().strip()
        password = self.ui_login.passward.text().strip()

        USER_PWD = get_id_info()
        if username not in USER_PWD.keys():
            replay = QMessageBox.warning(self,"登录失败！","账号或密码输入错误",QMessageBox.Yes)
        else:
            if USER_PWD.get(username) == password:
                print("jump to main win")
                #Ui_MainWindow
                shareInfo.mainWin = UI_Logic_Window()
                shareInfo.mainWin.show()
                self.close()
            else:
                replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)


class win_Register(QDialog):
    def __init__(self,parent = None):
        super(win_Register,self).__init__(parent)
        self.ui_register = Ui_Form2()
        self.ui_register.setupUi(self)
        self.init_slots()
    #绑定信号槽
    def init_slots(self):
        self.ui_register.reg_but.clicked.connect(self.new_account)
        self.ui_register.cancel.clicked.connect(self.cancel_)
    def cancel_(self):
        self.close()
    def new_account(self):
        print("cteate new account")
        USER_PWD = get_id_info()
        print(USER_PWD)
        new_username = self.ui_register.username_2.text().strip()
        new_password = self.ui_register.password_2.text().strip()
        if new_username == "":
            replay = QMessageBox.warning(self, "!", "账号不准为空", QMessageBox.Yes)
        else:
            if new_username in USER_PWD.keys():
                replay = QMessageBox.warning(self, "!", "账号已存在", QMessageBox.Yes)
        
            else:
                    # 注册成功
                print("succ")
                sava_id_info(new_username,new_password)
                replay = QMessageBox.warning(self,  "!", "注册成功！", QMessageBox.Yes)
                # 关闭界面
                self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 利用共享变量名来实例化对象
    shareInfo.loginWin = win_login() # 登录界面作为主界面
    shareInfo.loginWin.show()
    sys.exit(app.exec_())
