# 知识点
# 异常处理
# 捕捉异常可以使用try/except语句。
# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 如果你不想在异常发生时结束你的程序，只需在try里捕获它。
# try语句按照如下方式工作：
# 首先，执行try子句（在关键字try和关键字except之间的语句）
# 如果没有异常发生，忽略except子句，try子句执行后结束。
# 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。
# 如果异常的类型和except之后的名称相符，那么对应的except子句将被执行。
# 最后执行try语句之后的代码。
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
# 实例1（未发生异常）
#
# #!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
try:
    f1 = open("testfile.txt", "w") # 换x抛异常
    f1.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    f1.close()
os.remove('testfile.txt') # 用完清除文件，方便后续测试

# ====输出结果：====
# D:\untitled\venv\Scripts\python.exe D:/untitled/Python_learn/test1.py
# 内容写入文件成功
#
# ===查看testfile.txt文件内容：===
# 这是一个测试文件，用于测试异常!!

# 实例2（发生异常）
#
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# try:
#     f1 = open("testfile.txt", "r")
#     f1.read()
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     f1.close()
#
# ====输出结果：====
# D:\untitled\venv\Scripts\python.exe D:/untitled/Python_learn/test1.py
# Error: 没有找到文件或读取文件失败

# 实例3（发生异常并显示错误代码）
# try:
#     os.remove("testfile.txt")
# except FileNotFoundError:
#     print("不存在该文件！")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# try:
#     f1 = open("testfile.txt", "r")
#     f1.read()
# except IOError as ercode:
#     print("Error: 没有找到文件或读取文件失败,错误代码为：" + str(ercode))
# else:
#     print("内容写入文件成功")
#     f1.close()
#
# ====输出结果：====
# D:\untitled\venv\Scripts\python.exe D:/untitled/Python_learn/test1.py
# Error: 没有找到文件或读取文件失败,错误代码为：
# [Errno 2] No such file or directory: 'testfile.txt'

# 一个try语句包含多个except子句
# 分别来处理不同的特定的异常。最多只有一个分支会被执行。
# 实例4（含有多个except子句）
#
#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    os.remove("testfile.txt")
except FileNotFoundError:
    print("不存在该文件！")
try:
    a = 1/0
    f1 = open("testfile.txt", "r")
    f1.read()
except ZeroDivisionError:
    print('出现错误，原因是：余数不能为0')
except IOError as ercode:
    print("Error: 没有找到文件或读取文件失败,错误代码为：" + str(ercode))
else:
    print("内容写入文件成功")
    f1.close()
f1.close()

#
#
# ====输出结果：====
# D:\untitled\venv\Scripts\python.exe D:/untitled/Python_learn/test1.py
# 出现错误，原因是：余数不能为0

# 一个except带多种异常类型
# 实例5（一个except带多种异常类型）
#
# #一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元祖，
# 例如：
#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    os.remove("testfile.txt")
except FileNotFoundError:
    print("不存在该文件！")
try:
    f1 = open("testfile.txt", "w+")
    f1.read()
    a = 1 / 0
except (IOError,ZeroDivisionError) as ercode:
    print("发生错误了,错误代码为：" + str(ercode))
else:
    print("内容写入文件成功")
    f1.close()
f1.close()
#
# ====输出结果：====
# D:\untitled\venv\Scripts\python.exe D:/untitled/Python_learn/test1.py
# 发生错误了,错误代码为：division by zero

# 使用except而不带任何异常类型
# 实例6（使用except不带异常类型，相当于通配符）
#
# # 这种方式try-except语句捕获所有发生的异常。但这不是一个很好的方式，
# # 我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常。
try:
    os.remove("testfile.txt")
except FileNotFoundError:
    print("不存在该文件！")
#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    f1 = open("testfile.txt", "r")
    f1.read()
    a = 1 / 0
except:
    print('发生错误了')

# ===输出结果===
# D:\untitled\venv\Scripts\python.exe D:/untitled/Python_learn/test1.py
# 发生错误了

# try-finally语句
# try-finally 语句无论是否发生异常都将执行最后的代码。
# 实例7（finally）
#
# !/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    f = open('E:\Pythonclass\Python_intro\我为什么是一个文件.txt','w')
    print(f.write('我存在了!'))
    sum = 1 + '1'
