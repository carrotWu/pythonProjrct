#encoding=utf-8
import unittest
from First_test import Math

class TestMath(unittest.TestCase):
    def setUp(self):
        print("start test")
    def test_run(self):
        s=Math(1,2,3)
        self.assertEqual(s.add(),6)
        print("success")
    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_run"))#装载方法
    runner=unittest.TextTestRunner()
    runner.run(suite)