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

# V0.5.8

目标：
- 补齐消息阅读闭环
- 用户双击消息后，根据真实 message_id 查看完整消息

功能：
- 消息列表项使用真实 message_id 标识消息
- DatabaseService 支持按 message_id 查询单条消息
- MessageService 将数据库记录转换为 Message 对象
- 双击消息后显示群名称、发送人、接收时间和完整消息内容
- message_id 缺失时显示友好提示
- 消息不存在或已删除时显示友好提示
- 不修改数据库结构
- 不影响搜索、排序和删除功能

修改文件：
- docs/TASKS.md
- src/services/database_service.py
- src/services/message_service.py
- src/controllers/main_controller.py

验收标准：
✅ 程序正常启动
✅ 双击消息可以打开真实消息详情
✅ 群名称显示正确
✅ 发送人显示正确
✅ 接收时间显示正确
✅ 完整消息内容显示正确
✅ 搜索结果中的消息详情对应正确
✅ 切换最新/最早后，详情仍对应所选消息
✅ 查看详情后搜索条件和排序状态保持不变
✅ 单条删除功能保持正常
✅ 批量删除功能保持正常
✅ 查看详情不会修改数据库数据
✅ 未修改数据库表结构

已知问题：
- 当前“最新/最早”实际按数据库 id（插入顺序）排序，不是按 receive_time 排序
- 此问题不是 V0.5.8 消息详情功能造成
- 本版本不处理该排序缺陷，后续作为独立问题评估
