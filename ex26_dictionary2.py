# 0.
# Python的字典是否支持一键（Key）多值（Value）？
#  
# 答：不支持，对相同的键再次赋值会将上一次的值直接覆盖。
dict1 = {'one':1,'one' : 2} #会覆盖
# dict1 = dict(one = 1,one = 2) #会提示重复
print(dict1['one'])
# 1.
# 在字典中，如果试图为一个不存在的键（Key）赋值会怎样？
# 答：会自动创建对应的键（Key）并添加相应的值（Value）进去。
# （具体原理可以参考第3题的“扩展阅读”部分）
#
# 2.
# 成员资格操作符（in和not in）可以检查一个元素是否存在序列中，
# 当然也可以用来检查一个键（Key）是否存在字典中，那么请问哪种的
# 检查效率更高些？为什么？
# 答：在字典中检查键（Key）是否存在比在序列中检查指定元素是否存在更高效。
# 因为字典的原理是使用哈希算法存储，一步到位，不需要使用查找算法进行匹配，
# 因此时间复杂度是O（1），效率非常高。（关于如何使用哈希算法存储的
# 具体原理可以参考第3题的“扩展阅读”部分）
#
# 3.
# Python对键（Key）和值（Value）有没有类型限制？
# 答：Python对键的要求相对要严格一些，要求它们必须是可哈希（Hash）的对象，
# 不能是可变类型（包括变量、列表、字典本身等）。
#
# 但是Python对值是没有任何限制的，它们可以是任意的Python对象。
# 如果不清楚哈希原理以及字典的存放原理的童鞋，推荐阅读下小甲鱼
# 帮你整理的这篇文章：你知道Python的字典（Dict）是如何存储的吗？
'''http: // bbs.fishc.com / thread - 45016 - 1 - 1.html'''
#
# 4.
# 请目测下边代码执行后，字典dict1的内容是什么？
dict2 = {}
dict2 = dict2.fromkeys((1, 2, 3), ('one', 'two', 'three'))
print(dict2[3])
dict2 = dict2.fromkeys((1, 3), '数字')
print(dict2[3])
# 答：执行完成后，字典dict1的内容是：{1: '数字', 3: '数字'}
# 这里要注意的是，fromkeys方法是直接创建一个新的字典，
# 不要试图使用它来修改一个原有的字典，因为它会直接无情的用把整个字典给覆盖掉。
#
# 5.
# 如果你需要将字典dict1 = {1: 'one', 2: 'two', 3: 'three'}
# 拷贝到dict2，你应该怎么做？
# 答：可以利用字典的copy()
# 方法：dict2 = dict1.copy()，在其他语言转移到Python小伙伴们刚开始可能
# 会习惯性的直接用赋值的方法（dict2 = dict1），这样子做在Python中只是
# 将对象的引用拷贝过去而已。
#(=类似于贴标签)
# 看一下区别：
#
a = {1: 'one', 2: 'two', 3: 'three'}
b = a.copy()
c = a
c[4] = 'four'
print(c)
print(a)
print(b)
# c
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# a
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#b
# {1: 'one', 2: 'two', 3: 'three'}
# 动动手
# 0.
# 尝试编写一个用户登录程序（这次尝试将功能封装成函数），程序实现如图：
#

users = {}
def display():
    print("|--- 新建用户:N/n ---|\n|--- 登录账号:E/e ---|\n|--- "
          "退出程序:Q/q ---|")
def creat():
    name = input("请输入用户名：")
    if name in users:
        name = input("此用户已存在，请重新输入：")
    else:
        users[name] = input("请输入密码：")
    print("注册成功，赶紧试试登录吧！")
def login():
    name = input("请输入用户名：")
    if name in users:
        password = input("请输入密码：")
        while users[name] != password:
            password = input("密码错误，请重新输入：")
        print("欢迎进入XXOO系统，请点击右上角X结束！")

while 1:
    display()
    str = input("|--- 请输入指令代码 ---|")
    if(str.lower() == 'n'):
        creat()
        print()
    if(str.lower() == 'e'):
        login()
        print()
    if(str.lower() == 'q'):
        break
print("系统已退出，期待您的再次访问！")


