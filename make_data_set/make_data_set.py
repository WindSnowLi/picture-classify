import json
import os

import cv2
import numpy as np
from tqdm import tqdm


def imgTo192_108(img: np.array):
    """
    修改图片为192*108，不然模型过大，小显卡吃不消
    :param img:
    :return: 重设大小之后的图片
    """
    return cv2.resize(img, (192, 108))


def get_target_data(path, picSavePath, labelsSavePath, outJson):
    """
    生成目标集与标签
    :param outJson: 输出参数信息
    :param path: 图片所在路径
    :param picSavePath: 图片保存路径
    :param labelsSavePath: 标签保存路径
    """

    imgs = []
    labels = []
    table = []
    k = 0
    paths = os.listdir(path)
    paths.sort()
    for i in paths:
        if os.path.isdir(path + '/' + i):
            pbar = tqdm(total=100)
            temp_path = os.listdir(path + '/' + i)
            for j in temp_path:
                pbar.update(100.0 / len(temp_path))
                imgs.append(imgTo192_108(cv2.imread(path + '/' + i + '/' + j)))
                labels.append(k)
            table.append(i)
            pbar.close()
            k = k + 1
    np.save(picSavePath, np.array(imgs))
    np.save(labelsSavePath, np.array(labels))
    config = {'support': table}
    # 预测值对应的目录名
    with open(outJson, 'w', encoding='utf8') as fp:
        json.dump(config, fp)


# 生成训练集包、训练集标签包、测试集标签包，测试集直接是测试目录的壁纸
if __name__ == '__main__':
    # 生成训练集以及训练集标签
    get_target_data('../train_pic', '../train/train_pic', '../train/train_labels', '../train/train.json')
    # 生成测试集以及测试集标签
    get_target_data('../test_pic', '../test/test_pic', '../test/test_labels', '../test/test.json')
