import unittest

class TestPytestWorking(unittest.TestCase):

    def inc(self, x):
        return x + 1

    def test_something(self):
        assert self.inc(3) == 4

if __name__ == '__main__':
    unittest.main()
