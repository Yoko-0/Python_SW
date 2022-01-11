import unittest, sys, json
sys.path.append('../')
from utils.db import Database

class TestDBMethods(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_insert(self):
        data_json = {"config": "test"}
        json_object = json.dumps(data_json)
        self.assertTrue(self.db.insert('format_data_test', 4, 1, 'test_name', 
            'desc', json_object, 'test_type', 'test_infra_type', 2, 3))

if __name__ == '__main__':
    unittest.main()
