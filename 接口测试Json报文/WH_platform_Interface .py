#coding=utf-8
import os
import sys
import logging
import requests
import hashlib
import random
from time import time
import datetime
import json
import mysql.connector

class scriptError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

class Interface(object):
    def __init__(self):
        self.projectPath="D:\\JettchAgent1.6.0\\execute\\"
        #self.logConfig()
    #资源路径分隔符替换
    def urlReplace(self,path):
        return path.replace('\\',r'\\')

    #配置logger
    def logConfig(self):
        logger=logging.getLogger('pyLogging')
        logger.setLevel(logging.INFO)







