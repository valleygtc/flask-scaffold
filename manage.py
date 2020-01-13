import os
from app import create_app, db
from app.models import Student # TODO: 


app = create_app(os.getenv('FLASK_ENV', 'production'))


def make_shell_context():
    return dict(db=db, Student=Student) # TODO

app.shell_context_processor(make_shell_context)


"""create tables: student""" # TODO
@app.cli.command('create_tables')
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run()
