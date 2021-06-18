import json
import os

import cv2
import numpy as np
from tqdm import tqdm


def getListDir(path, recursion=False, target: list = None, imageCallback=None, dirCallback=None):
    """
    获取文件路径

    :param dirCallback: 发现目录回调
    :param imageCallback: 发现图片回调
    :param path: 根路径
    :param recursion: 是否递归获取
    :param target: 输出目标数组
    """
    if recursion:
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                if dirCallback is not None:
                    dirCallback(path + '/' + i)
                getListDir(path + '/' + i, recursion, target, imageCallback)
            else:
                temp = path + '/' + i
                if temp[-3:] != 'jpg' and temp[-3:] != 'png':
                    continue
                if imageCallback is not None:
                    imageCallback(path + '/' + i)
                target.append(path + '/' + i)
    else:
        for i in os.listdir(path):
            if not os.path.isdir(path + '/' + i):
                temp = path + '/' + i
                if temp[-3:] != 'jpg' and temp[-3:] != 'png':
                    continue
                if imageCallback is not None:
                    imageCallback(path + '/' + i)
                target.append(path + '/' + i)


def img_resize(image: np.array):
    """
    重设图片大小
    :param image: 图片np数组
    """
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = 192
    height_new = 108
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(
            image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(
            image, (int(width * height_new / height), height_new))
    return img_new


def get_data(paths: list, callback=None):
    """
    读取图片
    :param callback: 读取单个成功回调
    :param paths: 图片路径列表
    :return: 图片缩放100倍的多维数组
    """
    pic_list = []
    if len(paths) != 0:
        pbar = tqdm(total=100)
        for i in paths:
            pbar.update(100.0 / len(paths))
            # img = img_resize(cv2.imread('./train_pic/' + i + '/' + j, cv2.IMREAD_GRAYSCALE))
            img = img_resize(cv2.imread(i))
            if img.shape[0] != 108 or img.shape[1] != 192:
                continue
            if callback is not None:
                callback(i)
            pic_list.append(img)
        pbar.close()

    pic_images = np.array(pic_list)
    images = pic_images.reshape(
        pic_images.shape[0], 108, 192, 3) / 255.0
    return images
