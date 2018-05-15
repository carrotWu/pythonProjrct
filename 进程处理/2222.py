#coding=utf-8
a = 2
b = 3

class t:
    def asc(self):
        print(a)

if __name__ == '__main__':
    fun = t()
    for i in range(a,b):
        fun.asc()
        a+=1
