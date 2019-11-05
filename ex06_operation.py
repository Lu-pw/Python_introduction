# 0. Python 的 floor 除法现在使用 “//” 实现，那 3.0 // 2.0 您目测会显示什么内容呢？
print(3.0//2.0)
# 1. a < b < c 事实上是等于？
print('a'<'b'<'c',"==(a<b) and (b<c)")
# 2. 不使用 IDLE，你可以轻松说出 5 ** -2 的值吗？
print(5 ** -2)
# 3. 如何简单判断一个数是奇数还是偶数？
# number = input("请输入数字：")
# if(number.isdigit()):
#     if int(number) % 2 ==0:
#         print(number,"是偶数！")
#     else:
#         print(number,"是奇数！")
# 4. 请用最快速度说出答案：not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
# not or and 的优先级是不同的：not > and > or
#
# 我们按照优先级给它们加上括号：(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
# == 0 or 0 or 4 or 6 or 9
# == 4
#
# 为啥是 4？
#
# 大家还记得第四讲作业提到的“短路逻辑”吗？3 and 4 == 4，而 3 or 4 == 3。
# 所以答案是：4

# 5. 还记得我们上节课那个求闰年的作业吗？如果还没有学到“求余”操作，还记得用什么方法可以“委曲求全”代替“%”的功能呢？
print("if year / 4 == int(year / 4)")

# 0. 请写一个程序打印出 0~100 所有的奇数。
number = 100
while (number >= 0):
    if(number % 2 != 0):
        print(number,end='\t')
    number = number - 1
print()
# 1. 我们说过现在的 Python 可以计算很大很大的数据，但是......真正的大数据计算可是要靠刚刚的硬件滴，不妨写一个小代码，让你的计算机为之崩溃？
# print(2 ** 2 ** 32)

# 2. 
# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；
# 若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；
# 若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
# 题目：请编程求解该阶梯至少有多少阶？
number = 0
while not ((number % 2 ==1) and (number % 3 == 2) and (number % 5 == 4) \
           and (number % 6 == 5) and (number % 7 == 0)):
    number = number + 1
print(number)

