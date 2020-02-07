#!/bin/sh
. .venv/bin/activate
. .env
export FLASK_APP FLASK_ENV DATABASE_URI PORT
python run.py
