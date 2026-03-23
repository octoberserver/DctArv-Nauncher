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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QScrollArea,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)
import mainphoto_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(1000, 600)
        mainwindow.setTabShape(QTabWidget.TabShape.Triangular)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.photo = QFrame(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(10, 100, 670, 330))
        self.photo.setMouseTracking(False)
        self.photo.setStyleSheet(u"#photo {\n"
"    /* 1. \u8a2d\u5b9a\u80cc\u666f\u5716\u7247\u8def\u5f91 (\u958b\u982d\u4e00\u5b9a\u8981\u6709\u5192\u865f) */\n"
"    background-image: url(:/a);\n"
"\n"
"    /* 2. \u8a2d\u5b9a\u5716\u7247\u4e0d\u91cd\u8907 */\n"
"    background-repeat: no-repeat;\n"
"\n"
"    /* 3. \u8a2d\u5b9a\u5716\u7247\u7f6e\u4e2d */\n"
"    background-position: center;\n"
"\n"
"    /* 4. \u8a2d\u5b9a\u5713\u89d2 (\u9019\u5c31\u662f\u4f60\u8981\u7684\u73fe\u4ee3\u611f) */\n"
"    border-radius: 20px;\n"
"\n"
"    /* 5. \u9078\u64c7\u6027\uff1a\u52a0\u4e0a\u908a\u6846\u8b93\u5361\u7247\u66f4\u660e\u986f */\n"
"    border: 1px solid #2d2f45;\n"
"}")
        self.photo.setFrameShape(QFrame.Shape.StyledPanel)
        self.photo.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(720, 100, 271, 331))
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 271, 331))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName(u"statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"OctSrv Launcher", None))
    # retranslateUi

