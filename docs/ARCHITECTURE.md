# 微信消息助手（WeChatMessageAssistant）系统架构说明

> 文档版本：V1.0  
> 当前项目版本：V0.5.6  
> 更新时间：2026-07-18

---

# 一、架构设计目标

微信消息助手采用分层架构设计。

核心思想：

> 界面负责显示，控制器负责流程，服务负责业务，模型负责数据。

目标：

- 降低代码耦合
- 方便后期扩展
- 支持真实微信接入
- 支持长期维护

---

# 二、整体架构

当前架构：

```
用户操作

    ↓

View（界面层）

    ↓

Controller（控制层）

    ↓

Service（业务层）

    ↓

Database（数据层）

    ↓

SQLite 数据库
```

---

# 三、目录职责

## src/views

界面层。

主要负责：

- 窗口显示
- 控件创建
- 用户界面布局

当前：

```
src/views/main_window.py
```

---

## src/controllers

控制层。

主要负责：

- 接收用户操作
- 调用业务服务
- 控制页面刷新
- 管理页面状态


当前：

```
src/controllers/main_controller.py
```

---

## src/services

业务服务层。

负责：

- 数据处理
- 数据查询
- 数据删除
- 业务逻辑


当前：

```
src/services/

database_service.py

message_service.py
```

---

## src/models

数据模型层。

负责：

定义数据结构。

当前：

```
src/models/message.py
```

---

# 四、各层关系说明

## 1. View 层

不能：

- 直接操作数据库
- 写 SQL
- 处理复杂业务


例如：

错误：

```
按钮点击

↓

直接 DELETE SQLite
```


正确：

```
按钮点击

↓

Controller

↓

Service

↓

Database
```

---

# 五、当前主要模块

---

# 1. MainWindow

文件：

```
views/main_window.py
```


职责：

创建主窗口。


包含：

## 消息中心

当前功能：

- 消息列表
- 搜索框
- 搜索按钮
- 清空按钮
- 排序按钮
- 删除按钮
- 消息数量显示


---

# 2. MainController

文件：

```
controllers/main_controller.py
```


职责：

连接界面和业务。


当前管理：

## 消息刷新

负责：

```
刷新按钮

↓

加载消息

↓

更新列表
```


---

## 搜索状态


保存：

```
current_keyword
```


作用：

保证：

搜索后排序

不会丢失搜索条件。

---

## 排序状态


保存：

例如：

```
sort_desc
```


控制：

最新

或者

最早


---

# 3. MessageService

文件：

```
services/message_service.py
```


职责：

消息业务。


当前功能：

## 获取全部消息

```
get_all_messages()
```


## 搜索消息

```
search_messages(keyword)
```


支持：

group_name

sender

content


---

# 4. DatabaseService

文件：

```
services/database_service.py
```


职责：

数据库操作。


负责：

- SQLite连接
- SQL执行
- 删除数据


原则：

其他模块不能直接操作数据库。

---

# 五、消息数据流程

## 添加消息

流程：

```
用户操作

↓

Controller

↓

MessageService

↓

DatabaseService

↓

SQLite

```

---

## 显示消息


流程：

```
SQLite

↓

DatabaseService

↓

MessageService

↓

Controller

↓

MainWindow

↓

列表显示

```

---

# 六、搜索流程

用户输入：

```
张三
```


流程：

```
搜索按钮

↓

Controller

↓

保存：

current_keyword="张三"

↓

MessageService.search_messages()

↓

Database查询

↓

返回Message列表

↓

更新界面
```

---

# 七、排序流程

当前支持：

最新排序：

```
18:45

14:20

10:30

09:00
```


最早排序：

```
09:00

10:30

14:20

18:45
```


流程：

```
点击排序按钮

↓

Controller改变排序状态

↓

refresh_message_list()

↓

判断：

是否存在搜索关键词

↓

有：

search_messages()

无：

get_all_messages()

↓

排序

↓

刷新界面
```

---

# 八、为什么搜索状态放在 Controller

原因：

搜索属于用户当前操作状态。

例如：

用户：

搜索：

```
张三
```

然后：

点击排序。


用户期望：

仍然查看张三。

而不是：

重新显示所有消息。


所以：

Controller负责保存：

- 搜索状态
- 排序状态
- 页面状态

---

# 九、数据库设计原则

当前数据库：

SQLite

文件：

```
data/wechat.db
```


原则：

Service负责访问数据库。

禁止：

View直接访问数据库。

---

# 十、未来微信接入设计

未来增加：

微信监听模块。


预计：

新增：

```
src/services/wechat_service.py
```


负责：

- 接收微信消息
- 解析消息
- 转换Message对象


流程：

未来：

```
微信

↓

WechatService

↓

MessageService

↓

Database

↓

消息中心
```

---

# 十一、未来提醒系统设计


计划增加：

ReminderService


负责：

- @我的提醒
- 定时提醒
- 未处理提醒


流程：

```
Message

↓

判断提醒规则

↓

ReminderService

↓

通知用户
```

---

# 十二、开发原则

## 原则1

不要让一个模块承担所有事情。


错误：

```
main_controller.py

包含：

界面

数据库

业务

微信监听

```

正确：

```
View

Controller

Service

Model

```

---

## 原则2

小步开发。

每个版本：

一个主要目标。

---

## 原则3

先测试，再提交。

流程：

```
开发

↓

测试

↓

验收

↓

commit

↓

tag
```

---

# 十三、当前架构状态

目前：

```
界面层

        ✓

控制层

        ✓

业务层

        ✓

数据库层

        ✓

微信接入

        未开始

提醒系统

        未开始

```

---

# 十四、下一阶段方向

当前：

V0.5.6


下一版本：

V0.5.7


目标：

消息中心批量删除。


未来路线：

```
V0.5

消息中心完善

↓

V0.6

提醒系统

↓

V0.7

微信消息接入

↓

V0.8

统计分析

↓

V1.0

完整微信助手
```

---

# 文档维护规则

当架构发生重大变化时更新此文件。

例如：

新增：

- 新服务
- 新数据模型
- 新模块
- 新通信方式

必须同步更新。
