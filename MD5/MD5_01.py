#coding=utf-8
import hashlib

#MD5加密
def entry_md5(content):
    m = hashlib.md5()
    m.update(content.encode('utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    md5s = entry_md5('asd')
    print(md5s)
