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
import mainphoto_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(1280, 720)
        mainwindow.setAutoFillBackground(False)
        mainwindow.setStyleSheet(u"#centralwidget {\n"
"	background-image:url(:/b);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u8b8a\u4eae */\n"
"QPushButton:hover {\n"
"   /* background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(255, 255, 255, 0.5);*/\n"
"/* 1. \u7a0d\u5fae\u6539\u8b8a\u5916\u908a\u8ddd\uff0c\u8b93\u5b83\u5f80\u4e0a\u63a8 */\n"
"    margin-top: 0px;\n"
"    margin-bottom: 4px; /* \u539f\u672c\u53ef\u80fd\u662f margin: 2px\uff0c\u9019\u88e1\u7e2e\u5c0f\u9802\u90e8\u589e\u5927\u5e95\u90e8 */\n"
"    \n"
"    /* 2. \u540c\u6642\u589e\u52a0\u80cc\u666f\u4eae\u5ea6 */\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    \n"
"    /* 3. \u5f37\u5316\u908a\u6846\uff0c\u6a21\u64ec\u908a\u7de3\u53cd\u5149 */\n"
"    border: 1px solid rgba(255, 255,"
                        " 255, 0.5);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593\u8b8a\u6697\uff0c\u6a21\u64ec\u7269\u7406\u56de\u994b */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.2);\n"
"}")
        mainwindow.setTabShape(QTabWidget.TabShape.Triangular)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.photo = QFrame(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(79, 110, 771, 401))
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
        self.scrollArea.setGeometry(QRect(900, 100, 321, 421))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 321, 421))
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
        self.pushButton.setGeometry(QRect(210, 370, 82, 26))
        self.frame = QFrame(self.background)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 261, 31))
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
        self.date.setGeometry(QRect(200, 10, 61, 20))

        self.horizontalLayout.addWidget(self.background)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(360, 620, 261, 71))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(360, 530, 261, 71))
        self.LauncherSetting = QPushButton(self.centralwidget)
        self.LauncherSetting.setObjectName(u"LauncherSetting")
        self.LauncherSetting.setGeometry(QRect(640, 620, 261, 71))
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(15)
        font.setBold(True)
        self.LauncherSetting.setFont(font)
        self.LauncherSetting.setMouseTracking(True)
        self.LauncherSetting.setStyleSheet(u"#LauncherSetting {\n"
"	background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.1); \n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"#LauncherSetting:hover {\n"
"    background-color: rgba(255, 255, 255, 0.25); \n"
"    border: 2px solid rgba(255, 255, 255, 0.6); \n"
"    padding: 9px;\n"
"}")
        self.ChangeSkin = QPushButton(self.centralwidget)
        self.ChangeSkin.setObjectName(u"ChangeSkin")
        self.ChangeSkin.setGeometry(QRect(640, 530, 261, 71))
        font1 = QFont()
        font1.setPointSize(15)
        self.ChangeSkin.setFont(font1)
        self.ChangeSkin.setMouseTracking(True)
        self.ChangeSkin.setStyleSheet(u"#ChangeSkin {\n"
"	background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.1); \n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"#ChangeSkin:hover {\n"
"    background-color: rgba(255, 255, 255, 0.25); \n"
"    border: 2px solid rgba(255, 255, 255, 0.6); \n"
"    padding: 9px;\n"
"}")
        self.LaunchGame = QPushButton(self.centralwidget)
        self.LaunchGame.setObjectName(u"LaunchGame")
        self.LaunchGame.setGeometry(QRect(920, 530, 291, 161))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4 Light"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.LaunchGame.setFont(font2)
        self.LaunchGame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.LaunchGame.setMouseTracking(True)
        self.LaunchGame.setStyleSheet(u"/* \u91dd\u5c0d\u516c\u544a\u6b04\u6216\u6309\u9215\u7684\u61f8\u505c\u72c0\u614b */\n"
"#LaunchGame {\n"
"background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.1); \n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"#LaunchGame:hover {\n"
"    background-color: rgba(255, 255, 255, 0.25); \n"
"    border: 2px solid rgba(255, 255, 255, 0.6); \n"
"    padding: 9px;\n"
"}")
        self.DCLink = QPushButton(self.centralwidget)
        self.DCLink.setObjectName(u"DCLink")
        self.DCLink.setGeometry(QRect(90, 620, 71, 71))
        self.DCLink.setStyleSheet(u"#DCLink {\n"
"	border-image:url(:/c);\n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 35px;\n"
"    color: white;\n"
"}")
        self.YTLink = QPushButton(self.centralwidget)
        self.YTLink.setObjectName(u"YTLink")
        self.YTLink.setGeometry(QRect(90, 530, 71, 71))
        self.YTLink.setStyleSheet(u"#YTLink {\n"
"	border-image:url(:/g);\n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 35px;\n"
"    color: white;\n"
"}")
        self.OfficialWebLink = QPushButton(self.centralwidget)
        self.OfficialWebLink.setObjectName(u"OfficialWebLink")
        self.OfficialWebLink.setGeometry(QRect(180, 530, 71, 71))
        self.OfficialWebLink.setStyleSheet(u"#OfficialWebLink {\n"
"	border-image:url(:/f);\n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 35px;\n"
"    color: white;\n"
"}")
        self.GitHubLink = QPushButton(self.centralwidget)
        self.GitHubLink.setObjectName(u"GitHubLink")
        self.GitHubLink.setGeometry(QRect(180, 620, 71, 71))
        self.GitHubLink.setStyleSheet(u"#GitHubLink {\n"
"	border-image:url(:/e);\n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 35px;\n"
"    color: white;\n"
"}")
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
        self.pushButton_4.setText(QCoreApplication.translate("mainwindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainwindow", u"PushButton", None))
        self.LauncherSetting.setText(QCoreApplication.translate("mainwindow", u"\u555f\u52d5\u5668\u8a2d\u5b9a          ", None))
        self.ChangeSkin.setText(QCoreApplication.translate("mainwindow", u"\u66f4\u63db\u76ae\u819a(Coming Soon)  ", None))
        self.LaunchGame.setText(QCoreApplication.translate("mainwindow", u"\u4f3a\u670d\u5668\u9078\u55ae     ", None))
        self.DCLink.setText("")
        self.YTLink.setText("")
        self.OfficialWebLink.setText("")
        self.GitHubLink.setText("")
    # retranslateUi

