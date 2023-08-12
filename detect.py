import argparse

import torch.backends.cudnn as cudnn
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import numpy as np


from models.experimental import *
from utils.datasets import *
from utils.utils import *


def img_similarity(img1_path, img2_path):
    """
    # 自定义计算两个图片相似度函数
    :param img1_path: 图片1路径
    :param img2_path: 图片2路径
    :return: 图片相似度
    """
    img1 = img1_path
    img2 = img2_path
    w1= img1.shape[0]
    h1 = img1.shape[1]
    w2=img2.shape[0]
    h2 = img2.shape[1]
    img1 = cv2.resize(img1, (h1, w1))
    img2 = cv2.resize(img2, (h2, w2))
    # 初始化ORB检测器
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    # 提取并计算特征点
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    # knn筛选结果
    matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)
    # 查看最大匹配点数目
    good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
    similary = float(len(good)) / len(matches)
    if similary > 0.1:
        print("判断为ture,两张图片相似度为:%s" % similary)
    else:
        print("判断为false,两张图片相似度为:%s" % similary)
    return similary


def detect(save_img=False):
    out, source, weights, view_img, save_txt, imgsz = \
        opt.output, opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
    webcam = source == '0' or source.startswith('rtsp') or source.startswith('http') or source.endswith('.txt')




    # Initialize
    device = torch_utils.select_device(opt.device)
    if os.path.exists(out):
        shutil.rmtree(out)  # delete output folder
    os.makedirs(out)  # make new output folder
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = torch_utils.load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])  # load weights
        modelc.to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if webcam:
        view_img = True
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz)
    else:
        save_img = True
        dataset = LoadImages(source, img_size=imgsz)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

    # Run inference
    t0 = time.time()
    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
    _ = model(img.half() if half else img) if device.type != 'cpu' else None  # run once
    for path, img, im0s, vid_cap in dataset:
        #######################################################################处理反转
        showimg=img.transpose(1,2,0)
        #cv2.imshow("showing", showimg)
        up_cut=[0,1]
        for i in range(60,120):
            img_coner_up = showimg[0:i, 0:640]
            img_coner_up = cv2.flip(img_coner_up, 0)
            #print(img_coner_up.shape)
            img_coner_up_original=showimg[i:i*2,0:640]
            #print(ssim(img_coner_up, img_coner_up_original, multichannel=True))
            similar=ssim(img_coner_up, img_coner_up_original, multichannel=True)
            if similar>up_cut[0]:
                up_cut[0] = similar
                up_cut[1] = i

        if up_cut[0]>=0.86:
            img_coner_up = showimg[0:up_cut[1], 0:640]
            img_coner_up = cv2.flip(img_coner_up, 0)
            img_coner_up_original = showimg[up_cut[1]:up_cut[1] * 2, 0:640]

            showimg[0:up_cut[1], 0:640]=0
            #cv2.imshow("sad",img_coner_up)
            #cv2.imshow("sad1", showimg)
            #cv2.imshow("sad2", img_coner_up_original)
            #cv2.waitKey(0)
        else:
            print("图片上方没有相似度")
            #cv2.imshow("showing3", showimg)
        ##########################################################################


        #######################################################################处理反转
        down_cut=[0,1]
        for i in range(60,120):
            img_coner_up = showimg[640-i:640, 0:640]
            img_coner_up = cv2.flip(img_coner_up, 0)
            #print(img_coner_up.shape)
            img_coner_up_original=showimg[640-2*i:640-i,0:640]

            similar=ssim(img_coner_up, img_coner_up_original, multichannel=True)
            if similar>down_cut[0]:
                down_cut[0] = similar
                down_cut[1] = i

        if down_cut[0]>=0.86:
            img_coner_up = showimg[640-down_cut[1]:640, 0:640]

            showimg[640-down_cut[1]:640, 0:640]=0
        else:
            print("图片上方没有相似度")
            #cv2.imshow("showing2", showimg)
        ##########################################################################




        #######################################################################处理反转
        right_cut=[0,1]
        for i in range(60,220):
            img_coner_up = showimg[0:640, 640-i:640]
            img_coner_up = cv2.flip(img_coner_up, 1)
            #print(img_coner_up.shape)
            img_coner_up_original=showimg[0:640,640-2*i:640-i]
            #print(img_coner_up_original.shape)
            #print(ssim(img_coner_up, img_coner_up_original, multichannel=True))
            similar=ssim(img_coner_up, img_coner_up_original, multichannel=True)
            if similar>right_cut[0]:
                right_cut[0] = similar
                right_cut[1] = i
        print("相似度最大是" + str(right_cut[0]))
        if right_cut[0]>=0.86:
            img_coner_up = showimg[0:640,640-right_cut[1]:640]
            img_coner_up = cv2.flip(img_coner_up, 1)
            img_coner_up_original = showimg[0:640,640-right_cut[1] * 2:640]

            showimg[0:640,640-right_cut[1]:640]=0


        else:
            print("图片上方没有相似度")

        ##########################################################################

        lift_cut = [0, 1]
        for i in range(60, 220):
            img_coner_up = showimg[0:640,0:i]
            img_coner_up = cv2.flip(img_coner_up, 1)
            # print(img_coner_up.shape)
            img_coner_up_original = showimg[0:640,i:i * 2]
            #print(ssim(img_coner_up, img_coner_up_original, multichannel=True))
            similar = ssim(img_coner_up, img_coner_up_original, multichannel=True)
            if similar > lift_cut[0]:
                lift_cut[0] = similar
                lift_cut[1] = i
        print("相似度最大是"+str(lift_cut[0]))
        if lift_cut[0] >= 0.88:
            img_coner_up = showimg[0:640,0:lift_cut[1]]


            showimg[0:640,0:lift_cut[1]] = 0

        else:
            print("图片上方没有相似度")

        ##########################################################################

        #cv2.imshow("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", showimg)
        #cv2.waitKey(0)

        img=showimg.transpose(2, 0, 1)
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = torch_utils.time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t2 = torch_utils.time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
            else:
                p, s, im0 = path, '', im0s

            save_path = str(Path(out) / Path(p).name)
            txt_path = str(Path(out) / Path(p).stem) + ('_%g' % dataset.frame if dataset.mode == 'video' else '')
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if det is not None and len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += '%g %ss, ' % (n, names[int(c)])  # add to string
                Pwidth=416
                Pheight=415
                dic = {
                    '0': "person",  # 创建字典用来对类型进行转换
                    '1': "head",  # 此处的字典要与自己的classes.txt文件中的类对应，且顺序要一致
                    '2': "helmet",
                }

                # Write results
                for *xyxy, conf, cls in det:
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        with open(txt_path + '.txt', 'a') as f:
                            xmin=int(((float(xywh[0])) * Pwidth + 1) - (float(xywh[2])) * 0.5 * Pwidth)
                            ymin=int(((float(xywh[1])) * Pheight + 1) - (float(xywh[3])) * 0.5 * Pheight)
                            xmax=int(((float(xywh[0])) * Pwidth + 1) + (float(xywh[2])) * 0.5 * Pwidth)
                            ymax=int(((float(xywh[1])) * Pheight + 1) + (float(xywh[3])) * 0.5 * Pheight)
                            print("*****************************************************************************")
                            class_index=str(int([cls.cpu().numpy()][0].tolist()))
                            print(str(dic[class_index]))

                            f.write((str(dic[class_index])+ ' ' +'%.2f'+ ' ' +'%g ' * 4 + '\n') % (conf,xmin-1,ymin-1,xmax-2,ymax+1))  # label format

                    if save_img or view_img:  # Add bbox to image
                        label = '%s %.2f' % (names[int(cls)], conf)
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)

            # Print time (inference + NMS)
            print('%sDone. (%.3fs)' % (s, t2 - t1))

            # Stream results
            if view_img:
                cv2.imshow(p, im0)
                if cv2.waitKey(1) == ord('q'):  # q to quit
                    raise StopIteration

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'images':
                    cv2.imwrite(save_path, im0)
                else:
                    if vid_path != save_path:  # new video
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release()  # release previous video writer

                        fourcc = 'mp4v'  # output video codec
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
                    vid_writer.write(im0)

    if save_txt or save_img:
        print('Results saved to %s' % os.getcwd() + os.sep + out)
        if platform == 'darwin' and not opt.update:  # MacOS
            os.system('open ' + save_path)

    print('Done. (%.3fs)' % (time.time() - t0))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='./weights/helmet_head_person_l.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default=f'test_images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.4, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    opt = parser.parse_args()
    print(opt)

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt', 'yolov3-spp.pt']:
                detect()
                create_pretrained(opt.weights, opt.weights)
        else:
            detect()
