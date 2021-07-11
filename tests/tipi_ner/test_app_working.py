import unittest
import sys
sys.path.append('/app')

from ner.app import create_app
from ner.settings import Config

class TestLimit(unittest.TestCase):

    # def setUp(self):
    #     Config.TESTING = True
    #     Config.USE_ALERTS = True
    #     app = create_app(config=Config)
    #     self.client = app.test_client()

    def setUp(self):
        Config.TESTING = True
        Config.USE_ALERTS = True
        app = create_app(config=Config)
        self.client = app.test_client()

    def test_app_working(self):
        res = self.client.post('/ping')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b'pong')

if __name__ == '__main__':
    unittest.main()
