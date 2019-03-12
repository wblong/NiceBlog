import unittest
from app import create_app, db
from app.models import User, Role, Permission, Blog, Comment, Favourite, Label


class UserModelTestCase(unittest.TestCase):

    # 测试前执行
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        # 根据数据模型创建对应的表
        db.create_all()

    # 测试后执行
    def tearDown(self):
        db.session.remove()
        # 删除数据库中的表
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='123456')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='123456')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='123456')
        self.assertTrue(u.verify_password('123456'))
        self.assertFalse(u.verify_password('1234567'))

    def test_password_salts_are_random(self):
        u1 = User(password='123456')
        u2 = User(password='1234567')
        self.assertTrue(u1.password_hash != u2.password_hash)
