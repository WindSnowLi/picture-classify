import json
import os

import cv2
import numpy
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tqdm import tqdm

from utils import img_resize


def init_network():
    """
    初始化神经网络，支持五种类型
    :return: 模型
    """

    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(filters=48, kernel_size=(3, 3), padding='same', activation='relu', strides=1,
                               input_shape=(108, 192, 3)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        # 抑制过拟合
        tf.keras.layers.Dropout(rate=0.6),
        tf.keras.layers.Conv2D(filters=24, kernel_size=(
            3, 3), padding='same', activation='relu', strides=1),
        # 2*2池化取最大值
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        # 抑制过拟合
        tf.keras.layers.Dropout(rate=0.6),
        # 维度拉伸成1维
        tf.keras.layers.Flatten(),
        # 第二层隐藏层,使用relu激活函数
        tf.keras.layers.Dense(256, activation='relu'),
        # 抑制过拟合
        tf.keras.layers.Dropout(rate=0.6),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(rate=0.5),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(rate=0.5),
        # 输出层
        tf.keras.layers.Dense(5, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model


def getTrainData():
    """
    获取训练集数据
    :return: train_images, train_labels, class_names
    """
    fp = open('./train/train.json', 'r', encoding='utf8')
    class_names = json.load(fp)['support']
    fp.close()

    # 返回加载来的数据集
    pic_train_images = numpy.load('./train/train_pic.npy')
    train_images = pic_train_images.reshape(
        pic_train_images.shape[0], 108, 192, 3) / 255.0
    print(train_images.shape)
    train_labels = numpy.load('./train/train_labels.npy')
    print(numpy.load('./train/train_labels.npy').shape)
    return train_images, train_labels, class_names


def getTestData():
    """
    获取测试集包的数据
    :return: train_images, train_labels, class_names
    """
    fp = open('./test/test.json', 'r', encoding='utf8')
    class_names = json.load(fp)['support']
    fp.close()

    # 返回加载来的数据集
    pic_test_images = numpy.load('./test/test_pic.npy')
    test_images = pic_test_images.reshape(pic_test_images.shape[0], 108, 192, 3) / 255.0
    print(test_images.shape)
    test_labels = numpy.load('./test/test_labels.npy')
    print(numpy.load('./test/test_labels.npy').shape)
    return test_images, test_labels, class_names


def getTestImages():
    """
    加载测试集1920*1080的壁纸
    """
    path = './test_pic'
    imgs = []
    labels = []
    k = 0
    paths = os.listdir(path)
    paths.sort()
    for j in paths:
        pbar = tqdm(total=100)
        for i in os.listdir(path + '/' + j):
            pbar.update(100.0 / len(os.listdir(path + '/' + j)))
            pic_path = path + '/' + j + '/' + i
            # img = img_resize(cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE))
            img = img_resize(cv2.imread(pic_path))
            if img.shape[0] != 108 or img.shape[1] != 192:
                os.remove(pic_path)
                continue
            imgs.append(img)
            labels.append(k)
        pbar.close()
        k = k + 1
    pic_test_images = np.array(imgs)
    test_images = pic_test_images.reshape(
        pic_test_images.shape[0], 108, 192, 3) / 255.0
    return test_images, np.array(labels)


def getModel(train_mode=False):
    """
    获取模型
    :param train_mode: 是否训练
    :return: 模型
    """
    # 如果训练
    if train_mode:
        # 初始化神经网络
        model = init_network()
        # 加载数据集
        train_images, train_labels, _ = getTrainData()
        test_images, test_labels, _ = getTestData()
        print(train_images.shape)
        print(train_labels.shape)
        print(test_images.shape)
        print(test_labels.shape)
        # 开始训练，训练二十次，显示日志信息
        model.fit(train_images, keras.utils.to_categorical(
            train_labels), batch_size=128, epochs=100, verbose=2)
        # 评估模型,不输出预测结果
        test_loss, test_acc = model.evaluate(
            test_images, keras.utils.to_categorical(test_labels), verbose=2)
        # 输出损失值
        print('测试集损失：', test_loss)
        # 输出正确率
        print('测试集正确率：', test_acc)
        # 保存模型
        model.save('.\\model\\expll.h5')
        return model, test_loss, test_acc
    else:
        # 加载模型
        model = tf.keras.models.load_model('.\\model\\780_3x3_1_3_100_expll.h5')
        # 打印模型信息
        model.summary()

        test_images, test_labels, _ = getTestData()
        # 评估模型,不输出预测结果
        test_loss, test_acc = model.evaluate(
            test_images, keras.utils.to_categorical(test_labels), verbose=2)
        # print([np.where(i == np.max(i))[0][0] for i in model.predict(test_images)])
        return model, test_loss, test_acc


# 训练模型
# if __name__ == '__main__':
#     model = getModel(True)