except (OSError,TypeError) as err:
    print('出错了，错误原因是:' + str(err))
#
# ===查看文件内容：===
# 空白
#
# #添加子句finally后：
#
#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    f = open('E:\Pythonclass\Python_intro\我为什么是一个文件.txt','w')
    print(f.write('我存在了!'))
    sum = 1 + '1'
except (OSError,TypeError) as err:
    print('出错了，错误原因是:' + str(err))
finally:
    f.close()
#
# ===输出结果====
# ==================== RESTART: D:\untitled\Python_learn\test1.py =================
# 5       #写入5个字符
# 出错了，错误原因是:unsupported operand type(s) for +: 'int' and 'str'
#
# ===查看文件内容：===
# 我存在了

# raise语句
# raise 语句允许程序员强制抛出一个指定的异常。例如：
#
# >>> raise NameError('未定义的变量')
# Traceback (most recent call last):
#   File "<pyshell#1>", line 1, in <module>
#     raise NameError('未定义的变量')
# NameError: 未定义的变量

# 要抛出的异常由raise的唯一参数标识。它必需是一个异常实例或异常类（继承自Exception的类）。
# 如果你需要明确一个异常是否跑出，但不想处理它，raise语句可以让你很简单的重新抛出该异常：
#
# try:
#     raise NameError('未定义变量')
# except NameError:
#     print('一个异常产生')
#
# ===========输出结果=================
# 一个异常产生

# try:
#     raise NameError('未定义变量')
# except NameError:
#     print('一个异常产生')
#     raise
#
# ===========输出结果=================
# 一个异常产生
# Traceback (most recent call last):
#   File "<pyshell#8>", line 2, in <module>
#     raise NameError('未定义变量')
# NameError: 未定义变量

# 课后习题
# 动动手
#
# 我们使用什么方法来处理程序中出现的异常?
# 使用try ...except搭配来捕获处理程序中出现的异常
#
# try:
#     检测范围
# except Exception[as reason]：
#     出现异常(Exception)后的处理代码

# 一个try语句可以和多个except语句搭配吗？为什么？
# 可以。因为try语句块中可能出现多类异常，利用多个except语句可以分别捕获
# 并处理我们感兴趣的异常。
# try:
#     os.remove('我是一个不存在的文档.txt')
# except FileNotFoundError:
#     None
# try:
#
#     f = open('我是一个不存在的文档.txt')
#     sum = 1 + '1'
#     print(f.read())
#     f.close()
# except OSError as reason:
#     print('文件出错啦T_T\n错误原因是：' + str(reason))
# except TypeError as reason:
#     print('类型出错啦T_T\n错误原因是：' + str(reason))

# 你知道如何统一处理多类异常吗？
# 在except后边使用小括号()把多个需要统一处理的异常括起来：
#
try:
    int('abc')
    sum = 1 + '1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()
except (OSError,NameError,TypeError,ValueError) as reason:
    print('出错啦T_T\n错误原因是：' + str(reason))

# except后边如果不带任何异常类，python会捕获所有（try语句块内）的异常并统一处理，
# 但小甲鱼却不建议这么做，你知道为什么吗？
# 因为它会隐藏所有程序员未想到并且未做好准备处理的错误，
# 例如用户输入ctrl + c试图终止程序会被解释为KeyboardInterrupt异常。
# 如果异常发生在成功打开文件后，Python跳到except语句执行，
# 并没有执行关闭文件的命令（用户写入文件的数据就可能没有保存起来），
# 因此我们需要确保无论如何（就算出了异常退出）文件也要被关闭，我们应该怎么做呢？
# 我们可以使用finally语句来实现，如果try语句块中没有出现任何运行时错误，
# 会跳过except语句块执行finally语句块的内容。
#
# 如果出现异常，则会先执行except语句块的内容再接着执行finally语句块的内容。
# 总之，finally语句块里的内容就是确保无论如何都将被执行的内容！

# 请恢复以下代码中马赛克挡住的内容，使得程序执行后可以按要求输出。
#
# try:
#     for i in range(3):
#         for j in range(3):
#             if i == 2:
#                 raise KeyboardInterrupt
#             print(i, j)
# except KeyboardInterrupt:
#     print('退出啦！')

