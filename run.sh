#!/bin/sh
. .venv/bin/activate

export FLASK_APP=manage.py
export FLASK_ENV=development | test | production
export DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{localhost}/{db_name}?charset=utf8' # 指定字符集utf8
export PORT=5000

python run.py
