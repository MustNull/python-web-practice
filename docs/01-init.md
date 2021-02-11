# 项目初始化
## 项目概述
初始化项目仅需要实现基本的框架,和最最基本的功能,在初始化项目中我实现了以下几个功能点:

### 数据库连接
使用peewee + psycopg2 + postgresql实现,以后会配成可以支持多种数据,目前就是使用postgresql
代码在db目录下

### 数据库迁移
每次修改数据库,我肯定不想拿软件自己怼,也不想写一堆sql语句什么的,使用了peewee-migrate实现对数据库的迁移和回滚
并将这些操作封装成命令,供command.py调用
代码在lib/commands下

### 配置管理
配置要统一管理,目前感觉yaml的视觉体验是最棒的,实现了一个CONFIG实例,用于加载yaml配置文件,并且能够被.local.yml覆盖配置,支持使用`CONFIG.app.xxx`的形式使用该配置
代码实现参见`config/__init__.py`


### User数据的增删改查功能
当前面的几个工作都完成了,就可以开始真正的功能开发了,这里仅作示例,实现User数据的增删改查接口
首先我们需要定义User,UserDao, UserService三个类,分别继承BaseModel(app.model.base_model.BaseModel), BaseDao, BaseService即可,因为我们目前没有额外的逻辑,只需要继承并使用父类方法即可
dao类和service类本质上都是声明了一堆类方法,实际上是当作命名空间使用的,不会被实例化
然后controller层我们只要按照fastapi的官方文档那样写就可以了,仅仅是返回结果是从service来的

### 关于这里Controller, Service, Dao, Model的四层设计问题
为什么这样设计,简单说一下就是解耦,不同层负责不同层的事情
我这里的设计是:
- controller层向上直接接收fastapi处理过的来自用户的请求,对用户输入参数做基本的类型和结构校验,向下调用service层的方法返回给用户数据
- service层实现真实的业务逻辑,你业务逻辑复杂,这里就写得复杂,向下调用dao层函数操作数据库,平行调用其他Service的方法
- dao层负责数据库表的增删改查
- model层就是定义表结构和一些实例方法

未来各层还能做的事情
- controller 权限校验
- service 缓存
- dao (没有dao层,做缓存就很难再service层上做缓存了)

目前这么分层的好处是显而易见的,代码结构层次清晰,职责边界明显,查问题也好查,弊端是每次新增一个数据类型都要实现三个类,要是有一种方法一次性把三个类以模板的形式生成就好了(我后续会实现一个)


## 项目目录及文件介绍
- app/ 核心代码,主要以Model,Dao,Service,Controller四层分层
- config/ 配置管理
- db/ 存放迁移文件,一些获取数据库相关的类和函数
- docs/ 文档,写下心得
- lib/ 用于封装一些第三方库的函数或自定义函数
- static/ 用于存放一些可能需要的静态文件
- .flake8 语法检查配置
- .gitignore 忽略文件
- command.py 用于引入commands下的命令
- docker-compose.yml 用于快捷启动依赖服务
- makefile 简化常用操作,记录运行命令
- README.MD 自述文件
- requirements.txt python依赖库列表


