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
$ pip install -r requirements_top.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 使用清华大学镜像源
$ pip freeze > requirements.txt # 固定依赖包版本号
$ pip install -r requirements_dev.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 使用清华大学镜像源
```

全局搜索TODO，并按照MVC的顺序进行代码填写。

单元测试：python -m unittest test.py

run:
```bash
$ source .venv/bin/activate
$ source .env

$ flask create_tables # 创建数据库表
$ flask run [--host='0.0.0.0'/'::']
$ python run.py
$ bash run.sh
```

git: 注意：在加入git仓库之前，要先将`.env`加入`.gitignore`中。
