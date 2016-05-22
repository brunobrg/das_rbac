import unittest
from model.user import User

class TestUser(unittest.TestCase):

    def test_create_new_user(self):
        new_user = User("bruno", "12345")
        self.assertTrue(new_user)
