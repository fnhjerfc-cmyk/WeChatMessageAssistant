from PySide6.QtWidgets import QMessageBox

from src.services.logger_service import LoggerService
from src.services.database_service import DatabaseService
from src.services.message_service import MessageService
from src.services.group_service import GroupService


class MainController:

    def __init__(self, window):
        self.window = window

        self.logger = LoggerService()
        self.database = DatabaseService()
        self.message_service = MessageService()
        self.group_service = GroupService()

        # 初始化
        self.initialize()

        # 按钮事件
        self.window.test_button.clicked.connect(self.add_test_message)
        self.window.refresh_message_button.clicked.connect(self.refresh_message_list)
        self.window.delete_message_button.clicked.connect(
            self.delete_selected_message
        )
        self.window.search_button.clicked.connect(self.search_messages)
        self.window.clear_search_button.clicked.connect(self.clear_search)
        self.window.search_input.returnPressed.connect(self.search_messages)

        # 双击消息
        self.window.message_list.itemDoubleClicked.connect(
            self.show_message_detail
        )

        # 群组管理事件
        self.window.add_group_button.clicked.connect(self.add_group)
        self.window.delete_group_button.clicked.connect(self.delete_selected_group)

    def initialize(self):
        """初始化程序"""
        self.logger.info("MainController 初始化完成")

        self.database.create_tables()

        self.refresh_message_list()

        self.refresh_group_list()

    def add_test_message(self):
        """按顺序循环添加测试消息，便于搜索功能测试"""

        test_messages = [
            ("测试群", "张三", "欢迎使用微信消息助手！"),
            ("开发群", "李四", "今天完成 V0.5.5"),
            ("产品群", "王五", "下午三点开会"),
            ("运维群", "赵六", "服务器正常运行")
        ]

        if not hasattr(self, "_test_message_index"):
            self._test_message_index = 0

        group_name, sender, content = test_messages[self._test_message_index]

        self.message_service.add_message(
            group_name=group_name,
            sender=sender,
            content=content,
            receive_time="22:00"
        )

        self._test_message_index = (self._test_message_index + 1) % len(test_messages)

        self.refresh_message_list()

        self.logger.info(f"添加了一条测试消息: {group_name}/{sender}/{content}")

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

        self.window.message_count_label.setText(
            f"消息数量: {len(messages)}"
        )

    def search_messages(self):
        """根据关键词搜索消息并刷新列表"""

        keyword = self.window.search_input.text().strip()
        messages = self.message_service.search_messages(keyword)

        self.window.message_list.clear()

        for msg in messages:
            text = (
                f"{msg.receive_time} "
                f"【{msg.group_name}】 "
                f"{msg.sender}："
                f"{msg.content}"
            )

            self.window.message_list.addItem(text)

        self.window.message_count_label.setText(
            f"消息数量: {len(messages)}"
        )

    def clear_search(self):
        """清空搜索输入并恢复全部消息列表"""

        self.window.search_input.clear()
        self.refresh_message_list()

    def delete_selected_message(self):
        """删除选中的消息"""

        current_item = self.window.message_list.currentItem()

        if not current_item:
            QMessageBox.warning(
                self.window,
                "提示",
                "请选择要删除的消息"
            )
            return

        current_row = self.window.message_list.row(current_item)

        messages = self.message_service.get_all_messages()

        if current_row < 0 or current_row >= len(messages):
            QMessageBox.warning(
                self.window,
                "错误",
                "消息索引错误"
            )
            return

        message = messages[current_row]
        message_id = message.id

        reply = QMessageBox.question(
            self.window,
            "确认删除",
            "确定删除这条消息吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.database.delete_message(message_id)
            self.refresh_message_list()
            QMessageBox.information(
                self.window,
                "成功",
                "消息删除成功"
            )

    def show_message_detail(self, item):
        """双击查看消息"""

        QMessageBox.information(
            self.window,
            "消息详情",
            item.text()
        )

    def refresh_group_list(self):
        """刷新群组列表"""

        self.window.group_list.clear()

        groups = self.group_service.get_all_groups()

        for group in groups:
            # group is a tuple: (id, group_name, remark, create_time)
            group_id = group[0]
            group_name = group[1]
            remark = group[2]

            text = f"{group_name}"
            if remark:
                text += f" - {remark}"

            item = self.window.group_list.addItem(text)

    def add_group(self):
        """添加新群组"""

        group_name = self.window.group_name_input.text().strip()
        remark = self.window.group_remark_input.text().strip()

        if not group_name:
            QMessageBox.warning(
                self.window,
                "输入错误",
                "群名称不能为空"
            )
            return

        try:
            self.group_service.add_group(
                group_name=group_name,
                remark=remark
            )

            self.window.group_name_input.clear()
            self.window.group_remark_input.clear()

            self.refresh_group_list()

            self.logger.info(f"添加了微信群：{group_name}")

            QMessageBox.information(
                self.window,
                "成功",
                f"群组 '{group_name}' 添加成功"
            )

        except Exception as e:
            self.logger.error(f"添加群组失败：{str(e)}")
            QMessageBox.critical(
                self.window,
                "错误",
                f"添加群组失败：{str(e)}"
            )

    def delete_selected_group(self):
        """删除选中的群组"""

        current_item = self.window.group_list.currentItem()

        if not current_item:
            QMessageBox.warning(
                self.window,
                "提示",
                "请先选择要删除的群组"
            )
            return

        current_row = self.window.group_list.row(current_item)

        groups = self.group_service.get_all_groups()

        if current_row < 0 or current_row >= len(groups):
            QMessageBox.warning(
                self.window,
                "错误",
                "群组索引错误"
            )
            return

        group = groups[current_row]
        group_id = group[0]
        group_name = group[1]

        reply = QMessageBox.question(
            self.window,
            "确认删除",
            f"确定要删除群组 '{group_name}' 吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.group_service.delete_group(group_id)

                self.refresh_group_list()

                self.logger.info(f"删除了微信群：{group_name}")

                QMessageBox.information(
                    self.window,
                    "成功",
                    f"群组 '{group_name}' 已删除"
                )

            except Exception as e:
                self.logger.error(f"删除群组失败：{str(e)}")
                QMessageBox.critical(
                    self.window,
                    "错误",
                    f"删除群组失败：{str(e)}"
                )