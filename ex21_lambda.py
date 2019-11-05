print("---lambda表达式---")
# 测试题
# 0.
# 请使用lambda表达式将下边函数转变为匿名函数？
#
def fun_A(x, y=3):
    return x * y

lambda x,y = 3 : x * y

# 1.
# 请将下边的匿名函数转变为普通的屌丝函数？
# lambda x: x if x % 2 else None
def is_odd(x):
    if x % 2:
        return x
    else:
        return None
#
#
# 2.
# 感受一下使用匿名函数后给你的编程生活带来的变化？
# a. Python写一些执行脚本时，使用匿名函数就可以省下定义函数过程，
# 比如说我们只是需要写个简单的脚本来管理服务器时间，
# 我们就不需要专门定义一个函数然后再写调用，
# 使用匿名函数就可以使得代码更加精简。
#
# b. 对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，
# 有时候给函数起个名字也是比较头疼的问题，
# 使用匿名函数就不需要考虑命名的问题了。
#
# c.简化代码的可读性，由于普通的屌丝函数阅读经常要跳到开头def定义部分，
# 使用匿名函数函数可以省去这样的步骤。
#
#
# 3.
# 你可以利用filter()
# 和lambda表达式快速求出100以内所有3的倍数吗？
a = list(filter(lambda x: not(x % 3), range(1,100)))
print(a)
# 4.
# 还记得列表推导式吗？完全可以使用列表推导式代替filter()
# 和lambda组合，你可以做到吗？
# 例如将第3题转为列表推导式即：
a = list(x  for x in range(1,100) if not(x % 3))
print(a)
#
# [i for i in range(1, 100) if not (i % 3)]
# 5.
# 还记得zip吗？使用zip会将两数以元祖的形式绑定在一块，例如：
# >> > list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# 但如果我希望打包的形式是灵活多变的列表而不是元祖
# （希望是[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# 这种形式），你能做到吗？（采用map和lambda表达式）
print(list(map(lambda x,y:[x,y],[1,3,5,7,8],[2,4,6,8,10])))
# 注意：强大的map()
# 后边是可以接受多个序列作为参数的。
#
# 6.
# 请目测以下表达式会打印什么？
#
def make_repeat(n):
    return lambda s: s * n


double = make_repeat(2)
print(double(8))
print(double('FishC'))
# 会打印：
# 16
# FishCFishC
#
# 7.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# 这节课只要来讨论一下lambda表达式，Python允许使用lambda表达式创建匿名函数，
# 那什么是匿名函数呢？
#
# Python的lambda语句是非常精简的，基本的语法就是
'''在冒号的前面是原函数的参数， 而在冒号的后边是原函数的返回值。'''
# lambda语句实际上是构建了一个函数对象，
# 如果要对它进行使用，只需要简单的赋值即可。
#
# lambda语句构建的函数的参数也可以是多个的
#
# （2）lambda表达式的作用
#
# Python写一些执行脚本时，使用lambda就可以省下定义函数的过程，
# 比如说我们只是需要写个简单的脚本来管理服务器时间，
# 我们就不需要专门定义一个函数然后再写调用，
# 使用lambda就可以使得代码更加精简。
#
# 对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，
# 有时候给函数起个名字也是比较头痛的问题，使用lambda就不需要考虑命名的问题了。
#
# 简化代码的可读性，由于普通的屌丝函数阅读经常要跳到开头def定义部分，
# 使用lambda函数可以省去这样的步骤。
#
# （3）两个牛逼的BIF
#
# filter()
#
# 用法：filter(function or None,
#           iterable)，有两个参数，第二个参数为可迭代的数据，
#           第一个参数可以为None或者函数，当为None时，
#           将iterable中为真的数据挑选出来，当为function时
#           ，将iterable中满足function的结果为真的数据挑选出来。
#
# filter(None, [1, 0, False, True])
#            <filter object at 0x00000261C2E3C0B8>
#  list( filter(None, [1, 0, False, True]))
#            [1, True]

# 下面写一个挑选出奇数的代码：
print(list(filter(lambda x: x % 2,range(1,10))))
#
# 用lambda实现：
#
a = list(x for x in range(10) if x % 2 )
print(a)
#
# map()
# 用法：map(func, *iterables)，将可迭代序列的每一个数据作为函数
# 的参数进行运算加工，直到可迭代序列的每一个元素都加工完毕，
# 返回所有加工后的元素构成的新序列。
print(list(map(lambda x,y:[x,y],[1,3,5,7,9,11],[2,4,6,8,10])))
