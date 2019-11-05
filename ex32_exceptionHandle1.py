# 0. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！                                               
#       Python标准异常总结
# AssertionError	断言语句（assert）失败
# AttributeError	尝试访问未知的对象属性
# EOFError	        用户输入文件末尾标志EOF（Ctrl+d）
# FloatingPointError	浮点计算错误
# GeneratorExit	generator.close()方法被调用的时候
# ImportError	导入模块失败的时候
# IndexError	索引超出序列的范围
# KeyError	字典中查找一个不存在的关键字
# KeyboardInterrupt	用户输入中断键（Ctrl+c）
# MemoryError	内存溢出（可通过删除对象释放内存）
# NameError	尝试访问一个不存在的变量
# NotImplementedError	尚未实现的方法
# OSError	操作系统产生的异常（例如打开一个不存在的文件）
# OverflowError	数值运算超出最大限制
# ReferenceError	弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
# RuntimeError	一般的运行时错误
# StopIteration	迭代器没有更多的值
# SyntaxError	Python的语法错误
# IndentationError	缩进错误
# TabError	Tab和空格混合使用
# SystemError	Python编译器系统错误
# SystemExit	Python编译器进程被关闭
# TypeError	不同类型间的无效操作
# UnboundLocalError	访问一个未初始化的本地变量（NameError的子类）
# UnicodeError	Unicode相关的错误（ValueError的子类）
# UnicodeEncodeError	Unicode编码时的错误（UnicodeError的子类）
# UnicodeDecodeError	Unicode解码时的错误（UnicodeError的子类）
# UnicodeTranslateError	Unicode转换时的错误（UnicodeError的子类）
# ValueError	传入无效的参数
# ZeroDivisionError	除数为零
#  
#
# 0. 结合你自身的编程经验，总结下异常处理机制的重要性？-
# 答：由于环境的不确定性和用户操作的不可以预知性都可能导致程序出现各种问题，
# 因此异常机制最重要的无非就是：增强程序的健壮性和用户体验，
# 尽可能的捕获所有预知的异常并写好处理的代码，当异常出现的时候，
# 程序自动消化并恢复正常（不至于崩溃）。
# 以下题目可以参考（http://bbs.fishc.com/thread-45814-1-1.html），
# 但要求不使用IDLE直接获得答案。
#
# 1. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：
# >>> my_list = [1, 2, 3, 4,,]
#
# 答：语法错误版权属于：
# SyntaxError: invalid syntax^
#
# 2. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：
# >>> my_list = [1, 2, 3, 4, 5]
# >>> print(my_list[len(my_list)])
#
# 答：len(my_list) 是获得列表的长度，这里长度为5，
# 该列表各个元素的访问索引号分别是：[0, 1, 2, 3, 4]，
# 因此试图访问 my_list(5) 会引发 IndexError: list index out of range 异常。
#
# 3. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：
# >>> my_list = [3, 5, 1, 4, 2]
# >>> my_list.sorted()
#
# 答：初学者容易疏忽的错误，列表的排序方法叫 list.sort()，sorted() 是BIF。
# 因此会引发 AttributeError: 'list' object has no attribute 'sorted' 异常。
#
# 4. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：
# >>> my_dict = {'host': 'http://bbs.fishc.com', 'port': '80'}
# >>> print(my_dict['server'])
#
# 答：尝试访问字典中一个不存在的“键”引发 KeyError: 'server' 异常，
# 为了避免这个异常发生，可以使用 dict.get() 方法：
# if not my_dict.get('server'):
#
#         print('您所访问的键【server】不存在！')
#
# 5. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：
# def my_fun(x, y):
#     print(x, y)
#
# my_fun(x=1,2)
#
# 答：如果使用关键字参数的话，需要两个参数均使用关键字参数 my_fun(x=1, y=2)
#
# 6. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：GJS{F
# f = open('C:\\test.txt', wb)
# f.write('I love FishC.com!\n')
#
# f.close()
#
# 答：注意 open() 第二个参数是字符串，应该 f = open('C:\\test.txt', 'wb')。
# wb不加双引号 Python 还以为是变量名呢，往上一找，艾玛没找着……
# 引发 NameError 异常。由于打开文件失败，接着下边一连串与 f 相关的
# 均会报同样异常。
#
# 7. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：
# def my_fun1():
#         x = 5
#         def my_fun2():
#                 x *= x
#                 return x
#         return my_fun2()
# my_fun1()
#
# 答：闭包的知识大家还记得不？ Python 认为在内部函数的 x 是局部变量的时候，
# 外部函数的 x 就被屏蔽了起来，所以执行 x *= x 的时候，
# 在右边根本就找不到局部变量 x 的值，因此报错。

# 在 Python3 之前没有直接的解决方案，只能间接地通过容器类型来存放，
# 因为容器类型不是放在栈里，所以不会被“屏蔽”掉。
# 容器类型这个词儿大家是不是似曾相识？我们之前介绍的字符串、列表、元祖，
# 这些啥都可以往里的扔的就是容器类型啦。
# 于是乎我们可以把代码改造为：
# def my_fun1():
#         x = [5]
#         def my_fun2():
#                 x[0] *= x[0]
#                 return x[0]
#         return my_fun2()
# my_fun1()
#
# 但是到了 Python3 的世界里，又有了不少的改进，如果我们希望在内部函数里
# 可以修改外部函数里的局部变量的值，那么也有一个关键字可以使用，
# 就是 nonlocal：
# def my_fun1():
#         x = 5
#         def my_fun2():
#                 nonlocal x
#                 x *= x
#                 return x
#         return my_fun2()
# my_fun1()
