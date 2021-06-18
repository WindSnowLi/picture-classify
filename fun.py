import json
import os
import shutil

import numpy as np
from PyQt5.QtCore import *

import utils
from model import getModel


def getModelSupportTypes(data):
    """
    获取模型支持的分类
    :return:
    """
    temp = ''
    for i in data:
        temp = temp + ' ' + i
    return temp


def getModelInfo(loss, acc):
    """
    获取模型信息
    :return: 模型测试准确度
    """
    return '测试集损失：{:.3f}\n测试集准确率：{:.3f}%'.format(loss, acc * 100)


class Service(QObject):
    signalRunTime = pyqtSignal(str, bool)
    model = None
    signalWorking = pyqtSignal(bool)
    loadModelStatus = False
    signalModelInfo = pyqtSignal(str)
    signalModelSupportTypes = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def predict(self, imgs: np.array):
        """
        预测
        :param imgs: 预测图片集
        :return: 预测结果
        """
        rs = self.model.predict(imgs)
        return [np.where(i == np.max(i))[0][0] for i in rs]

    def iniModel(self):
        """
        初始化加载模型
        """
        if self.loadModelStatus:
            self.signalRunTime.emit('模型加载中···', False)
            return
        self.loadModelStatus = True
        self.signalRunTime.emit('正在加载模型···', False)
        self.model, loss, acc = getModel()
        with open('model/model.json', 'r', encoding='utf8') as fp:
            info = json.load(fp)
            self.signalModelInfo.emit('方法：' + info['way'] + '\n' + getModelInfo(loss, acc))
            self.signalModelSupportTypes.emit(getModelSupportTypes(info['support']))
        self.signalRunTime.emit('模型加载完成', False)
        self.loadModelStatus = False

    def startRun(self, window):
        """
        开始进行分类
        :param window: 窗口对象
        """
        if len(window.getFromPath()) == 0 or len(window.getTargetPath()) == 0:
            self.signalRunTime.emit('\n存在路径为空\n', False)
            self.signalWorking.emit(False)
            return
        list_path = []
        self.signalRunTime.emit('\n检索中······\n', False)
        utils.getListDir(window.fromPath.toPlainText(), window.getRecursionPathStatus(), list_path, imageCallback=None,
                         dirCallback=lambda x: self.signalRunTime.emit('检索检索到目录: {0}\n'.format(x), False))
        self.signalRunTime.emit('检索完成，共计{0}张图片\n'.format(len(list_path)), False)
        if len(list_path) == 0:
            self.signalWorking.emit(False)
            return
        self.signalRunTime.emit('开始读取图片······', False)
        img = utils.get_data(list_path, lambda x: self.signalRunTime.emit('已加载: {0}\n'.format(x), False))
        self.signalRunTime.emit('读取图片完成', False)
        self.signalRunTime.emit('维度信息:{0}'.format(img.shape), False)
        self.signalRunTime.emit('进行分类识别中······', False)
        rs = self.predict(img)
        self.signalRunTime.emit('分类识别完成\n***********\n识别结果:\n***********\n***********\n***********\n', False)

        with open('.\\model\\model.json', encoding='utf8') as fp:
            supportTypes = json.load(fp)['support']
            outRunInfo = '\n'
            for i in zip(list_path, rs):
                outRunInfo = outRunInfo + '路径： {0}； 结果：{1}\n\n'.format(i[0], supportTypes[i[1]])
            self.signalRunTime.emit(outRunInfo + '\n\n***********\n***********\n识别结果输出结束\n***********\n***********\n',
                                    False)
            targetPathRoot = window.getTargetPath()
            for i in supportTypes:
                if not os.path.exists(targetPathRoot + '/' + i):
                    os.mkdir(targetPathRoot + '/' + i)
        self.signalRunTime.emit('\n\n开始进行分类迁移······', False)

        onlyMoveMax = window.getOnlyNumber()
        with open('.\\model\\model.json', encoding='utf8') as fp:
            supportTypes = json.load(fp)['support']
            for j in range(0, int(len(list_path) * 1.0 / onlyMoveMax + 1)):
                for i in list(zip(list_path, rs))[onlyMoveMax * j:onlyMoveMax * (j + 1)]:
                    try:
                        self.signalRunTime.emit(
                            '来源： {0}； 迁移至：{1}\n\n'.format(i[0], (targetPathRoot + '/' + supportTypes[i[1]])), False)
                        shutil.move(i[0], targetPathRoot + '/' + supportTypes[i[1]])
                    except Exception as e:
                        self.signalRunTime.emit(
                            'ERROR: {0}'.format(e, False))
        self.signalRunTime.emit('\n\n迁移结束，任务完成\n\n', False)
        self.signalWorking.emit(False)
