print("----猜数小游戏----")
import random

secret = random.randint(1,10)
times = 3
guess = 0
print("请输入您的数字: ","end = ")
while(guess != secret and times != 0):
    temp = input()
    while not temp.isdigit():
        temp = input("请输入一个整数")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print("哼，竟然猜对了！")
    else:
        if guess > secret:
            print("大了，大了！")
        else:
            print("小了，小了！")
        if times >0:
            print("再给你一次机会！")

