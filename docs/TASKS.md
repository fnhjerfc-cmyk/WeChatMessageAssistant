# V0.5.3

目标：
- 消息中心增加刷新按钮
- 消息数量实时显示

修改文件：
- src/views/main_window.py
- src/controllers/main_controller.py

验收标准：
✅ 程序正常启动
✅ 消息中心显示已有消息
✅ 点击刷新按钮可以重新加载消息
✅ 消息数量正确显示
✅ 添加测试消息后数量同步变化


# V0.5.4

目标：
- 消息中心支持删除消息

修改文件：
- src/views/main_window.py
- src/controllers/main_controller.py
- src/services/database_service.py

验收标准：
□ 可以选中一条消息
□ 点击"删除消息"按钮
□ 数据库中的消息被删除
□ 消息列表自动刷新
□ 消息数量自动更新
# V0.5.5

目标：
- 消息搜索功能

功能：
- 按发送人搜索
- 按群名称搜索
- 按消息内容搜索
- 实时过滤消息
- 清空搜索恢复全部消息

预计修改文件：
- src/views/main_window.py
- src/controllers/main_controller.py
- src/services/message_service.py
# V0.5.6

目标：
消息排序

功能：

- 默认按最新排序
- 支持切换最早/最新
- 搜索结果支持排序
- 不修改数据库结构
- 不修改 MessageService