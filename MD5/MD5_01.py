#coding=utf-8
import hashlib

#MD5加密
#MD5加密是单向不可逆加密 一般用于生成验签，用于判断收到数据的完整性。
def entry_md5(content):
    m = hashlib.md5()
    m.update(content.encode('utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    md5s = entry_md5('asd')
    print(md5s)
