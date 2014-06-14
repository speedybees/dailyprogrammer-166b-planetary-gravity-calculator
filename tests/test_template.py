import os, sys
sys.path.insert(0, os.path.abspath(".."))

class XTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
