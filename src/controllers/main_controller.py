from PySide6.QtWidgets import QMessageBox

from services.logger_service import LoggerService
from services.database_service import DatabaseService
from services.message_service import MessageService


class MainController:

    def __init__(self, window):
        self.window = window

        self.logger = LoggerService()
        self.database = DatabaseService()
        self.message_service = MessageService()

        # 初始化
        self.initialize()

        # 按钮事件
        self.window.test_button.clicked.connect(self.add_test_message)

        # 双击消息
        self.window.message_list.itemDoubleClicked.connect(
            self.show_message_detail
        )

    def initialize(self):
        """初始化程序"""
        self.logger.info("MainController 初始化完成")

        self.database.create_tables()

        self.refresh_message_list()

    def add_test_message(self):
        """添加一条测试消息"""

        self.message_service.add_message(
            group_name="测试群",
            sender="张三",
            content="欢迎使用微信消息助手！",
            receive_time="22:00"
        )

        self.refresh_message_list()

        self.logger.info("添加了一条测试消息")

    def refresh_message_list(self):
        """刷新消息列表"""

        self.window.message_list.clear()

        messages = self.message_service.get_all_messages()

        for msg in messages:

            text = (
                f"{msg.receive_time} "
                f"【{msg.group_name}】 "
                f"{msg.sender}："
                f"{msg.content}"
            )

            self.window.message_list.addItem(text)

    def show_message_detail(self, item):
        """双击查看消息"""

        QMessageBox.information(
            self.window,
            "消息详情",
            item.text()
        )