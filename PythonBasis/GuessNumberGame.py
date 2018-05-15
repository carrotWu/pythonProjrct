import random
#生成随机数
answer=random.randint(1,100)
#玩家输入数字
n=int(input("请输入你所猜测的数字(0-100):"))
#判断输入数字大小
while n!=answer:
    if n>answer:
        n=int(input("你猜大了,请从新输入:"))
    elif n<answer:
        n=int(input("你猜小了,请从新输入:"))
#输入正确，游戏结束
print("恭喜你猜对了!")