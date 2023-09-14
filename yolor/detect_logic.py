import sys
import argparse
import shutil
import torch
import os
import random
import cv2
from datetime import datetime
from utils.plots import plot_one_box,plot_one_box2
from utils.datasets import LoadStreams, LoadImages
from utils.torch_utils import select_device, load_classifier, time_synchronized
from utils.datasets import letterbox
from models.models import *
from lib.share import shareInfo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.detect_ui import Ui_MainWindow # 导入detect_ui的界面
from add import win_addinfo    #导入添加信息界面
from win_log import win_logs   #导入日志信息界面
from info_mysql import MySql  #导入自定义数据库
class UI_Logic_Window(QtWidgets.QMainWindow):
    locations = {}
    start_t = None
    flag = False
    def __init__(self,parent = None):
        super(UI_Logic_Window,self).__init__(parent)
        self.timer_video = QtCore.QTimer()#创建定时器
        #检测主界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #初始化信号槽
        self.init_slots()
        #捕获视频
        self.cap = cv2.VideoCapture()
        #参数0表示默认为笔记本的内置第一个摄像头，如果需要读取已有的视频则参数改为视频所在路径路径
        #输出文件夹
        self.output_folder = './inference/'
        #判断暂停/开始
        self.num_stop = 1
        #默认模型文件为None
        self.openfile_name_model = None
        #获取自定义数据库类
        self.db = MySql()
        #计时器
        self.start_t = time.time()
    #self.model_init()
    def init_slots(self):
        #初始化模型
        self.ui.pushButton.clicked.connect(self.model_init)
        #打开图像进行检测
        self.ui.pushButton_4.clicked.connect(self.button_image_open)
        #打开视频进行检测
        self.ui.pushButton_5.clicked.connect(self.button_video_open_1)
        #定时器超时进行视频帧现
        self.timer_video.timeout.connect(self.show_video_frame) 
        #选择权重
        self.ui.action_3.triggered.connect(self.select_weights)
        #视频暂停
        self.ui.pushButton_6.clicked.connect(self.button_video_stop)
        #结束视频检测
        self.ui.pushButton_7.clicked.connect(self.finish_detect)
        #添加摄像头检测
        #self.ui.pushButton_5.clicked.connect(self.button_video_open_1)
        #更换视频
        self.ui.comboBox_2.currentIndexChanged.connect(self.change_video)
        #获得日志
        self.ui.action.triggered.connect(self.get_logs)
        #打开摄像头检测
        self.ui.pushButton_8.clicked.connect(self.button_camera_open)
        #退出
        self.ui.action_4.triggered.connect(self.exit_)
        #添加摄像头
        self.ui.action_2.triggered.connect(self.add_info)
        pass
    #添加cam_
    def add_info(self):
        shareInfo.addWin = win_addinfo()
        shareInfo.addWin.show()
        shareInfo.addWin.mySignal.connect(self.get_emit_info)
        pass
    #获得添加cam界面发送的信息
    def get_emit_info(self,returndata):
        self.ui.textBrowser_3.setText(returndata[2])
        self.locations[returndata[0]] = [returndata[1],returndata[2]]
        self.ui.comboBox_2.addItem(returndata[0])
        self.flag = True
        self.button_video_open(returndata[1])
        print(self.locations)
    #记录日志
    def record_log(self,text_log):
        print(self.locations)
        loc = self.ui.comboBox.currentText()
        camID = self.ui.comboBox_2.currentText()
        loc_pos = self.locations[camID][1]
        logs = text_log
        log_date = datetime.now().strftime('%Y-%m-%d')
        log_time =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()).split(' ')
        log_time = log_time[1]
        #设置记录时间间隔
        record_logs = [loc,camID,loc_pos,logs,log_date,log_time]
        print(record_logs)
        if(int(time.time())-int(self.start_t))%30==0:

            self.db.insert_record(record_logs)
    # 打开摄像头检测
    def button_camera_open(self):
        print("Open camera to detect")
        # 设置使用的摄像头序号，系统自带为0
        camera_num = 0
        # 打开摄像头
        self.cap = cv2.VideoCapture(camera_num)
        # 判断摄像头是否处于打开状态
        bool_open = self.cap.isOpened()
        if not bool_open:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开摄像头失败", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            fps, w, h, save_path = self.set_video_name_and_path()
            fps = 5 # 控制摄像头检测下的fps，Note：保存的视频，播放速度有点快，我只是粗暴的调整了FPS
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
            self.timer_video.start(30)
            self.close_button()
    def close_button(self):
        self.ui.pushButton_4.setDisabled(True)
        self.ui.pushButton_5.setDisabled(True)
        self.ui.pushButton_8.setDisabled(True)
    def open_button(self):
        self.ui.pushButton_4.setDisabled(False)
        self.ui.pushButton_5.setDisabled(False)
        self.ui.pushButton_8.setDisabled(False)
    #打开日志信息
    def get_logs(self):
        self.logs = win_logs()
        self.logs.show()
    #改变视频
    def change_video(self):
        currentText = self.ui.comboBox_2.currentText()
        print(self.locations[currentText])
        self.button_video_open(self.locations[currentText][0])
        self.ui.textBrowser_3.setText(self.locations[currentText][1])
    # 打开视频并检测
    def button_video_open_1(self):
        self.ui.pushButton_6.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)
        self.flag = False
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开视频", "dataset/video", "*.mp4;;*.avi;;All Files(*)")
        flag = self.cap.open(video_name)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            #-------------------------写入视频----------------------------------#
            fps, w, h, save_path = self.set_video_name_and_path()
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
            self.timer_video.start(20) # 以0ms为间隔，启动或重启定时器
            # 进行视频识别时，关闭其他按键点击功能
            self.close_button()
    #打开视频检测
    def button_video_open(self,video_name):
        self.ui.pushButton_6.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)
        flag = self.cap.open(video_name)
        print(flag)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            #-------------------------写入视频----------------------------------#
            fps, w, h, save_path = self.set_video_name_and_path()
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
            self.timer_video.start(30) # 以30ms为间隔，启动或重启定时器
            # 进行视频识别时，关闭其他按键点击功能
            self.close_button()
    # 结束视频检测
    def finish_detect(self):
        # self.timer_video.stop()
        self.cap.release()  # 释放video_capture资源
        self.vid_writer.release()  # 释放video_writer资源
        self.ui.label_4.clear() # 清空label画布
        # 启动其他检测按键功能
        self.ui.pushButton_4.setDisabled(False)
        self.ui.pushButton_5.setDisabled(False)
        self.ui.pushButton_8.setDisabled(False)

        self.ui.textBrowser_3.setText('')
        self.ui.textBrowser_4.setText('')
        # 结束检测时，查看暂停功能是否复位，将暂停功能恢复至初始状态
        # Note:点击暂停之后，num_stop为偶数状态
    # 暂停与继续检测
    def button_video_stop(self):
        self.timer_video.blockSignals(False)
        # 暂停检测
        # 若QTimer已经触发，且激活
        if self.timer_video.isActive() == True and self.num_stop%2 == 1:
            self.ui.pushButton_6.setText(u'继续检测') # 当前状态为暂停状态
            self.num_stop = self.num_stop + 1 # 调整标记信号为偶数
            self.timer_video.blockSignals(True)
        # 继续检测
        else:
            self.num_stop = self.num_stop + 1
            self.ui.pushButton_6.setText(u'暂停检测')
    #选择模型
    def select_weights(self):
        self.openfile_name_model,_ = QFileDialog.getOpenFileName(None,'选择weights文件','weights/')
        if not self.openfile_name_model:
            QtWidgets.QMessageBox.warning(self,u'Waring',u"选择模型失败",buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            print('加载weights文件地址为：' + str(self.openfile_name_model))
    # 定义视频帧显示操作
    def show_video_frame(self):
        name_list = []
        flag, img = self.cap.read()
        if img is not None:
            info_show = self.detect(name_list, img) # 检测结果写入到原始img上
            self.vid_writer.write(img) # 检测结果写入视频
            print(info_show)
            # 检测信息显示在界面
            try:
                self.ui.textBrowser_2.setText(info_show)
                text_log='一切正常，注意防范火灾'
                w_list = info_show.split(' ')
                if 'fire' in w_list:
                    text_log = "发生火灾,请快速联系消防员"
                    self.ui.textBrowser_4.setStyleSheet("#textBrowser_4{\n"
                    "    font-size: 25px;\n"
                    "    color:red;\n"
                    "    font-weight:bold;"
                    "}\n")
                elif 'smoke' in w_list:
                    text_log = "无火灾有烟雾,请快速核查" 
                    self.ui.textBrowser_4.setStyleSheet("#textBrowser_4{\n"
                    "    font-size: 25px;\n"
                    "    color:gold;\n"
                    "    font-weight:bold;"
                    "}\n")
                                                
                elif 'fire' not in w_list and 'smoke' not in w_list:
                    self.ui.textBrowser_4.setStyleSheet("#textBrowser_4{\n"
                    "    font-size: 25px;\n"
                    "    color:black;\n"
                    "    font-weight:bold;"
                    "}\n")
            except:
                print('error')
            if self.flag:
                self.ui.textBrowser_4.setText(text_log)
            #self.ui.textBrowser_4.setText()
                self.record_log(text_log)
            show = cv2.resize(img, (640, 480)) # 直接将原始img上的检测结果进行显示
            self.result = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                     QtGui.QImage.Format_RGB888)
            self.ui.label_4.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.ui.label_4.setScaledContents(True)  # 设置图像自适应界面大小
    # 打开视频并检测
    def button_video_open_1(self):
        self.ui.pushButton_6.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)
        self.flag = False
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开视频", "dataset/video", "*.mp4;;*.avi;;All Files(*)")
        flag = self.cap.open(video_name)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            #-------------------------写入视频----------------------------------#
            fps, w, h, save_path = self.set_video_name_and_path()
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

            self.timer_video.start(20) # 以30ms为间隔，启动或重启定时器
            # 进行视频识别时，关闭其他按键点击功能
    def set_video_name_and_path(self):
        # 获取当前系统时间，作为img和video的文件名
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # if vid_cap:  # video
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 视频检测结果存储位置
        save_path = self.output_folder + 'output/' + now + '.mp4'
        return fps, w, h, save_path
    #模型推理
    def detect(self,name_list,img):
        '''
        :param name_list: 文件列表名
        :param img: 待检测图片
        :return info_show:检测输出的文字信息
        '''
        showimg = img
        with torch.no_grad():
            #将图片转化为32像素
            img = letterbox(img, new_shape=640,auto_size = 128)[0]
            # 转化
            img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
            #将一个内存不连续存储的数组转换为内存连续存储的数组，使得运行速度更快
            img = np.ascontiguousarray(img)
            img = torch.from_numpy(img).to(self.device)
            #使用半精度或者浮点数
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            #归一化
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                #起到升维的作用，后续图像处理可以更好地进行批操作
                img = img.unsqueeze(0)
            # Inference
            pred = self.model(img, augment=self.opt.augment)[0]
            # Apply NMS
            #非最大值抑制
            pred = non_max_suppression(pred, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes, agnostic=self.opt.agnostic_nms)

            # Process detections
            info_show=''
            for i, det in enumerate(pred):  # detections per image
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], showimg.shape).round()

                    # Write results
                    for *xyxy, conf, cls in det:
                        label = '%s %.2f' % (self.names[int(cls)], conf)
                        name_list.append(self.names[int(cls)])
                        single_info=plot_one_box2(xyxy, showimg, label=label, color=self.colors[int(cls)], line_thickness=2)
                        #info_show+=single_info
                        info_show = info_show + single_info + "\n"
            return info_show
        pass
    def button_image_open(self):
        self.ui.pushButton_6.setDisabled(True)
        self.ui.pushButton_7.setDisabled(True)
        print('button image open')
        name_list =[]
        try:
            img_name,_ = QtWidgets.QFileDialog.getOpenFileName(self,"打开图片","dataset/images","*.jpg;;*.png;;All Files(*)")
        except OSError as reason:
            print('文件打开出错！核对路径是否正确'+str(reason))
        else:
            if not img_name:
                QtWidgets.QMessageBox.warning(self,u"Warning",u"打开图片失败",buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                img = cv2.imread(img_name)
                info_show =self.detect(name_list,img)
                print(info_show)
                self.result = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
                self.result = cv2.resize(self.result,(640,480),interpolation=cv2.INTER_AREA)
                self.QtImg = QtGui.QImage(self.result.data,self.result.shape[1],self.result.shape[0],QtGui.QImage.Format_RGB32)
                self.ui.label_4.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                self.ui.label_4.setScaledContents(True) # 设置图像自适应界面大小
                #获取当前系统实践，作为img文件名
                now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
                file_extension = img_name.split('.')[-1]
                new_filename = now+'.'+file_extension
                file_path = self.output_folder+'output/'+new_filename
                cv2.imwrite(file_path,img)
                #检测信息显示在界面
                self.ui.textBrowser_2.setText(info_show)
                #检测结果显示在页面
                self.result = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
                self.result = cv2.resize(self.result,(640,480),interpolation=cv2.INTER_AREA)
                self.QtImg = QtGui.QImage(self.result.data,self.result.shape[1],self.result.shape[0],QtGui.QImage.Format_RGB32)
                self.ui.label_4.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                self.ui.label_4.setScaledContents(True) # 设置图像自适应界面大小
    def model_init(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--weights', nargs='+', type=str,default=['weights/bestr.pt'], help='model.pt path(s)')
        parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
        parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
        parser.add_argument('--img-size', type=int, default=1280, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.1, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.1, help='IOU threshold for NMS')
        parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
        parser.add_argument('--view-img',action='store_true', help='display results')
        parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
        parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        parser.add_argument('--augment', action='store_true', help='augmented inference')
        parser.add_argument('--update', action='store_true', help='update all models')
        parser.add_argument('--cfg', type=str, default='cfg/yolor_p6.cfg', help='*.cfg path')
        parser.add_argument('--names', type=str, default='data/coco.names', help='*.cfg path')
        self.opt = parser.parse_args()
        print(self.opt)
        out, source, weights, view_img, save_txt, imgsz, cfg, names = \
        self.opt.output, self.opt.source, self.opt.weights, self.opt.view_img, self.opt.save_txt, self.opt.img_size, self.opt.cfg, self.opt.names
        self.webcam = source == '0' or source.startswith('rtsp') or source.startswith('http') or source.endswith('.txt')
        if self.openfile_name_model:
            weights = [self.openfile_name_model]
            print("using selected model")

        # Initialize
        self.device = select_device(self.opt.device)
        if os.path.exists(out):
            shutil.rmtree(out)  # delete output folder
        os.makedirs(out)  # make new output folder
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        self.model = Darknet(cfg, imgsz).cuda()
        self.model.load_state_dict(torch.load(weights[0], map_location=self.device)['model'])
        #model = attempt_load(weights, map_location=device)  # load FP32 model
        #imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
        self.model.to(self.device).eval()
        if self.half:
            self.model.half()  # to FP16

        # Second-stage classifier
        classify = False
        if classify:
            modelc = load_classifier(name='resnet101', n=2)  # initialize
            modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=self.device)['model'])  # load weights
            modelc.to(self.device).eval()
        # Get names and colors
        self.names = self.load_classes(names)
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        print("model initial done")
            # 设置提示框
        QtWidgets.QMessageBox.information(self, u"Notice", u"模型加载完成", buttons=QtWidgets.QMessageBox.Ok,
                                        defaultButton=QtWidgets.QMessageBox.Ok)
    def load_classes(self,path):
        # Loads *.names file at 'path'
        with open(path, 'r') as f:
            names = f.read().split('\n')
        return list(filter(None, names))  # filter removes empty strings (such as last line)
    def exit_(self):
        self.close()
        print("successful quit")
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    current_ui = UI_Logic_Window()
    current_ui.show()
    sys.exit(app.exec_())