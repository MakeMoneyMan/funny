import os
import cv2
import time
import numpy as np

def touch(x, y):
    os.system('adb.exe shell input tap '+str(x)+' '+str(y)+'')

def scrollScreen():
    os.system('adb.exe shell input swipe 600 800 600 200')

def screenCapture():
    os.system('adb.exe shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb.exe pull /sdcard/screenshot.png D:/')

def find_picture(target, template):
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( result >= 0.9)
    
    print('loc')
    print(len(loc[0]))
    print(loc)
    if len(loc[0]) > 0:
        return loc[1][0], loc[0][0]
    else:
        return False, False


    # print(loc[0][0])
    # #归一化处理
    # cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    # print('result2')
    # print(result)
    # #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print('min_val, max_val, min_loc, max_loc')
    # print("%.2f" % min_val)
    # print(min_val, max_val, min_loc, max_loc)
    # if min_val < 0.3:
    #     return False, False
    # #匹配值转换为字符串
    # #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    # strmin_val = str(min_val)
    # #绘制矩形边框，将匹配区域标注出来
    # #min_loc：矩形定点
    # #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    # # cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    # #显示结果,并将匹配值显示在标题栏上
    # # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # # cv2.waitKey()
    # # cv2.destroyAllWindows()
    # x=min_loc[0]
    # y=min_loc[1]
    # return x,y




while True:
    screenCapture()
    time.sleep(1)
    x, y = find_picture(cv2.imread('D:\screenshot.png'), cv2.imread('D:\like.png'))
    if x != False:
        time.sleep(1)
        touch(x +15, y + 15)
        time.sleep(1)
    scrollScreen()
    time.sleep(1)
