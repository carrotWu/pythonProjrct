#coding=utf-8
import random

#1、有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                print i*100+j*10+k
                count+=1
print'不重复的数字一共有%d个'%(count)

#2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
# 可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

s=0
i=int(raw_input(u'请输入利润额:'))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
for index in range(6):
    if i>arr[index]:
        s+=(i-arr[index])*rat[index]
        print (i-arr[index])*rat[index]
        i=arr[index]
print s
