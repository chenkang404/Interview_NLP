### 环境
- py10
### 
### nohup 后台启动Worker服务
- 命令： nohup celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail,ops_trace --loglevel INFO
kill 掉Worker服务方法
- 1、查找后台进程PID,命令：ps aux | grep 'celery worker' | grep -v grep
- 2、kill -9 PID

### nohup 后台启动app 服务(单进程)
- 后台启动命令：nohup flask run --host 0.0.0.0 --port=5001 --debug > start_app_server_v1.log
kill 掉app服务
- 1、查找后台进程PID:        ps aux | grep 'flask run' | grep -v grep
- 2、kill -9 PID 





### error记录
- error_1
”“”pyhton
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "dify_setups" does not exist
LINE 2: FROM dify_setups 
             ^

[SQL: SELECT dify_setups.version AS dify_setups_version, dify_setups.setup_at AS dify_setups_setup_at 
FROM dify_setups 
 LIMIT %(param_1)s]
[parameters: {'param_1': 1}]
"""
解释：db没有更新，需要更新数据库，命令：flask db upgrade
参考：https://docs.dify.ai/zh-hans/learn-more/faq/install-faq  的5. 部署后如何升级版本？


公网IP 219.147.100.45
物理机ip 10.10.20.101