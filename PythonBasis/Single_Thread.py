from time import ctime,sleep
#说
def talk():
    print("Start talk: %r" %ctime())

#写
def write():
    print("Start write: %r" %ctime())
    sleep(3)

if __name__=='__main__':
    talk()
    write()
    print('All end! %r' %ctime())
