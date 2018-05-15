#encoding=utf-8
#转义 \
str='hello,\nAre you ok?'
print(str)

#路径中的\ 要用\\来自转义
print("c:\\python35")

#转义出单引号‘
print('My name is \'Jack\' and you?')

#逻辑运算 and or
t=True
f=False
print(t and f)#False
print(t or f)#True

#数组
student=['jack','rose','Jack','Micle']
print(student)
print(student[2])
print(student[-1])
#下比标越界 报错：index out of range

#追加元素append()方法  (在数组末尾添加)
student.append('Xiao')
print(student)

#插入元素 insert()
student.insert(1,'No.2')
print(student)

#修改(替换)
student[0]='No.1'
print(student)

#删除 pop()方法 不加下边标默认删除最后一个
student.pop()
student.pop(1)
print(student)

#元组，与数组相似，用系小括号，元组一单定义里边的元素不能修改
course=('chinese','english','Math','computer')
print(course)
print(course[-1])#输出最后一个
print (course[0])
print(course[1:3])#输出下标1到2的元素（含头不含尾）
print(course[1:])#输出下标从1包含1到末尾的元素
print(course[:2])#输出下标2不含2以前的元素
#定义元组的时候，若只有一个元素需要这样写t=（1,） 必须加逗号以防止当做整数1

#元组长度len()
print(len(course))

#元组最大值max()
score=(21,23,55,6,22)
print(max(score))

#paython字典，可以储存任意类型对象的键值对。要求key唯一
#eg: d={key1:value,key2:value2}
sc={'jack':86,'Bob':88,'ros':100}
print(sc['Bob'])

#字典增加
sc['ss']=89
print(sc)
#字典修改
sc['Bob']=99
print(sc)
#字典删除
del sc['ss']
print(sc)
#清空字典 clear()
sc.clear()
#删除字典 del
del sc


bc={1:'jac',2:'fc',3:'sd'}
bc[4]='sdd'
print(bc)


#条件判断
score=75
if score>=80:
    print('Score is A')
else:
    print('Score is not A')

#elif   (else if的缩写)
if score>=80:
    print("SCORE IS A")
elif score>=60:
    print('Score is B')
else:
    print('Score is C')

#for 循环
#遍历student数组
for stu in student:
    print(stu)

#range(11) 生成10以内的整数序列
#计算1累加到10
sum=0
for i in range(11):
    sum=sum+i
print(sum)

#while 循环
n=10
while n>0:
    n=n-1
    print(n)
print("OVER")












