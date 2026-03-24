# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)
import asset.texture.mainphoto_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(1000, 600)
        mainwindow.setAutoFillBackground(False)
        mainwindow.setStyleSheet(u"#centralwidget {\n"
"	background-image:url(:/b);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        mainwindow.setTabShape(QTabWidget.TabShape.Triangular)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.photo = QFrame(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(10, 100, 670, 330))
        self.photo.setMouseTracking(False)
        self.photo.setStyleSheet(u"#photo {\n"
"    /* 1. \u8a2d\u5b9a\u80cc\u666f\u5716\u7247\u8def\u5f91 (\u958b\u982d\u4e00\u5b9a\u8981\u6709\u5192\u865f) */\n"
"   border-image: url(:/a);\n"
"\n"
"    /* 2. \u8a2d\u5b9a\u5716\u7247\u4e0d\u91cd\u8907 */\n"
"    background-repeat: no-repeat;\n"
"\n"
"    /* 3. \u8a2d\u5b9a\u5716\u7247\u7f6e\u4e2d */\n"
"    background-position: center;\n"
"\n"
"    /* 4. \u8a2d\u5b9a\u5713\u89d2 (\u9019\u5c31\u662f\u4f60\u8981\u7684\u73fe\u4ee3\u611f) */\n"
"    border-radius: 40px;\n"
"\n"
"    /* 5. \u9078\u64c7\u6027\uff1a\u52a0\u4e0a\u908a\u6846\u8b93\u5361\u7247\u66f4\u660e\u986f */\n"
"    border: 1px solid #2d2f45;\n"
"}")
        self.photo.setFrameShape(QFrame.Shape.StyledPanel)
        self.photo.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(710, 90, 271, 341))
        self.scrollArea.setStyleSheet(u"#scrollArea {\n"
"    background-color: transparent; /* \u5fb9\u5e95\u900f\u660e */\n"
"    border-radius: 40px; \n"
"    border: none; \n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: 	#000000;\n"
"    font-family: \"Microsoft JhengHei\";\n"
"}\n"
"\n"
"#background {\n"
"/* \u5f9e\u5de6\u4e0a\u5230\u53f3\u4e0b\u7684\u5fae\u5f31\u6f38\u5c64 */\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgba(255, 255, 255, 0.12), \n"
"        stop: 0.5 rgba(255, 255, 255, 0.05), \n"
"        stop: 1 rgba(255, 255, 255, 0.1)\n"
"    );\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"\n"
"}\n"
"\n"
"#background:hover {\n"
"	background-color: rgba(255, 255, 255, 0.15);\n"
"    border: 1px solid rgba(189, 147, 249, 0.5); /* \u79fb\u4e0a\u53bb\u6642\u908a\u6846\u8b8a\u7d2b\u8272\u5fae\u5149 */\n"
"}\n"
"\n"
"#annou {\n"
"	color: #ffffff;\n"
"	font-si"
                        "ze:20px;\n"
"}\n"
"\n"
"#date {\n"
"    color: #6272a4; \n"
"    font-size: 11px;\n"
"}\n"
"\n"
"#pushButton {\n"
"    color: #bd93f9;\n"
"    background: transparent;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"    color: #ff79c6;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 271, 341))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.background = QFrame(self.scrollAreaWidgetContents)
        self.background.setObjectName(u"background")
        self.background.setEnabled(True)
        self.background.setFrameShape(QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QFrame.Shadow.Raised)
        self.annou = QLabel(self.background)
        self.annou.setObjectName(u"annou")
        self.annou.setGeometry(QRect(20, 10, 81, 21))
        self.pushButton = QPushButton(self.background)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 290, 82, 26))
        self.frame = QFrame(self.background)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 211, 31))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.annou_2 = QLabel(self.frame)
        self.annou_2.setObjectName(u"annou_2")
        self.annou_2.setGeometry(QRect(10, 10, 91, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annou_2.sizePolicy().hasHeightForWidth())
        self.annou_2.setSizePolicy(sizePolicy)
        self.date = QLabel(self.frame)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(140, 10, 91, 20))

        self.horizontalLayout.addWidget(self.background)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(mainwindow)
        self.statusBar.setObjectName(u"statusBar")
        mainwindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"OctSrv Launcher", None))
        self.annou.setText(QCoreApplication.translate("mainwindow", u"\u6700\u65b0\u516c\u544a", None))
        self.pushButton.setText(QCoreApplication.translate("mainwindow", u"\u66f4\u591a-->", None))
        self.annou_2.setText(QCoreApplication.translate("mainwindow", u"annou", None))
        self.date.setText(QCoreApplication.translate("mainwindow", u"2026-3-15", None))
    # retranslateUi

