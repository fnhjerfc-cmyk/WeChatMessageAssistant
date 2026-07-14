from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QListWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QStatusBar,
    QStackedWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        print("====== MainWindow V0.4 已加载 ======")

        self.setWindowTitle("微信消息助手 V0.4")
        self.resize(1200, 700)

        # ==========================
        # 中央窗口
        # ==========================
        central = QWidget()
        self.setCentralWidget(central)

        # 主布局
        layout = QHBoxLayout(central)

        # ==========================
        # 左侧菜单
        # ==========================
        self.menu = QListWidget()
        self.menu.setFixedWidth(220)

        self.menu.addItems([
            "📥 消息中心",
            "🔔 提醒中心",
            "👥 微信群",
            "📊 数据统计",
            "📤 导出Excel",
            "⚙ 设置"
        ])

        # ==========================
        # 页面容器
        # ==========================
        self.pages = QStackedWidget()

        # =====================================================
        # 页面1：消息中心
        # =====================================================

        page_message = QWidget()

        message_layout = QVBoxLayout(page_message)

        title = QLabel("📥 消息中心")
        title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )

        self.message_list = QListWidget()

        self.test_button = QPushButton(
            "添加测试消息"
        )

        message_layout.addWidget(title)
        message_layout.addWidget(self.message_list)
        message_layout.addWidget(self.test_button)

        self.pages.addWidget(page_message)

        # =====================================================
        # 页面2：提醒中心
        # =====================================================

        page_reminder = QWidget()

        reminder_layout = QVBoxLayout(page_reminder)

        reminder_title = QLabel("🔔 提醒中心")
        reminder_title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )

        reminder_info = QLabel(
            "提醒功能开发中..."
        )

        reminder_layout.addWidget(reminder_title)
        reminder_layout.addWidget(reminder_info)
        reminder_layout.addStretch()

        self.pages.addWidget(page_reminder)

        # =====================================================
        # 页面3：微信群
        # =====================================================

        page_group = QWidget()

        group_layout = QVBoxLayout(page_group)

        group_title = QLabel("👥 微信群管理")
        group_title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )

        group_info = QLabel(
            "微信群管理功能开发中..."
        )

        group_layout.addWidget(group_title)
        group_layout.addWidget(group_info)
        group_layout.addStretch()

        self.pages.addWidget(page_group)
                # =====================================================
        # 页面4：数据统计
        # =====================================================

        page_stat = QWidget()

        stat_layout = QVBoxLayout(page_stat)

        stat_title = QLabel("📊 数据统计")
        stat_title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )

        stat_info = QLabel(
            "暂无统计数据"
        )

        stat_layout.addWidget(stat_title)
        stat_layout.addWidget(stat_info)
        stat_layout.addStretch()

        self.pages.addWidget(page_stat)

        # =====================================================
        # 页面5：导出Excel
        # =====================================================

        page_export = QWidget()

        export_layout = QVBoxLayout(page_export)

        export_title = QLabel("📤 导出Excel")
        export_title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )

        export_info = QLabel(
            "暂未导出"
        )

        export_layout.addWidget(export_title)
        export_layout.addWidget(export_info)
        export_layout.addStretch()

        self.pages.addWidget(page_export)

        # =====================================================
        # 页面6：设置
        # =====================================================

        page_setting = QWidget()

        setting_layout = QVBoxLayout(page_setting)

        setting_title = QLabel("⚙ 设置")
        setting_title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )

        setting_info = QLabel(
            "设置功能开发中..."
        )

        setting_layout.addWidget(setting_title)
        setting_layout.addWidget(setting_info)
        setting_layout.addStretch()

        self.pages.addWidget(page_setting)

        # =====================================================
        # 主布局
        # =====================================================

        layout.addWidget(self.menu)
        layout.addWidget(self.pages)

        # =====================================================
        # 状态栏
        # =====================================================

        status = QStatusBar()
        status.showMessage("微信消息助手 V0.4 已启动")
        self.setStatusBar(status)

        # =====================================================
        # 菜单切换页面
        # =====================================================

        self.menu.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )

        # 默认打开第一页
        self.menu.setCurrentRow(0)
