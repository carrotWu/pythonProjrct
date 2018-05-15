#encoding=utf-8
from time import sleep,ctime
import  threading
#定义说和写的方法
def talk(content,loop):
    for i in range(loop):
        print("Start talk:%s %s" %(content,ctime()))
        sleep(2)

def write(content,loop):
    for i in range(loop):
        print("Start write:%s %s" % (content, ctime()))
        sleep(3)
#定义加载说和写的线程
threads=[]
t1=threading.Thread(target=talk,args=('Hello 51TEXT',2))
threads.append(t1)
t2=threading.Thread(target=write,args=('Life is hort,You need python',2))
threads.append(t2)

#执行多线程
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All the End %r" %ctime())