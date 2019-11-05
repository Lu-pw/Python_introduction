print("----内嵌函数和闭包-----")
# 测试题
#
# 0.如果希望在函数中修改全局变量的值，应该使用什么关键字？
# 使用global关键字
number = 1
def num():
    global number
    number = 2
    print(number)
num()
print(number)
2
2
# 1.在嵌套的函数中，如果希望在内部修改外部函数的局部变量，应该使用什么关键字？
# 使用nonlocal关键字
def fun1():
    num = 1
    def fun2():
        nonlocal num
        num = 2
        return num
    return  fun2()

print(fun1())
# 2. Python 的函数可以嵌套，但要注意访问的作用域问题哦，请问以下代码存在什么问题呢？
# def outside():
#     print('I am outside!')
#
#     def inside():
#         print('I am inside!')
# inside()
#使用嵌套函数要注意一点就是作用域问题，inside() 函数是内嵌在 outside() 函数中的，
# 所以 inside() 是人妻，除了身为老公的 outside() 可以碰（调用），
# 在外边或者别的函数体里是无法对其进行调用的。
def outside():
    print('I am outside!')

    def inside():
        print('I am inside!')
    inside()
outside()

# 3. 请问为什么代码 A 没有报错，但代码 B 却报错了？应该如何修改？
# #代码A：
# # def outside():
# #     var = 5
# #
# #     def inside():
# #         var = 3
# #         print(var)
# #
# #     inside()
# #
# # outside()
# # # 代码B：
# # def outside():
# #     var = 5
# #
# #     def inside(): #补充nonlocal var 访问函数外部变量
# #         print(var)
# #         var = 3
# #
# #     inside()
# #
# # outside()
# 仔细一看报错的内容是：UnboundLocalError: local variable 'var' referenced
# before assignment，说的是变量 var 没有被定义就拿来使用，肯定错啦！
# 这里 outside() 函数里有一个 var 变量，但要注意的是，内嵌函数 inside()
# 也有一个同名的变量，Python 为了保护变量的作用域，故将 outside() 的 var
# 变量屏蔽起来，因此此时是无法访问到外层的 var 变量的。

# 4. 请问如何访问 funIn() 呢？
#
def funOut():
    def funIn():
        print('宾果！你成功访问到我啦！')
    return funIn()
# 直接调用
funOut()

# 5. 请问如何访问 funIn() 呢？
# def funOut():
#     def funIn():
#         print('宾果！你成功访问到我啦！')
#     return funIn
# # 使用
# funOut()()
# 6. 以下是“闭包”的一个例子，请你目测下会打印什么内容？
def funX():
    x = 5

    def funY():
        nonlocal x
        x += 1
        return x

    return funY


a = funX()
print(a())
print(a())
print(a())

6
7
8
# 动动手
#
# 0. 请用已学过的知识编写程序，统计下边这个长字符串中各个字符出现的次数
# 并找到小甲鱼送给大家的一句话。
str1 = "jfalkjgdlaskdnvsladnv"
str2 = []
# for i in str1:
# #     if i not in str2:
# #         str2.append(i)
# #         str2.append(str1.count(i))
# # print(str2)
for i in str1:
    if i not in str2:
        if i == '\\n':
            print('\\n',str1.count(i))
        else:
            print(i,":",str1.count(i),end='\t\t')
        str2.append(i)
print()
# 1. 请用已学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码
# ，密码的埋藏点符合以下规律：
# a) 每位密码为单个小写字母Powered by bbs.fishc.com
# b) 每位密码的左右两边均有且只有三个大写字母

str1 = '''ABDaDKSbRIHcRcTHGdDIM'''
str_len = len(str1)
password = ""
for i in range(3,str_len-2):
    if str1[i].islower() and str1[i-3:i].isupper() and \
            str1[i+1:i+4].isupper() and i+3<str_len and\
            (True if i >=4 and (not str1[i-4].isupper()) else (True if(i < 4 ) else False))\
            and (True if i+4 < str_len and (not str1[i+4].isupper()) else(True if i+4>=str_len else False)):
        password += str1[i]
