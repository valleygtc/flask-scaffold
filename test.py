import unittest
import sys

from app import create_app, db
from app.models import Student # TODO


test_app = create_app('test')


# TODO
def fake_records(n):
    for i in range(n):
        e = Student(name='namexxx', age=20, address='addressxxx')
        db.session.add(e)
    db.session.commit()


# TODO: 测试用例
class TestExample(unittest.TestCase):
    url = '/example'

    def setUp(self):
        with test_app.app_context():
            db.create_all()
            fake_records(30)

    def tearDown(self):
        with test_app.app_context():
            db.drop_all()

    def test_default(self):
        client = test_app.test_client()
        resp = client.get(
            self.url,
            headers={'Authorization': authorization},
        )
        json_data = resp.get_json()
        self.assertTrue(json_data['success'])


if __name__ == '__main__':
    if sys.argv[1] == 'fake_records':
        fake_records(20)
        
