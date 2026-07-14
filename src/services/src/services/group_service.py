from datetime import datetime

from services.database_service import DatabaseService


class GroupService:

    def __init__(self):
        self.db = DatabaseService()

    # ==========================
    # 新增微信群
    # ==========================
    def add_group(self, group_name, remark=""):

        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.db.insert_group(
            group_name=group_name,
            remark=remark,
            create_time=create_time
        )

    # ==========================
    # 获取全部微信群
    # ==========================
    def get_all_groups(self):
        return self.db.get_groups()

    # ==========================
    # 删除微信群
    # ==========================
    def delete_group(self, group_id):
        self.db.delete_group(group_id)