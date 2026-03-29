import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QFile


# 修正匯入路徑，確保能找到 gui 與 asset 模組
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# 請將 'gui.main_ui' 換成你實際轉檔後的檔名
# 將 'Ui_mainwindow' 換成你 .py 檔內 class 的名稱
try:
    from main_ui import Ui_mainwindow
except ImportError:
    print("錯誤：找不到 gui.main_ui 或 Ui_mainwindow，請檢查檔案名稱與資料夾內是否有 __init__.py")
    sys.exit(1)

import pywinstyles

class MyLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. 初始化 UI
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)
        
        # 2. 視窗透明化設定 (霧化效果必須開啟這個)
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        #self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 3. 執行自定義初始化
        self.setup_blur_effect()
        self.load_account_buttons()

    def setup_blur_effect(self):
        """套用 Windows 霧化 (Acrylic) 效果"""
        try:
            # 對你的主紅框套用霧化
            pywinstyles.apply_style(self.ui.AccountMenu, style="acrylic")
            # 如果想讓整個視窗也霧化，取消下面這行註釋
            # pywinstyles.apply_style(self, style="acrylic")
        except Exception as e:
            print(f"霧化效果載入失敗: {e}")

    def load_account_buttons(self):
        """動態生成帳號按鈕並強制排版"""
        # 模擬後台帳號資料
        accounts = ["IdealProduct580", "Steve_Player", "Alex_Expert"]
        
        # A. 強制建立並獲取 Layout
        layout = self.ui.AccountMenu.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.AccountMenu)
            self.ui.AccountMenu.setLayout(layout)
        
        # B. 設定排版細節
        # setContentsMargins(左, 上, 右, 下) -> 上方留 70px 避開「選擇帳號」標題
        layout.setContentsMargins(5, 5, 5, 5) 
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # C. 迴圈產生按鈕
        for name in accounts:
            btn = QPushButton(name)
            
            # D. 套用純紅、透明、消白框的 QSS
            btn.setStyleSheet("""
                QPushButton {
                    background-color: rgba(255, 0, 0, 60); /* 半透明紅 */
                    border: 2px solid rgba(255, 0, 0, 255); /* 純紅邊框 */
                    border-radius: 10px;
                    color: white;
                    font-size: 14px;
                    font-weight: bold;
                    min-height: 50px;
                    text-align: left;
                    padding-left: 20px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 0, 0, 150); /* 懸停時變深紅 */
                }
                QPushButton:pressed {
                    background-color: rgba(200, 0, 0, 200); /* 點擊時感饋 */
                }
            """)
            
            # E. 串接點擊事件
            btn.clicked.connect(lambda chk=False, n=name: self.on_account_clicked(n))
            
            # F. 塞進去
            layout.addWidget(btn)

    def on_account_clicked(self, name):
        """後台串接入口：處理帳號切換"""
        print(f"【後台指令】使用者選擇了帳號：{name}")
        # 在這裡呼叫你的登入驗證邏輯

# --- 啟動區 ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 解決高解析度螢幕縮放問題
    app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    
    window = MyLauncher()
    window.show()
    sys.exit(app.exec())