print(password)


# countA = 0  # 统计前边的大写字母
# countB = 0  # 统计小写字母
# countC = 0  # 统计后边的大写字母
# length = len(str1)
#
# for i in range(length):
#     if str1[i] == '\n':
#         continue
#
#     """
#     |如果str1[i]是大写字母：
#     |-- 如果已经出现小写字母：
#     |-- -- 统计后边的大写字母
#     |-- 如果未出现小写字母：
#     |-- -- 清空后边大写字母的统计
#     |-- -- 统计前边的大写字母
#     """
#     if str1[i].isupper():
#         if countB:
#             countC += 1
#         else:
#             countC = 0
#             countA += 1
#
#     """
#     |如果str1[i]是小写字母：
#     |-- 如果小写字母前边不是三个大写字母（不符合条件）：
#     |-- -- 清空所有记录，重新统计
#     |-- 如果小写字母前边是三个大写字母（符合条件）：
#     |-- -- 如果已经存在小写字母：
#     |-- -- -- 清空所有记录，重新统计（出现两个小写字母）
#     |-- -- 如果该小写字母是唯一的：
#     |-- -- -- countB记录出现小写字母，准备开始统计countC
#     """
#     if str1[i].islower():
#         if countA != 3:
#             countA = 0
#             countB = 0
#             countC = 0
#         else:
#             if countB:
#                 countA = 0
#                 countB = 0
#                 countC = 0
#             else:
#                 countB = 1
#                 countC = 0
#                 target = i
#
#     """
#     |如果前边和后边都是三个大写字母：
#     |-- 如果后边第四个字母也是大写字母（不符合条件）：
#     |-- -- 清空记录B和C，重新统计
#     |-- 如果后边仅有三个大写字母（符合所有条件）：
#     |-- -- 打印结果，并清空所有记录，进入下一轮统计
#     """
#     if countA == 3 and countC == 3:
#         if i + 1 != length and str1[i + 1].isupper():
#             countB = 0
#             countC = 0
#         else:
#             print(str1[target], end='')
#             countA = 3
#             countB = 0
#             countC = 0

# 2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# （1）glabal 关键字
#
# 将函数体内部的局部变量变为全局变量。
#
# （2）内嵌函数（内部函数）
#
# 需要注意的是内嵌函数的整个作用域，都在外部函数之内的，也就是说，
# 出了外部函数的范围，是没有办法调用内部函数的。即：
# 假设函数 fun2()的定义和调用的过程都在函数 fun1()内，
# 那么除了在 fun1() 这个函数体里面可以随便调用 fun2()外，出了fun1()，
# 就没有任何可以对fun2(）调用的方式了。
#
# （3）闭包
#
# 闭包是函数式编程重要的语法结构。不同的编程语言实现闭包的形式不同，
# Python中闭包从表现形式上定义为：如果在一个内部函数里，对外部作用域
# （但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包。例如：
#
#
#
# 对于函数FunX()，内部函数为FunY()，内部函数的外部作用域就是
# FunX（）的整个函数空间，的变量就是x，对它进行引用了，达到这个要求了，
# 所以就是内部函数FunY()就是一个闭包。那如何进行调用呢？
#
#
#
# 首先我们发现调用FunX()会得到一个函数，i是函数FunX（）的函数，
# 如果需要得到x*y的值，我们还需要对FunY()进行调用。
#
#
#
# 使用闭包需要注意的是：因为闭包的概念是由内部函数演变而来，
# 所以你也不能在外部函数的外边对内部函数进行调用。在闭包中，
# 外部函数的局部变量对内部函数的局部变量就相当于之前的全局变量之于局部变量的关系。
# 在内部函数中，你只能对外部函数的局部变量进行访问，但你不能对它进行修改。例如：
#
#
#
# 因为这里的 x *= x 中的x被认为是一个局部变量，且没有被定义，
# 所以报错。如果需要在局部使用全局的变量，需要用到nonlocal关键字，
# 这个关键字的使用方法与global相同。


