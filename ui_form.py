# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(824, 665)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(2000, 2000))
        MainWindow.setBaseSize(QSize(1080, 1920))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 100, 801, 501))
        self.tabCoordsRobot = QWidget()
        self.tabCoordsRobot.setObjectName(u"tabCoordsRobot")
        self.gridLayoutWidget = QWidget(self.tabCoordsRobot)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 561, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.graphBig = PlotWidget(self.gridLayoutWidget)
        self.graphBig.setObjectName(u"graphBig")

        self.gridLayout.addWidget(self.graphBig, 0, 0, 1, 1)

        self.tabPointsToGo = QTableWidget(self.tabCoordsRobot)
        if (self.tabPointsToGo.columnCount() < 2):
            self.tabPointsToGo.setColumnCount(2)
        if (self.tabPointsToGo.rowCount() < 5):
            self.tabPointsToGo.setRowCount(5)
        self.tabPointsToGo.setObjectName(u"tabPointsToGo")
        self.tabPointsToGo.setGeometry(QRect(570, 10, 211, 231))
        self.tabPointsToGo.setFrameShape(QFrame.Shape.StyledPanel)
        self.tabPointsToGo.setShowGrid(True)
        self.tabPointsToGo.setWordWrap(True)
        self.tabPointsToGo.setCornerButtonEnabled(True)
        self.tabPointsToGo.setRowCount(5)
        self.tabPointsToGo.setColumnCount(2)
        self.tabPointsToGo.horizontalHeader().setVisible(True)
        self.tabPointsToGo.horizontalHeader().setCascadingSectionResizes(False)
        self.tabPointsToGo.horizontalHeader().setDefaultSectionSize(98)
        self.tabPointsToGo.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabPointsToGo.verticalHeader().setVisible(True)
        self.tabPointsToGo.verticalHeader().setCascadingSectionResizes(False)
        self.tabPointsToGo.verticalHeader().setDefaultSectionSize(40)
        self.tabPointsToGo.verticalHeader().setProperty(u"showSortIndicator", False)
        self.btnAddPoint = QPushButton(self.tabCoordsRobot)
        self.btnAddPoint.setObjectName(u"btnAddPoint")
        self.btnAddPoint.setGeometry(QRect(590, 250, 83, 29))
        self.btnClearTab = QPushButton(self.tabCoordsRobot)
        self.btnClearTab.setObjectName(u"btnClearTab")
        self.btnClearTab.setGeometry(QRect(680, 250, 83, 29))
        self.graphOrientation = PlotWidget(self.tabCoordsRobot)
        self.graphOrientation.setObjectName(u"graphOrientation")
        self.graphOrientation.setGeometry(QRect(590, 310, 171, 151))
        self.graphOrientation.setStyleSheet(u"")
        self.btnRun = QPushButton(self.tabCoordsRobot)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(630, 280, 83, 29))
        self.tabWidget.addTab(self.tabCoordsRobot, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayoutWidget_2 = QWidget(self.tab_6)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(-10, -10, 571, 481))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.graphNoth = PlotWidget(self.gridLayoutWidget_2)
        self.graphNoth.setObjectName(u"graphNoth")

        self.gridLayout_2.addWidget(self.graphNoth, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayoutWidget_3 = QWidget(self.tab_5)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(60, 40, 311, 244))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_4.addWidget(self.label_16)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sboxKp = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.sboxKp.setObjectName(u"sboxKp")
        self.sboxKp.setDecimals(4)
        self.sboxKp.setMaximum(1000000.000000000000000)
        self.sboxKp.setValue(80.000000000000000)

        self.verticalLayout_2.addWidget(self.sboxKp)

        self.sboxKi = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.sboxKi.setObjectName(u"sboxKi")
        self.sboxKi.setDecimals(4)

        self.verticalLayout_2.addWidget(self.sboxKi)

        self.sboxKd = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.sboxKd.setObjectName(u"sboxKd")
        self.sboxKd.setDecimals(4)
        self.sboxKd.setMaximum(100000.000000000000000)

        self.verticalLayout_2.addWidget(self.sboxKd)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.btnUploadControl = QPushButton(self.verticalLayoutWidget_3)
        self.btnUploadControl.setObjectName(u"btnUploadControl")

        self.verticalLayout_4.addWidget(self.btnUploadControl)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sbDistanceError = QSpinBox(self.verticalLayoutWidget_3)
        self.sbDistanceError.setObjectName(u"sbDistanceError")
        self.sbDistanceError.setMinimum(5)
        self.sbDistanceError.setValue(5)

        self.horizontalLayout_5.addWidget(self.sbDistanceError)

        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.btnSetDistanceError = QPushButton(self.verticalLayoutWidget_3)
        self.btnSetDistanceError.setObjectName(u"btnSetDistanceError")

        self.verticalLayout_4.addWidget(self.btnSetDistanceError)

        self.pbtnSendSerial = QPushButton(self.tab_5)
        self.pbtnSendSerial.setObjectName(u"pbtnSendSerial")
        self.pbtnSendSerial.setGeometry(QRect(690, 30, 101, 24))
        self.txtMsgToSend = QPlainTextEdit(self.tab_5)
        self.txtMsgToSend.setObjectName(u"txtMsgToSend")
        self.txtMsgToSend.setGeometry(QRect(400, 30, 271, 31))
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 801, 89))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pbtnConnect = QPushButton(self.gridLayoutWidget_3)
        self.pbtnConnect.setObjectName(u"pbtnConnect")
        self.pbtnConnect.setEnabled(False)
        self.pbtnConnect.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pbtnConnect)

        self.pbScanPorts = QPushButton(self.gridLayoutWidget_3)
        self.pbScanPorts.setObjectName(u"pbScanPorts")

        self.horizontalLayout_2.addWidget(self.pbScanPorts)

        self.btnCalibrate = QPushButton(self.gridLayoutWidget_3)
        self.btnCalibrate.setObjectName(u"btnCalibrate")
        self.btnCalibrate.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btnCalibrate)

        self.btnTestMotors = QPushButton(self.gridLayoutWidget_3)
        self.btnTestMotors.setObjectName(u"btnTestMotors")
        self.btnTestMotors.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btnTestMotors)

        self.btnTestControl = QPushButton(self.gridLayoutWidget_3)
        self.btnTestControl.setObjectName(u"btnTestControl")
        self.btnTestControl.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btnTestControl)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.cbSelectCom = QComboBox(self.gridLayoutWidget_3)
        self.cbSelectCom.setObjectName(u"cbSelectCom")

        self.horizontalLayout.addWidget(self.cbSelectCom)

        self.cbSelectBaudRate = QComboBox(self.gridLayoutWidget_3)
        self.cbSelectBaudRate.setObjectName(u"cbSelectBaudRate")

        self.horizontalLayout.addWidget(self.cbSelectBaudRate)

        self.x_pos_robot = QSpinBox(self.gridLayoutWidget_3)
        self.x_pos_robot.setObjectName(u"x_pos_robot")
        self.x_pos_robot.setMinimum(-100)
        self.x_pos_robot.setMaximum(100)

        self.horizontalLayout.addWidget(self.x_pos_robot)

        self.y_pos_robot = QSpinBox(self.gridLayoutWidget_3)
        self.y_pos_robot.setObjectName(u"y_pos_robot")
        self.y_pos_robot.setMinimum(-100)
        self.y_pos_robot.setMaximum(100)

        self.horizontalLayout.addWidget(self.y_pos_robot)

        self.btnGoToPos = QPushButton(self.gridLayoutWidget_3)
        self.btnGoToPos.setObjectName(u"btnGoToPos")
        self.btnGoToPos.setEnabled(False)

        self.horizontalLayout.addWidget(self.btnGoToPos)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.serialInput = QPlainTextEdit(self.gridLayoutWidget_3)
        self.serialInput.setObjectName(u"serialInput")
        self.serialInput.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.serialInput)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 824, 25))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnAddPoint.setText(QCoreApplication.translate("MainWindow", u"AddPoint", None))
        self.btnClearTab.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCoordsRobot), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Config Position", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kp", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ki", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Kd", None))
        self.btnUploadControl.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Distance error", None))
        self.btnSetDistanceError.setText(QCoreApplication.translate("MainWindow", u"Set Distance error", None))
        self.pbtnSendSerial.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Page", None))
        self.pbtnConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pbScanPorts.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btnCalibrate.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.btnTestMotors.setText(QCoreApplication.translate("MainWindow", u"Test motors", None))
        self.btnTestControl.setText(QCoreApplication.translate("MainWindow", u"Magnetometer", None))
        self.btnGoToPos.setText(QCoreApplication.translate("MainWindow", u"Go", None))
    # retranslateUi

