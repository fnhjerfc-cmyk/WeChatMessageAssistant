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


# V0.5.7

目标：
- 消息中心支持批量删除

功能：
- 支持 Ctrl + 鼠标左键多选消息
- 支持 Shift 连续选择消息
- 删除前显示选中消息数量
- 确认后批量删除数据库记录
- 删除后自动刷新消息列表和数量
- 保持当前搜索条件和排序状态

修改文件：
- docs/TASKS.md
- src/views/main_window.py
- src/controllers/main_controller.py
- src/services/database_service.py

验收标准：
□ 可以使用 Ctrl 选择多条不连续消息
□ 可以使用 Shift 选择连续消息
□ 未选择消息时显示提示
□ 删除确认框显示正确的选中数量
□ 取消删除时数据库和列表不发生变化
□ 确认后选中的消息全部从数据库删除
□ 删除后消息列表和消息数量自动更新
□ 搜索结果中批量删除不会误删其他消息
□ 最早排序下批量删除不会误删其他消息
□ 删除后保持当前搜索条件和排序状态
