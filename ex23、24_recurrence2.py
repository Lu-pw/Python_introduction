# 0.
# 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，
# 结果与调用bin()一样返回字符串形式）。
def Dec2Bin(x):
    if x:
        return x % 2 + Dec2Bin(x//2) * 10
    else:
        return 0
print(Dec2Bin(62))


# def Dec2Bin(dec):
#     result = ''
#
#     if dec:
#         result = Dec2Bin(dec // 2)
#         return result + str(dec % 2)
#     else:
#         return result
#
#
# print(Dec2Bin(62))
# 1.
# 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。
list1 = []
def get_digits(n):
    if n:
        list1.append(n%10)
        return get_digits(n//10)
    else:
        list1.reverse()
        print(list1)
get_digits(12345)

result = []


# def get_digits(n):
#     if n > 0:
#         result.insert(0, n % 10)
#         get_digits(n // 10)
#
#
# get_digits(12345)
# print(result)
# 2.
# 还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能骄傲的说我可以吗？
# str1 = input("请输入字符串")
# def couplet(n=0):
#     if n < len(str1) // 2:
#         if str1[n] != str1[-n-1]:
#             print(str1,"不是回文数")
#             return
#         else:
#             return couplet(n+1)
#     else:
#         print(str1,"是回文联")
# couplet()


# def is_palindrome(n, start, end):
#     if start > end:
#         return 1
#     else:
#         return is_palindrome(n, start + 1, end - 1)\
#             if n[start] == n[end] else 0
#
#
# string = input('请输入一串字符串：')
# length = len(string) - 1
#
# if is_palindrome(string, 0, length):
#     print('"%s"是回文字符串!' % string)
# else:
#     print('"%s"不是回文字符串!' % string)

# 3.
# 使用递归编程求解以下问题：
def year(n):
    if (n-1):
        return year(n-1) + 2
    else:
        return 10
print(year(5))


# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return age(n-1) + 2

# 4.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# （1）斐波那契数列的递归实现：
#
# 1，1，2，3，5，8，13，21.....
#
# 我们可以用数学函数来定义：
def num(x = 1,y = 1): # 范围
    if x < 100:
        print(x,end=' ')
        return num(y,x + y)
    else:
        print()
num()

# 分别用迭代和递归实现：
#
# 迭代
#
#
# def fab(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#     if n < 1:
#         print("输入错误！")
#         return -1
#     while (n - 2) > 0:
#         print(n1, end=' ')
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
# fab(10)
#
#
# 递归：
#
# def fab(n):
#     if n < 1:
#         print('输入有误！')
#         return -1
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return ferber(n - 1) + ferber(n - 2)
#
#
# 递归算法称为分治思想。
#
# （2）递归实现汉诺塔
#
# 对于游戏的玩法，我们可以简单分解为三个步骤：
#
# 将前63个盘子从a移到b上
#
# 将最底下的第64个盘子从a移到c
#
# 将b上的63个盘子移到c
#
# 问题1：将a上的63个盘子借助c移到b
#
# 问题2：将b上的63个盘子借助a移到c
#
# 然后：
#
# 问题1拆解为：
#
#         将前62个盘子从a移到c上
#
#         将最底下的第63个盘子从a移到b
#
#         将c上的62个盘子移到b
#
# 问题2拆解为：
#
#         将前62个盘子从b移到a上
#
#         将最底下的第63个盘子从b移到c
#
#         将a上的62个盘子移到b
#
def hanoi(n,a,b,c):
    'n为盘子数，a，b，c，为三根柱子'
    if n==1:
        print(a,'->',c)
    else:
        hanoi(n-1,a,c,b) # 将前n-1个盘子从a 移到b
        print(a,'->',c) #将最底下最后一个盘子从a移到c
        hanoi(n-1,b,a,c) #将b上的n-1个盘子移到c上

hanoi(2,'a','b','c')
print("---------------")
hanoi(3,'a','b','c')
# 动动手
# 0.
# 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()
# 一样返回字符串形式）。
#
# def Dec2Bin(dec):
#     result = ''
#
#     if dec:
#         result = Dec2Bin(dec // 2)
#         return result + str(dec % 2)
#     else:
#         return result
#
#
# print(Dec2Bin(62))
# 1.
# 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。
# 举例：get_digits(12345) == > [1, 2, 3, 4, 5]
#
# 解题思路：利用除以10取余数的方式，每次调用get_digits(n // 10)，并将余数存放到列表中即可。要注意的是结束条件设置正确。
#
# result = []
#
#
# def get_digits(n):
#     if n > 0:
#         result.insert(0, n % 10)
#         get_digits(n // 10)
#
#
# get_digits(12345)
# print(result)
# 2.
# 还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能骄傲的说我可以吗？
# 解题思路：有好多种方法，不过综合效率来说，小甲鱼的实现方式比较朴素，利用递归每次索引前后两个字符进行对比，当start > end的时候，也正是首尾下标“碰面”的时候，即作为结束递归的条件。
#
# def is_palindrome(n, start, end):
#     if start > end:
#         return 1
#     else:
#         return is_palindrome(n, start + 1, end - 1) if n[start] == n[end] else 0
#
#
# string = input('请输入一串字符串：')
# length = len(string) - 1
#
# if is_palindrome(string, 0, length):
#     print('"%s"是回文字符串!' % string)
# else:
#     print('"%s"不是回文字符串!' % string)
# 3.
# 使用递归编程求解以下问题：
# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
#
# 解题思路：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10
# 岁），再往回推。
#
# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return age(n - 1) + 2
#
#
# print('哈哈，我知道了，第五个人的年龄是 %d 岁，啵啵脆！' % age(5))
