# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QAction, QCursor, QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMenu,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QToolButton,
    QWidget,
)

# Keep compatibility with different run paths.
try:
    import mainphoto_rc  # type: ignore
except ImportError:
    try:
        from gui.asset.texture import mainphoto_rc  # type: ignore
    except ImportError:
        mainphoto_rc = None


class Ui_CustomMainWindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName("custom_mainwindow")

        mainwindow.resize(1280, 720)
        mainwindow.setAutoFillBackground(False)
        mainwindow.setTabShape(QTabWidget.TabShape.Triangular)
        mainwindow.setStyleSheet(
            "#centralwidget {\n"
            "    background-image:url(:/b);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center;\n"
            "}\n"
            "QPushButton {\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.2);\n"
            "    border-radius: 10px;\n"
            "    color: white;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    margin-top: 0px;\n"
            "    margin-bottom: 4px;\n"
            "    background-color: rgba(255, 255, 255, 0.2);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.5);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(0, 0, 0, 0.2);\n"
            "}\n"
        )

        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QFrame(self.centralwidget)
        self.photo.setObjectName("photo")
        self.photo.setGeometry(QRect(79, 110, 771, 401))
        self.photo.setStyleSheet(
            "#photo {\n"
            "    border-image: url(:/a);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center;\n"
            "    border-radius: 40px;\n"
            "    border: 1px solid #2d2f45;\n"
            "}\n"
        )
        self.photo.setFrameShape(QFrame.Shape.StyledPanel)
        self.photo.setFrameShadow(QFrame.Shadow.Raised)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(900, 100, 321, 421))
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet(
            "#scrollArea {\n"
            "    background-color: transparent;\n"
            "    border-radius: 40px;\n"
            "    border: none;\n"
            "}\n"
            "#scrollAreaWidgetContents {\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "}\n"
            "QLabel {\n"
            "    color: #000000;\n"
            "    font-family: \"Microsoft JhengHei\";\n"
            "}\n"
            "#background {\n"
            "    background-color: qlineargradient(\n"
            "        x1: 0, y1: 0, x2: 1, y2: 1,\n"
            "        stop: 0 rgba(255, 255, 255, 0.12),\n"
            "        stop: 0.5 rgba(255, 255, 255, 0.05),\n"
            "        stop: 1 rgba(255, 255, 255, 0.1)\n"
            "    );\n"
            "    border-radius: 15px;\n"
            "    border: 1px solid rgba(255, 255, 255, 0.1);\n"
            "}\n"
            "#background:hover {\n"
            "    background-color: rgba(255, 255, 255, 0.15);\n"
            "    border: 1px solid rgba(189, 147, 249, 0.5);\n"
            "}\n"
            "#annou {\n"
            "    color: #ffffff;\n"
            "    font-size: 20px;\n"
            "}\n"
            "#date {\n"
            "    color: #6272a4;\n"
            "    font-size: 11px;\n"
            "}\n"
            "#pushButton {\n"
            "    color: #bd93f9;\n"
            "    background: transparent;\n"
            "    font-weight: bold;\n"
            "    border: none;\n"
            "}\n"
            "#pushButton:hover {\n"
            "    color: #ff79c6;\n"
            "}\n"
        )

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 321, 421))

        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.background = QFrame(self.scrollAreaWidgetContents)
        self.background.setObjectName("background")
        self.background.setEnabled(True)
        self.background.setFrameShape(QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QFrame.Shadow.Raised)

        self.annou = QLabel(self.background)
        self.annou.setObjectName("annou")
        self.annou.setGeometry(QRect(20, 10, 81, 21))

        self.pushButton = QPushButton(self.background)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(210, 370, 82, 26))

        self.frame = QFrame(self.background)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(20, 50, 261, 31))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.annou_2 = QLabel(self.frame)
        self.annou_2.setObjectName("annou_2")
        self.annou_2.setGeometry(QRect(10, 10, 91, 20))

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annou_2.sizePolicy().hasHeightForWidth())
        self.annou_2.setSizePolicy(sizePolicy)

        self.date = QLabel(self.frame)
        self.date.setObjectName("date")
        self.date.setGeometry(QRect(200, 10, 61, 20))

        self.horizontalLayout.addWidget(self.background)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QRect(360, 620, 261, 71))

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(QRect(360, 530, 261, 71))

        self.LauncherSetting = QPushButton(self.centralwidget)
        self.LauncherSetting.setObjectName("LauncherSetting")
        self.LauncherSetting.setGeometry(QRect(640, 620, 261, 71))
        font = QFont()
        font.setFamilies(["微軟正黑體"])
        font.setPointSize(15)
        font.setBold(True)
        self.LauncherSetting.setFont(font)
        self.LauncherSetting.setMouseTracking(True)
        self.LauncherSetting.setStyleSheet(
            "#LauncherSetting {\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.1);\n"
            "    border-radius: 12px;\n"
            "    padding: 10px;\n"
            "    text-align: right;\n"
            "}\n"
            "#LauncherSetting:hover {\n"
            "    background-color: rgba(255, 255, 255, 0.25);\n"
            "    border: 2px solid rgba(255, 255, 255, 0.6);\n"
            "    padding: 9px;\n"
            "}\n"
        )

        self.ChangeSkin = QPushButton(self.centralwidget)
        self.ChangeSkin.setObjectName("ChangeSkin")
        self.ChangeSkin.setGeometry(QRect(640, 530, 261, 71))
        font1 = QFont()
        font1.setPointSize(15)
        self.ChangeSkin.setFont(font1)
        self.ChangeSkin.setMouseTracking(True)
        self.ChangeSkin.setStyleSheet(
            "#ChangeSkin {\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.1);\n"
            "    border-radius: 12px;\n"
            "    padding: 10px;\n"
            "    text-align: right;\n"
            "}\n"
            "#ChangeSkin:hover {\n"
            "    background-color: rgba(255, 255, 255, 0.25);\n"
            "    border: 2px solid rgba(255, 255, 255, 0.6);\n"
            "    padding: 9px;\n"
            "}\n"
        )

        self.LaunchGame = QPushButton(self.centralwidget)
        self.LaunchGame.setObjectName("LaunchGame")
        self.LaunchGame.setGeometry(QRect(920, 530, 291, 161))
        font2 = QFont()
        font2.setFamilies(["微軟正黑體 Light"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.LaunchGame.setFont(font2)
        self.LaunchGame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.LaunchGame.setMouseTracking(True)
        self.LaunchGame.setStyleSheet(
            "#LaunchGame {\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.1);\n"
            "    border-radius: 12px;\n"
            "    padding: 10px;\n"
            "    text-align: right;\n"
            "}\n"
            "#LaunchGame:hover {\n"
            "    background-color: rgba(255, 255, 255, 0.25);\n"
            "    border: 2px solid rgba(255, 255, 255, 0.6);\n"
            "    padding: 9px;\n"
            "}\n"
        )

        self.DCLink = QPushButton(self.centralwidget)
        self.DCLink.setObjectName("DCLink")
        self.DCLink.setGeometry(QRect(90, 620, 71, 71))
        self.DCLink.setStyleSheet(
            "#DCLink {\n"
            "    border-image:url(:/c);\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.2);\n"
            "    border-radius: 35px;\n"
            "    color: white;\n"
            "}\n"
        )

        self.YTLink = QPushButton(self.centralwidget)
        self.YTLink.setObjectName("YTLink")
        self.YTLink.setGeometry(QRect(90, 530, 71, 71))
        self.YTLink.setStyleSheet(
            "#YTLink {\n"
            "    border-image:url(:/g);\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.2);\n"
            "    border-radius: 35px;\n"
            "    color: white;\n"
            "}\n"
        )

        self.OfficialWebLink = QPushButton(self.centralwidget)
        self.OfficialWebLink.setObjectName("OfficialWebLink")
        self.OfficialWebLink.setGeometry(QRect(180, 530, 71, 71))
        self.OfficialWebLink.setStyleSheet(
            "#OfficialWebLink {\n"
            "    border-image:url(:/f);\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.2);\n"
            "    border-radius: 35px;\n"
            "    color: white;\n"
            "}\n"
        )

        self.GitHubLink = QPushButton(self.centralwidget)
        self.GitHubLink.setObjectName("GitHubLink")
        self.GitHubLink.setGeometry(QRect(180, 620, 71, 71))
        self.GitHubLink.setStyleSheet(
            "#GitHubLink {\n"
            "    border-image:url(:/e);\n"
            "    background-color: rgba(255, 255, 255, 0.1);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.2);\n"
            "    border-radius: 35px;\n"
            "    color: white;\n"
            "}\n"
        )

        self.AccountSwitch = QToolButton(self.centralwidget)
        self.AccountSwitch.setObjectName("AccountSwitch")
        self.AccountSwitch.setGeometry(QRect(890, 20, 330, 72))
        self.AccountSwitch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AccountSwitch.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.AccountSwitch.setStyleSheet(
            "#AccountSwitch {\n"
            "    background-color: rgba(31, 41, 67, 0.95);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.12);\n"
            "    border-radius: 24px;\n"
            "    color: #f4f6ff;\n"
            "    font-family: \"Microsoft JhengHei\";\n"
            "    font-size: 15px;\n"
            "    font-weight: bold;\n"
            "    text-align: left;\n"
            "    padding-left: 22px;\n"
            "}\n"
            "#AccountSwitch:hover {\n"
            "    background-color: rgba(48, 58, 88, 0.95);\n"
            "    border: 1px solid rgba(255, 255, 255, 0.2);\n"
            "}\n"
        )

        self.AccountMenu = QMenu(self.AccountSwitch)
        self.AccountMenu.setObjectName("AccountMenu")
        self.AccountMenu.setMinimumWidth(330)
        self.AccountMenu.setStyleSheet(
            "QMenu {\n"
            "    background-color: rgba(8, 22, 56, 240);\n"
            "    border: 1px solid rgba(123, 140, 187, 0.35);\n"
            "    border-radius: 14px;\n"
            "    padding: 10px 8px;\n"
            "    color: #d7deff;\n"
            "    font-family: \"Microsoft JhengHei\";\n"
            "    font-size: 13px;\n"
            "}\n"
            "QMenu::item {\n"
            "    background-color: transparent;\n"
            "    border-radius: 10px;\n"
            "    padding: 12px 14px;\n"
            "    margin: 2px 4px;\n"
            "}\n"
            "QMenu::item:selected {\n"
            "    background-color: rgba(107, 95, 235, 0.36);\n"
            "    color: #f4f6ff;\n"
            "}\n"
            "QMenu::separator {\n"
            "    height: 1px;\n"
            "    background: rgba(255, 255, 255, 0.14);\n"
            "    margin: 6px 8px;\n"
            "}\n"
        )

        self.accountMenuTitleAction = QAction(mainwindow)
        self.accountMenuTitleAction.setEnabled(False)
        self.AccountMenu.addAction(self.accountMenuTitleAction)
        self.AccountMenu.addSeparator()

        self.accountCurrentAction = QAction(mainwindow)
        self.accountCurrentAction.setCheckable(True)
        self.accountCurrentAction.setChecked(True)
        self.AccountMenu.addAction(self.accountCurrentAction)
        self.AccountMenu.addSeparator()

        self.accountAddAction = QAction(mainwindow)
        self.AccountMenu.addAction(self.accountAddAction)

        self.accountLogoutAction = QAction(mainwindow)
        self.AccountMenu.addAction(self.accountLogoutAction)

        self.AccountSwitch.setMenu(self.AccountMenu)

        mainwindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(mainwindow)
        self.statusBar.setObjectName("statusBar")
        mainwindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainwindow)
        QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("custom_mainwindow", "OctSrv Launcher", None))
        self.annou.setText(QCoreApplication.translate("custom_mainwindow", "最新公告", None))
        self.pushButton.setText(QCoreApplication.translate("custom_mainwindow", "更多-->", None))
        self.annou_2.setText(QCoreApplication.translate("custom_mainwindow", "annou", None))
        self.date.setText(QCoreApplication.translate("custom_mainwindow", "2026-3-15", None))
        self.pushButton_4.setText(QCoreApplication.translate("custom_mainwindow", "PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("custom_mainwindow", "PushButton", None))
        self.LauncherSetting.setText(QCoreApplication.translate("custom_mainwindow", "啟動器設定          ", None))
        self.ChangeSkin.setText(QCoreApplication.translate("custom_mainwindow", "更換皮膚(Coming Soon)  ", None))
        self.LaunchGame.setText(QCoreApplication.translate("custom_mainwindow", "伺服器選單     ", None))
        self.AccountSwitch.setText(QCoreApplication.translate("custom_mainwindow", "●  IdealProduct580\n   正版帳號        ▾", None))
        self.accountMenuTitleAction.setText(QCoreApplication.translate("custom_mainwindow", "切換帳號", None))
        self.accountCurrentAction.setText(QCoreApplication.translate("custom_mainwindow", "IdealProduct580  |  Microsoft 帳號   ✓", None))
        self.accountAddAction.setText(QCoreApplication.translate("custom_mainwindow", "+  新增帳號", None))
        self.accountLogoutAction.setText(QCoreApplication.translate("custom_mainwindow", "登出當前帳號", None))
        self.DCLink.setText("")
        self.YTLink.setText("")
        self.OfficialWebLink.setText("")
        self.GitHubLink.setText("")
