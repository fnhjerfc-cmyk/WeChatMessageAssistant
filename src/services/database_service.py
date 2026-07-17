import sqlite3
from pathlib import Path


class DatabaseService:

    def __init__(self):
        # 创建 data 文件夹
        Path("data").mkdir(exist_ok=True)

        # 数据库路径
        self.db_path = "data/wechat.db"

        # ===== 调试信息 =====
        print("=" * 60)
        print("当前工作目录：", Path.cwd())
        print("数据库路径：", Path(self.db_path).resolve())
        print("=" * 60)

        # 连接数据库
        self.conn = sqlite3.connect(self.db_path)

        # 创建数据表
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # 消息表
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT,
            sender TEXT,
            content TEXT,
            receive_time TEXT,
            is_at_me INTEGER,
            reminder_time TEXT,
            reminder_status INTEGER,
            create_time TEXT
        )
        """)

        # 微信群表
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS groups(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT UNIQUE,
            remark TEXT,
            create_time TEXT
        )
        """)

        self.conn.commit()

    # ==========================
    # 新增消息
    # ==========================
    def insert_message(
        self,
        group_name,
        sender,
        content,
        receive_time,
        is_at_me,
        reminder_time,
        reminder_status,
        create_time,
    ):
        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO messages(
            group_name,
            sender,
            content,
            receive_time,
            is_at_me,
            reminder_time,
            reminder_status,
            create_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            group_name,
            sender,
            content,
            receive_time,
            is_at_me,
            reminder_time,
            reminder_status,
            create_time
        ))

        self.conn.commit()

    # ==========================
    # 查询消息
    # ==========================
    def get_messages(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT
            id,
            group_name,
            sender,
            content,
            receive_time
        FROM messages
        ORDER BY id DESC
        """)

        return cursor.fetchall()

    # ==========================
    # 新增微信群
    # ==========================
    def insert_group(self, group_name, remark, create_time):
        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO groups(
            group_name,
            remark,
            create_time
        )
        VALUES (?, ?, ?)
        """, (
            group_name,
            remark,
            create_time
        ))

        self.conn.commit()

    # ==========================
    # 查询所有微信群
    # ==========================
    def get_groups(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT
            id,
            group_name,
            remark,
            create_time
        FROM groups
        ORDER BY id DESC
        """)

        return cursor.fetchall()

    # ==========================
    # 删除微信群
    # ==========================
    def delete_group(self, group_id):
        cursor = self.conn.cursor()

        cursor.execute("""
        DELETE FROM groups
        WHERE id = ?
        """, (group_id,))

        self.conn.commit()

    # ==========================
    # 删除消息
    # ==========================
    def delete_message(self, message_id):
        cursor = self.conn.cursor()

        cursor.execute("""
        DELETE FROM messages
        WHERE id = ?
        """, (message_id,))

        self.conn.commit()

    # ==========================
    # 关闭数据库
    # ==========================
    def close(self):
        self.conn.close()