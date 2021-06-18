# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\colorUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 950)
        Form.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  padding: 15px 25px;\n"
"  cursor: pointer;\n"
"  text-align: center;   \n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"}\n"
"QPushButton:hover {background-color: #3e8e41}\n"
"\n"
"QPushButton:active {\n"
"  background-color: #3e8e41;\n"
"  box-shadow: 0 5px #666;\n"
"  transform: translateY(4px);\n"
"}\n"
"\n"
"\n"
"QTextEdit{\n"
"width: 100%;\n"
"  padding: 8px 10px;\n"
"  margin: 4px 0;\n"
"  display: inline-block;\n"
"  border: 1px solid #ccc;\n"
"  border-radius: 4px;\n"
"  box-sizing: border-box;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 18px;\n"
"    color: #BDC8E2;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: aqua;\n"
"    border-radius: 20px;\n"
"\n"
"    padding-left: 20px;\n"
"    padding-top: 0px;\n"
"\n"
"    background-color: #2E3648;\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"}\n"
"/*\n"
"QLabel:hover{\n"
"    color: red;\n"
"    border-color: green;\n"
"    background-color: aqua;\n"
"}\n"
"QLabel:disabled{\n"
"    color: blue;\n"
"    border-color: brown;\n"
"    background-color: aqua;\n"
"}\n"
"*/\n"
"")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 781, 951))
        self.label_8.setStyleSheet("QLabel:hover{\n"
"}\n"
"QLabel:disabled{\n"
"}\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 749, 917))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.modelInfor = QtWidgets.QTextEdit(self.layoutWidget)
        self.modelInfor.setMaximumSize(QtCore.QSize(16777215, 150))
        self.modelInfor.setStyleSheet("")
        self.modelInfor.setReadOnly(True)
        self.modelInfor.setObjectName("modelInfor")
        self.horizontalLayout.addWidget(self.modelInfor)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.modelType = QtWidgets.QTextEdit(self.layoutWidget)
        self.modelType.setMaximumSize(QtCore.QSize(16777215, 150))
        self.modelType.setStyleSheet("")
        self.modelType.setReadOnly(True)
        self.modelType.setObjectName("modelType")
        self.horizontalLayout_2.addWidget(self.modelType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.onlyNumber = QtWidgets.QSpinBox(self.layoutWidget)
        self.onlyNumber.setProperty("value", 10)
        self.onlyNumber.setObjectName("onlyNumber")
        self.horizontalLayout_3.addWidget(self.onlyNumber)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.recursionPath = QtWidgets.QCheckBox(self.layoutWidget)
        self.recursionPath.setStyleSheet("QCheckBox{\n"
"    color:white;\n"
"}")
        self.recursionPath.setObjectName("recursionPath")
        self.horizontalLayout_4.addWidget(self.recursionPath)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.fromPath = QtWidgets.QTextEdit(self.layoutWidget)
        self.fromPath.setMaximumSize(QtCore.QSize(16777215, 150))
        self.fromPath.setStyleSheet("")
        self.fromPath.setReadOnly(True)
        self.fromPath.setObjectName("fromPath")
        self.horizontalLayout_5.addWidget(self.fromPath)
        self.btu_selectFromPath = QtWidgets.QPushButton(self.layoutWidget)
        self.btu_selectFromPath.setStyleSheet("")
        self.btu_selectFromPath.setObjectName("btu_selectFromPath")
        self.horizontalLayout_5.addWidget(self.btu_selectFromPath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.targetPath = QtWidgets.QTextEdit(self.layoutWidget)
        self.targetPath.setMaximumSize(QtCore.QSize(16777215, 150))
        self.targetPath.setStyleSheet("")
        self.targetPath.setReadOnly(True)
        self.targetPath.setObjectName("targetPath")
        self.horizontalLayout_6.addWidget(self.targetPath)
        self.btu_selectTargetPath = QtWidgets.QPushButton(self.layoutWidget)
        self.btu_selectTargetPath.setStyleSheet("")
        self.btu_selectTargetPath.setObjectName("btu_selectTargetPath")
        self.horizontalLayout_6.addWidget(self.btu_selectTargetPath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.runtimeInfor = QtWidgets.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.runtimeInfor.setFont(font)
        self.runtimeInfor.setStyleSheet("")
        self.runtimeInfor.setObjectName("runtimeInfor")
        self.verticalLayout.addWidget(self.runtimeInfor)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.btu_startRun = QtWidgets.QPushButton(self.layoutWidget)
        self.btu_startRun.setMinimumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btu_startRun.setFont(font)
        self.btu_startRun.setStyleSheet("")
        self.btu_startRun.setAutoDefault(False)
        self.btu_startRun.setDefault(False)
        self.btu_startRun.setObjectName("btu_startRun")
        self.horizontalLayout_8.addWidget(self.btu_startRun)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "1920*1080壁纸分类"))
        self.label.setText(_translate("Form", "模型信息："))
        self.label_2.setText(_translate("Form", "支持种类："))
        self.label_3.setText(_translate("Form", "单次分类数量："))
        self.label_5.setText(_translate("Form", "目录所有层级："))
        self.recursionPath.setText(_translate("Form", "递归目录"))
        self.label_6.setText(_translate("Form", "数据源路径："))
        self.btu_selectFromPath.setText(_translate("Form", "选择"))
        self.label_7.setText(_translate("Form", " 目标路径："))
        self.btu_selectTargetPath.setText(_translate("Form", "选择"))
        self.label_4.setText(_translate("Form", "运行时信息："))
        self.btu_startRun.setText(_translate("Form", "开始分类"))