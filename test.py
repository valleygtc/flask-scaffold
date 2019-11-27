import unittest
import sys

from app import create_app, db
from app.models import PlanTask # TODO


test_app = create_app('test')


# TODO
def fake_records(n):
    for i in range(n):
        e = PlanTask(field1=value1, field2=value2)
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
        with test_app.test_client() as client:
            rv = client.get(
                self.url,
                headers={'Authorization': authorization},
            )
            json_data = rv.get_json()
            self.assertTrue(json_data['success'])


if __name__ == '__main__':
    if sys.argv[1] == 'fake_records':
        fake_records(20)
        
