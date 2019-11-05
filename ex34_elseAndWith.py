# 0.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# 这节课我们来谈谈丰富的else语句及简洁的with语句，大多数编程语言来说，
# else 语句只能跟 if 语句进行搭配，但是在Python里面,else 语句具有更加丰富的
# 功能，在Python中，(1)else语句不仅能够跟 if 语句进行搭配，构成“要么怎么，
# 要么不怎样”的句式,(2)还能跟循环语句（for语句或者while语句）进行搭配，
# 构成“干完了能怎样，干不完就别想怎样”的句式 (3)还能跟异常处理进行搭配，
# 构成“没有问题，那就干吧”的句式。
# 2中，只有循环完成后执行，也就是说只有循环顺利结束才会执行else
# 里面的语句，也就是说，如果循环中使用了break
# 跳出了循环，那么else里面的语句就不会被执行。
# 例如：
#
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d最大的约数是%d" % (num, count))
            break
        count -= 1
    else:
        print("%d是素数" % num)


# num = int(input("请输入一个数："))
# showMaxFactor(num)
# 当输入的数有约数的时候，循环就会break，就输出最大约数，当输入的是素数时，
# 循环就会正常执行完，然后退出循环，输出是素数。
#
# 3中，与异常处理进行搭配，实现与循环语句的实现类似，只要
# try 语句中没有出现任何异常，就会执行 else 语句块里的内容。
#
try:
    print(int("abc"))
except ValueError as reason:
    print("出错啦：" + str(reason))
else:
    print("没有任何异常！")
#
# == == == == == == RESTART: C: / Users / XiangyangDai / Desktop / 上课代码 / 34 - 2.
# 出错啦：invalid
# literal
# for int() with base 10: 'abc'
try:
    print(int("123"))
except ValueError as reason:
     print("出错啦：" + str(reason))
else:
     print("没有任何异常！")