#
# user_data = {}
#
#
# def new_user():
#     prompt = '请输入用户名：'
#     while True:
#         name = input(prompt)
#         if name in user_data:
#             prompt = '此用户名已经被使用，请重新输入：'
#             continue
#         else:
#             break
#
#     passwd = input('请输入密码：')
#     user_data[name] = passwd
#     print('注册成功，赶紧试试登录吧^_^')
#
#
# def old_user():
#     prompt = '请输入用户名：'
#     while True:
#         name = input(prompt)
#         if name not in user_data:
#             prompt = '您输入的用户名不存在，请重新输入：'
#             continue
#         else:
#             break
#
#     passwd = input('请输入密码：')
#     pwd = user_data.get(name)
#     if passwd == pwd:
#         print('欢迎进入XXOO系统，请点右上角的X结束程序！')
#     else:
#         print('密码错误！')
#
#
# def showmenu():
#     prompt = '''
# |--- 新建用户：N/n ---|
# |--- 登录账号：E/e ---|
# |--- 推出程序：Q/q ---|
# |--- 请输入指令代码：'''
#
#     while True:
#         chosen = False
#         while not chosen:
#             choice = input(prompt)
#             if choice not in 'NnEeQq':
#                 print('您输入的指令代码错误，请重新输入：')
#             else:
#                 chosen = True
#
#         if choice == 'q' or choice == 'Q':
#             break
#         if choice == 'n' or choice == 'N':
#             new_user()
#         if choice == 'e' or choice == 'E':
#             old_user()
#
#
# showmenu()
#
# 1.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# 比序列更加使用的映射类型，Python唯一的一个映射类型就是字典，
# 字典也有一个关键符号，就是大括号，跟序列一样，也可以用dict()
# 这个工厂函数来创建一个字典，跟序列不一样的是，如果在序列中试图为一个
# 不存在的位置去赋值的时候，会报错，会提示该位置并不存在，但如果在字典中，
# 它会自动创建相应的键并添加对应的值。
#
# dict()
# 是一个工厂函数，实际上是一个类型，调用它会生成一个该类型的实例，
# 此前我们学习了str()，int()，list()，tuple()，这些都是工厂函数（类型），
# 不过在学习类和对象之前，你可以把它们当做普通函数来理解。
#
# 1、下面介绍字典的内建方法
#
# fromkeys(....)
#
# 用法：dict.fromkeys(S[, v]) -> New
# dict
# with keys from S and values equal to v(v default to None).
#
# 你可以用fromkeys(....)
# 方法创建并返回新的字典，第一个参数S是字典的键值，
# 第二个参数v是可选的键值对应的值，如果第二个参数不提供的话，就是None。
#
dict1 = dict.fromkeys((1, 2, 3))
print(dict1)
# {1: None, 2: None, 3: None}
#dict1
# {}
#
# dict1.fromkeys（）只是创建新的字典，对原数组无影响，和下面的代码是一样的：
#
# dict.fromkeys((1, 2, 3))
# {1: None, 2: None, 3: None}
#
# 如果给键对应的值的话：
#
#dict.fromkeys((1, 2, 3), 'number')
# {1: 'number', 2: 'number', 3: 'number'}
#
'''但是不要指望分别给键对应的值：'''
#
#dict.fromkeys((1, 2, 3), ('one', 'two', 'three'))
# {1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'),
# 3: ('one', 'two', 'three')}
#
# 2、下面介绍访问字典的几个方法
#
# keys()、values()、items()
#
# keys()
# 返回字典键的引用，values()
# 返回字典值的引用，items()
# 返回字典项的引用
#
dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(dict1.keys())
# dict_keys([1, 2, 3, 4, 5])
#dict1.values()
# dict_values(['one', 'two', 'three', 'four', 'five'])
#dict1.items()
# dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), 
# (5, 'five')])
#
#for eachkey in dict1.keys():
#         print(eachkey, end=' ')
#
#     
# 1
# 2
# 3
# 4
# 5 
#
#for eachvalue in dict1.values():
#         print(eachvalue, end=' ')
#
#     
# one
# two
# three
# four
# five 
#
#for eachitem in dict1.items():
#         print(eachitem, end=' ')
#
#     
# (1, 'one')(2, 'two')(3, 'three')(4, 'four')(5, 'five') 
#
# 当我们试图访问字典中不存在的项时，就可能会报错：
#
#dict1
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
#dict1[6]
# Traceback(most recent call last):   File "<pyshell#56>", line 1,
# in < module >     dict1[6] KeyError: 6
# 这样的用户体验就会不好。
#
# 因此使用get() 内建函数。
#
# dict1.get(5)
# 'five'
# dict1.get(6)
#print(dict1.get(6))
# None
#
# 也可以在get中为不存在的项输出相应的提示：
#
#dict1.get(6, '不存在')
# '不存在'
#dict1.get(5,  '不存在')
# 'five'
#dict1
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
#
# 如果不知道一个键是否在字典中（不能查找值），可以使用成员资格操作符来进行判断。 in 和 not in
#
#6 in dict1
# False
#5 in dict1
# True
#'five' in dict1
# False
#
# 清空一个字典，使用clear()
# 方法。
#
#dict1
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
#dict1.clear()
#dict1
# {}
#
# clear()
# 会完全清除整个字典，即使该字典有多个名字对应：
#
#a = {1: 'one'}
#b = a
#b
# {1: 'one'}
#a.clear()
#a
# {}
#b
# {}
#
# copy()
# 拷贝，区别于赋值：
#a = {1: 'one', 2: 'two', 3: 'three'}
#b = a.copy()
#c = a
#a
# {1: 'one', 2: 'two', 3: 'three'}
#b
# {1: 'one', 2: 'two', 3: 'three'}
#c
# {1: 'one', 2: 'two', 3: 'three'}
#id(a)                                    id()
# 返回地址，可以发现c和a指向同一个字典
# 2200132871048
#id(b)
# 2200132857800
#id(c)
# 2200132871048
#c[4] = 'four'
#a
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#b
# {1: 'one', 2: 'two', 3: 'three'}
#c
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#
# pop() 和popitem()，都是弹出字典中的元素。
#
#a = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#a.pop(2)
# 'two'
#a
# {1: 'one', 3: 'three', 4: 'four'}
#a = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#a.popitem()
# (1, 'one')
#a
# {2: 'two', 3: 'three', 4: 'four'}
#
# pop() 是弹出对应键的项，返回键对应的值，
# popitem() 是随机从字典弹出项，返回键和值的元组。
#
# setdefault() 用法与get() 类似，只是如果找不到对应的键，会自动添加，
# 值默认为None，也可以给值。
#
a = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
a.setdefault(2)
# 'two'
a.setdefault(5)
print(a)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: None}
a.setdefault(5, 'five') #如果找到了，给的值也不生效
print(a)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: None}
a.setdefault(6, 'six')
print(a)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: None, 6: 'six'}

# update()，用一个字典或映射关系去更新一个字典。
#
a = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: None, 6: 'six'}
b = {2: 'double'}
a.update(b)
print(a)