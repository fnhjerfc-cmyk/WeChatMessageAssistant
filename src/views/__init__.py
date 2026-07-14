from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QListWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QStatusBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("微信消息助手 V0.2")
        self.resize(1200, 700)

        # ========= 中央窗口 =========
        central = QWidget()
        self.setCentralWidget(central)

        # 总布局
        layout = QHBoxLayout(central)

        # ========= 左侧菜单 =========
        self.menu = QListWidget()
        self.menu.addItems([
            "📥 消息中心",
            "🔔 提醒中心",
            "👥 微信群",
            "📊 数据统计",
            "📤 导出Excel",
            "⚙ 设置"
        ])
        self.menu.setFixedWidth(220)

        # ========= 右侧 =========
        right = QVBoxLayout()

        title = QLabel("欢迎使用微信消息助手")
        title.setStyleSheet("font-size:22px;font-weight:bold;")

        info = QLabel(
            "程序状态：🟢 已启动\n\n"
            "今日消息：0\n"
            "@我的：0\n"
            "待提醒：0"
        )

        right.addWidget(title)
        right.addWidget(info)
        right.addStretch()

        layout.addWidget(self.menu)
        layout.addLayout(right)

        # ========= 状态栏 =========
        status = QStatusBar()
        status.showMessage("微信消息助手 V0.2 已启动")
        self.setStatusBar(status)