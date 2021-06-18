# -*- coding: utf-8 -*-
import os
import sys
from concurrent.futures import ThreadPoolExecutor

from PyQt5.QtWidgets import *

import fun
from ui import Ui_Form

threadPool = ThreadPoolExecutor(max_workers=20)


def openPath(callback):
    # 选择图片
    path = QFileDialog.getExistingDirectory(None, "选择存储文件夹", os.getcwd())
    if path == "":
        return 0
    callback(path)


class MainWindow(QWidget, Ui_Form):
    service = None
    img = None
    working = False

    def __init__(self, service_):
        super(MainWindow, self).__init__()
        self.service = service_
        self.setupUi(self)

    def openFromPath(self):
        """
        选择来源路径
        """
        openPath(callback=lambda x: self.fromPath.setText(x))

    def openTargetPath(self):
        """
        选择输出路径
        """
        openPath(callback=lambda x: self.targetPath.setText(x))

    def outRuntimeInfo(self, data, refresh=True):
        """
        输出运行时
        :param data: 日志
        :param refresh: 追加或清空再输出
        """
        if refresh:
            self.runtimeInfor.setText(data)
        else:
            self.runtimeInfor.setText(self.runtimeInfor.toPlainText() + '\n' + data)
        self.runtimeInfor.moveCursor(self.runtimeInfor.textCursor().End)

    def getFromPath(self):
        """
        获取源路径
        :return: 源路径
        """
        return self.fromPath.toPlainText()

    def getTargetPath(self):
        """
        获取输出路径
        :return: 输出路径
        """
        return self.targetPath.toPlainText()

    def outSupportTypes(self, data):
        """
        输出模型支持的类型
        :param data: 类型串
        """
        self.modelType.setText(data)

    def outModelInfo(self, data):
        """
        输出模型信息
        :param data: 模型信息
        """
        self.modelInfor.setText(data)

    def getOnlyNumber(self):
        """
        单次处理图片数量
        :return: 数量
        """
        return self.onlyNumber.value()

    def getRecursionPathStatus(self):
        """
        是否递归目录
        """
        return self.recursionPath.checkState() == 2

    def startRun(self):
        """
        开始分类
        """
        if self.working:
            self.outRuntimeInfo('任务执行中', False)
            return
        try:
            threadPool.submit(service.startRun, self)
        except Exception as e:
            print(e)

    def setWorking(self, status):
        self.working = status


if __name__ == '__main__':
    service = fun.Service()
    app = QApplication(sys.argv)
    # 初始化窗口
    m = MainWindow(service)
    m.btu_selectFromPath.clicked.connect(m.openFromPath)
    m.btu_selectTargetPath.clicked.connect(m.openTargetPath)
    m.btu_startRun.clicked.connect(m.startRun)
    m.setWindowTitle('1920*1080壁纸分类')
    m.show()
    service.signalRunTime.connect(m.outRuntimeInfo)
    service.signalWorking.connect(m.setWorking)
    service.signalModelInfo.connect(m.outModelInfo)
    service.signalModelSupportTypes.connect(m.outSupportTypes)
    threadPool.submit(service.iniModel)
    sys.exit(app.exec_())