# 动动手：
#
# 还记得我们第一个小游戏吗？只要用户输入非整形数据，程序立刻就会蹦出不和谐的
# 异常信息然后崩溃。请使用刚学的异常处理方法修改以下程序，提高用户体验。
import random
def game():
    num = random.randint(1,10)
    while True:
        guess = input("请输入你认为的数字：")
        try:
            if int(guess) > int(num):
                print("大了，请重新输入！")
            else:
                if int(guess) < int(num):
                    print("小了，请重新输入！")
                else:
                    print("mua~, 你好聪明呀！")
                    break
        except ValueError:
            print("请输入整数呦！")
# game()
##########################################################
# import random
#
# secret = random.randint(1,10)
# print('------------------我爱鱼C工作室------------------')
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# guess = int(temp)
# while guess != secret:
#     temp = input("哎呀，猜错了，请重新输入吧：")
#     guess = int(temp)
#     if guess == secret:
#         print("我草，你是小甲鱼心里的蛔虫吗？！")
#         print("哼，猜中了也没有奖励！")
#     else:
#         if guess > secret:
#             print("哥，大了大了~~~")
#         else:
#             print("嘿，小了，小了~~~")
# print("游戏结束，不玩啦^_^")

# 答：
#
# import random
#
# secret = random.randint(1,10)
# print('------------------我爱鱼C工作室------------------')
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# try:
#     guess = int(temp)
# except ValueError:
#     print('输入的有误,',end = '')
#     guess = 0
# while guess != secret:
#     temp = input("请重新输入吧：")
#     try:
#         guess = int(temp)
#     except:
#         print('输入的有误,',end='')
#         continue
#     if guess == secret:
#         print("我草，你是小甲鱼心里的蛔虫吗？！")
#         print("哼，猜中了也没有奖励！")
#     else:
#         if guess > secret:
#             print("哥，大了大了~~~")
#         else:
#             print("嘿，小了，小了~~~")
# print("游戏结束，不玩啦^_^")

# input()函数有可能产生两类异常：EOFError（文件末尾endoffile，
# 当用户按下组合键Ctrl + d产生） 和KeyboardInterrupt（取消输入，
# 当用户按下组合键Ctrl +c产生），再次修改上边代码，捕获处理input()的两类异常，
# 提高用户体验。
# import random
#
# secret = random.randint(1,10)
# print('------------------我爱鱼C工作室------------------')
# try:
#     temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
#     guess = int(temp)
# except (KeyboardInterrupt,EOFError,ValueError):
#     print('输入的有误,',end = '')
#     guess = 0
# while guess != secret:
#     try:
#         temp = input("请重新输入吧：")
#         guess = int(temp)
#     except (KeyboardInterrupt,EOFError,ValueError):
#         print('输入的有误,',end='')
#         continue
#     if guess == secret:
#         print("我草，你是小甲鱼心里的蛔虫吗？！")
#         print("哼，猜中了也没有奖励！")
#         break
#     else:
#         if guess > secret:
#             print("哥，大了大了~~~")
#         else:
#             print("嘿，小了，小了~~~")
# print("游戏结束，不玩啦^_^")

# 尝试一个新的函数int_input()，当用户输入整数的时候正常返回，
# 否则提示出错并要求重新输入。
# def int_input(prompt=''):
#     while True:
#         try:
#             print(int(input(prompt)))
#             break
#         except ValueError:
#             print('出错，您输入的不是整数！')
#
# int_input('请输入一个整数：')

# 把文件关闭放在finally语句块中执行还是会出现问题，像下边这个代码，
# 当前文件夹中并不存在My_File。txt这个文件，那么程序执行起来会发生什么事情呢？你有办法解决这个问题吗？
# try:
#     f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
#     print(f.read())
# except OSError as reason:
#     print('出错啦：' + str(reason))
# finally:
#     f.close()
#
# 出错信息：
#
# 出错啦：[Errno 2] No such file or directory: 'My_File.txt'
# Traceback (most recent call last):
#   File "D:\untitled\Python_learn\test1.py", line 7, in <module>
#     f.close()
# NameError: name 'f' is not defined

# 答：
#
try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    if 'f' in locals(): # 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()
