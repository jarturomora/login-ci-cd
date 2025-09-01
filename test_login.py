import unittest
from main import login

class TestLogin(unittest.TestCase):
    def test_valid_user(self):
        self.assertTrue(login("alice", "password123"))

    def test_invalid_password(self):
        self.assertFalse(login("alice", "wrongpass"))

    def test_nonexistent_user(self):
        self.assertFalse(login("charlie", "nopass"))

if __name__ == "__main__":
    unittest.main()
