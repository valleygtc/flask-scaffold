import unittest
import sys

from app import create_app, db
from app.models import PlanTask # TODO

app = create_app('test')
app.app_context().push()


# TODO
def fake_records(n):
    for i in range(n):
        e = PlanTask(field1=value1, field2=value2)
        db.session.add(e)
    db.session.commit()


def setUpModule():
    db.drop_all()
    db.create_all()
    fake_records(20)


def tearDownModule():
    pass


# TODO: 测试用例
class TestExample(unittest.TestCase):
    url = '/example'

    def test_default(self):
        with app.test_client() as client:
            rv = client.get(self.url, headers={'Authorization': authorization})
            json_data = rv.get_json()
            self.assertTrue(json_data['success'])


if __name__ == '__main__':
    if sys.argv[1] == 'fake_records':
        fake_records(20)
        
