#coding=utf-8
#Python单元测试框架——unittest
##对Math类进行单元测试
from clator import SS
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print ("test start")
    def test_add(self):
        j=SS(5,10)
        self.assertEqual(j.add(),15)
    def tearDown(self):
        print ("test end")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_add"))
    runner=unittest.TextTestRunner()
    runner.run(suite)



