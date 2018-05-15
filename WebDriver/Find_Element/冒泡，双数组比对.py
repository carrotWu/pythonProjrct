#coding=utf-8
# 1.B  2.E
#3.冒泡：
arr=[1,3,23,4,56,99]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
print(arr)
#4.编写一个A 数组中字符串不在B数组中的对比算法
A=["a","b","c","F"]
B=["D","E","F","b"]
for j in range(len(A)):
    if A[j] in B:
        print A[j]+"在数组B中"
    else:
        print A[j]+"不在数组B中"
#5.写一个sql语句   要求两表联合查询
# SELECT a.name,b.account
#  FROM A a
#  JOIN B b
#  ON a.id=b.id

