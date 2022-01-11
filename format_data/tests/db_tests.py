import unittest, sys
sys.path.append('../')
from utils.db import Database

class TestDBMethods(unittest.TestCase):

     def setUp(self):
         self.db = Database()

if __name__ == '__main__':
    unittest.main()
