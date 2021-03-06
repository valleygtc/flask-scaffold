TODO: 不要忘了更改这个README
# 简介
python3 + Flask框架快速开发后台api的脚手架。


# 使用
```bash
$ git clone <repo> [<dir_name>]
$ cd <project_name>
$ rm -rf .git
# 创建虚拟环境并安装依赖
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements-top.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 使用清华大学镜像源
$ pip freeze > requirements.txt # 固定依赖包版本号
$ pip install -r requirements-dev.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 使用清华大学镜像源
```

全局搜索TODO，并按照MVC的顺序进行代码填写。

单元测试：python -m unittest discover

run:
```bash
# 激活虚拟环境
$ source .venv/bin/activate

$ cp env.sh.example env.sh # 并在 env.sh 中填写好程序运行所需环境变量。

$ source env.sh # 读入环境变量。
$ flask create_tables # 创建数据库表。

$ flask run [--host='0.0.0.0'/'::']
$ python run.py
$ bash run.sh
```

env.sh 文件示例：
```
FLASK_APP=manage.py
FLASK_ENV=development | test | production
DATABASE_URI=mysql+mysqlconnector://{user}:{password}@{localhost}/{db_name}?charset=utf8
PORT=5000
```
