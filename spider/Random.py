#coding=utf-8
import random
a=random.random()#生成0到1之间的随机小数
b=random.randint(0,10)#生成0到10之间的随机整数（含前不含后）
print('a='+str(a))
print "b="+str(b)

arr=[
    "像我这样优秀的人",
    "本该灿烂过一生",
    "怎么二十多年到头来",
    "还在人海里浮沉"
]
c=random.choice(arr)#随机选取字符串
print "c="+c

st='qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
lis=random.sample(st,4)
icd=''.join(lis)#验证码
print icd
