import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print("about to test a function")
    def test_do_stuff(self):
        """
        Hello!
        """
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def tearDown(self):
        print('clean up')

if __name__ == '__main__':
    unittest.main()