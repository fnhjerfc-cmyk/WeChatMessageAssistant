版本：V0.5.3
名称：消息中心完善

目标：
完善现有消息中心基础功能，为 V0.6 微信接入做准备。

修改范围：

1. src/views/main_window.py

增加：
- 消息刷新按钮
- 今日消息数量显示区域


2. src/controllers/main_controller.py

增加：
- 消息数量统计刷新逻辑
- 刷新按钮事件绑定


保持不变：

- database_service.py
- message_service.py
- group_service.py
- message_manager.py
- wechat目录


验收标准：

✅ 程序正常启动
✅ 消息中心显示已有消息
✅ 点击刷新按钮可以重新加载消息
✅ 消息数量正确显示
✅ 添加测试消息后数量同步变化