# == == == == == == RESTART: C: / Users / XiangyangDai / Desktop / 上课代码 / 34 - 2.
# py == == == == == ==
# 123
# 没有任何异常！
#
# 接下来是介绍
# with 语句：
#
# 我们可能会觉得打开文件又要关闭文件，然后我们还怕打开的文件会出问题，
# 所以我们又加入了异常处理，所以这样是不是有点烦呢，所以我们的Python提供了
# with 语句，利用这个语句抽象出文件操作中频繁使用 try—exception—finally
# 这样相关的细节，对文件中使用 with 语句可以大大的减少代码量，
# 再也不用担心文件打开的时候忘记关闭了。
#
# with 会自动帮你考虑文件关闭的问题，当你的文件不再需要用到的时候，
# with 语句会自动帮你关闭，那么什么是使用 with 语句呢？
#
try:
    f = open('data.txt', 'w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print("出错啦：" + str(reason))
finally:
    f.close()
#
# 上面的代码显然是存在问题的，这里使用的是read的形式，
# 如果这么文件不存在的时候，那么你这里就试图去关闭一个不存在的文件对象。
# 这里可以使用
# with 语句
#
try:
    with open('data.txt', 'w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print("出错啦：" + str(reason))
#
# 测试题
# 0.
# 在Python中，else语句可以跟哪些语句进行搭配？
# 答：在Python中，else语句不仅能跟 if 语句搭配，构成“要么怎样，要么不怎样”
# 语境；Ta 还能跟循环语句（for 语句或者 while 语句），构成“干完了能怎样，
# 干不完就别想怎样”的语境；其实 else 语句还能够跟我们刚刚讲的异常处理进行搭配，
# 构成“没有问题，那就干吧”的语境。
#
# 1.
# 请问以下例子中，循环中的
# break
# 语句会跳过 else 语句吗？
#
# def showMaxFactor(num):
#     count = num // 2
#     while count > 1:
#         if num % count == 0:
#             print('%d最大的约数是%d' % (num, count))
#             break
#         count -= 1
#     else:
#         print('%d是素数！' % num)
#
#
# num = int(input('请输入一个数：'))
# showMaxFactor(num)
'''答：会，因为如果将 else 语句与循环语句（while 和 for 语句）进行搭配，
那么只有在循环正常执行完成后才会执行 else 语句块的内容。'''
#
# 2.
# 请目测以下代码会打印什么内容？
try:
    print('ABC')
except:
    print('DEF')
else:
    print('GHI')
finally:
    print('JKL')
# 答：只有 except 语句中的内容不被打印，因为
# try 语句块中并没有异常，则 else 语句块也会被执行。
# ABC
# GHI
# JKL
#
# 3.
# 使用什么语句可以使你不比再担心文件打开后却忘了关闭的尴尬？
# 答：使用
# with 语句。
#
# try:
#     with open('data.txt', 'w') as f:
#         for each_line in f:
#             print(each_line)
# except OSError as reason:
#     print('出错啦：' + str(reason))
# 4.
# 使用with 语句固然方便，但如果出现异常的话，文件还会自动正常关闭吗？
# 答：with 语句会自动处理文件的打开和关闭，如果中途出现异常，会执行清理代码，
# 然后确保文件自动关闭。
#
# 5.
# 你可以换一种形式写出下边的伪代码吗？
# with A() as a:
#     with B() as b:
#         suite
# 答：with 语句处理多个项目的时候，可以用逗号隔开写成一条语句
#
# with A() as a, B() as b:
#     suite
# 动动手
# 0.
# 使用with 语句改写以下代码，让 Python 去关心文件的打开与关闭吧。
#
# def file_compare(file1, file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     count = 0  # 统计行数
#     differ = []  # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#     return differ
#
#
# file1 = input('请输入需要比较的头一个文件名：')
# file2 = input('请输入需要比较的另一个文件名：')
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print('两个文件完全一样！')
# else:
#     print('两个文件共有【%d】处不同：' % len(differ))
#     for each in differ:
#         print('第 %d 行不一样' % each)
def file_compare(file1,file2):
    with open(file1,encoding='utf8') as f1:
        with open(file2,encoding='utf8') as f2:
            count = 0
            differ = []
            for line1 in f1:
                line2 = f2.readline()
                count += 1
                if line1 != line2:
                    differ.append(count)
    return differ
# file1 = input("请输入要比较的第一个文件：")
# file2 = input("请输入要比较的第二个文件：")
# differ = file_compare(file1,file2)
# if len(differ) == 0:
#     print("两个文件完全一致！")
# else:
#     print("两个文件共有【%d】处不同"%len(differ))
#     for each in differ:
#         print("第【%d】行不一样"%each)
# 答：使用 with 语句处理文件可以减少需要编写的代码量和粗心的错误。
#
#
# def file_compare(file1, file2):
#     with open(file1) as f1, open(file2) as f2:
#         count = 0  # 统计行数
#         differ = []  # 统计不一样的数量
#
#         for line1 in f1:
#             line2 = f2.readline()
#             count += 1
#             if line1 != line2:
#                 differ.append(count)
#
#     return differ
#
#
# file1 = input('请输入需要比较的头一个文件名：')
# file2 = input('请输入需要比较的另一个文件名：')
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print('两个文件完全一样！')
# else:
#     print('两个文件共有【%d】处不同：' % len(differ))
#     for each in differ:
#         print('第 %d 行不一样' % each)
# 1.
# 你可以利用异常的原理，修改下面的代码使得更高效率的实现吗？
# print('|--- 欢迎进入通讯录程序 ---|')
# print('|--- 1：查询联系人资料  ---|')
# print('|--- 2：插入新的联系人  ---|')
# print('|--- 3：删除已有联系人  ---|')
# print('|--- 4：退出通讯录程序  ---|')
#
# contacts = dict()
#
# while 1:
#     instr = int(input('\n请输入相关的指令代码：'))
#
#     if instr == 1:
#         name = input('请输入联系人姓名：')
#         if name in contacts:
#             print(name + ' : ' + contacts[name])
#         else:
#             print('您输入的姓名不再通讯录中！')
#
#     if instr == 2:
#         name = input('请输入联系人姓名：')
#         if name in contacts:
#             print('您输入的姓名在通讯录中已存在 -->> ', end='')
#             print(name + ' : ' + contacts[name])
#             if input('是否修改用户资料（YES/NO）：') == 'YES':
#                 contacts[name] = input('请输入用户联系电话：')
#         else:
#             contacts[name] = input('请输入用户联系电话：')
#
#     if instr == 3:
#         name = input('请输入联系人姓名：')
#         if name in contacts:
#             del (contacts[name])  # 也可以使用dict.pop()
#         else:
#             print('您输入的联系人不存在。')
#
#     if instr == 4:
#         break
#
# print('|--- 感谢使用通讯录程序 ---|')
################################################################
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:
            print(name + ' : ' + contacts[name])
        except:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:
            print(name + ' : ' + contacts[name])
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        except:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        try:
            del (contacts[name])  # 也可以使用dict.pop()
        except:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')
# 答：使用条件语句的代码非常直观明了，但是效率不高。因为程序会两次访问字典的键，一次判断是否存在（例如 if name in contacts），一次获得值（例如
# print(name + ' : ' + contacts[name])）。
#
# 如果利用异常解决方案，我们可以简单避开每次需要使用 in 判断是否键存在字典中的操作。因为只要当键不存在字典中时，会触发
# KeyError
# 异常，利用此特性我们可以修改代码如下：
#
# print('|--- 欢迎进入通讯录程序 ---|')
# print('|--- 1：查询联系人资料  ---|')
# print('|--- 2：插入新的联系人  ---|')
# print('|--- 3：删除已有联系人  ---|')
# print('|--- 4：退出通讯录程序  ---|')
#
# contacts = dict()
#
# while 1:
#     instr = int(input('\n请输入相关的指令代码：'))
#
#     if instr == 1:
#         name = input('请输入联系人姓名：')
#         try:
#             print(name + ' : ' + contacts[name])
#         except KeyError:
#             print('您输入的姓名不再通讯录中！')
#
#     if instr == 2:
#         name = input('请输入联系人姓名：')
#         try:
#             contacts[name]  # 有点“为赋新词强说愁”的感觉
#             print('您输入的姓名在通讯录中已存在 -->> ', end='')
#             print(name + ' : ' + contacts[name])
#             if input('是否修改用户资料（YES/NO）：') == 'YES':
#                 contacts[name] = input('请输入用户联系电话：')
#         except KeyError:
#             contacts[name] = input('请输入用户联系电话：')
#
#     if instr == 3:
#         name = input('请输入联系人姓名：')
#         try:
#             del (contacts[name])  # 也可以使用dict.pop()
#         except KeyError:
#             print('您输入的联系人不存在。')
#
#     if instr == 4:
#         break
#
# print('|--- 感谢使用通讯录程序 ---|')
