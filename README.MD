## Introduction
本项目为一个FastAPI+peewee+postgresql+celery的脚手架

docs目录下记录了每个细节是如何实现,算是一个用于学习的项目

## GetStart
- python3 -m venv .env
- source ./env/bin/activate
- make install
- make dev

## ToDo
- 实现基本功能,能够增删改查User 
    - 实现Model,Dao,Service基类方法,以及User的基于这三个的子类
    - 实现基本的controller,增删改查User
    - 实现gunicorn部署
- 补充文档&把本项目推上仓库
- 提供command命令,自动创建Model&Dao&Service类,并完成
- 迁移回滚命令补全迁移名称
- 依赖第三方docker-compose文件提供
- celery任务支持
- Dockerfile支持将项目打包成docker发布
- CICD流水线


