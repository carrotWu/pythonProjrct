#coding=utf-8
class SS:
    a=1
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
if __name__ == '__main__':
    print (SS.a)
