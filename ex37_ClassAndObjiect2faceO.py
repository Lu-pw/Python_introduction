# '''这段代码是觉得文件名太长，把excercise替换为ex'''
# # import os
# # import easygui as g
# #
# # path = input("请输入要重命名文件的文件夹：")
# # for each in os.listdir(path):
# #     file_name = os.path.basename(each)
# #     if os.path.splitext(file_name)[0][:9] == 'excercise':
# #         if os.path.splitext(file_name)[1] == '.py':
# #             with open(file_name,encoding='utf8') as f:
# #                 new_name = "ex" + file_name[9:]
# #                 new_file = open(new_name,'w',encoding='utf8')
# #                 new_file.write(f.read())
# #                 new_file.close()
# #             os.remove(file_name)
# 
# ####################面向对象##############################
# 0.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# 经过上一节课的热身，相信大家对类和对象已经有了初步的认识。这节课通过
# 几个主题来理解，面向对象编程。
# 
# （一）self是什么？
# Python的self相当于C + + 的this指针。我们知道，类是图纸，而由类实例化出的
# 对象才是真正可以住人的房子，这是我们上节课大的比方。我们还知道，根据
# 一张图纸就可以设计出成千上万的房子，这些房子都长得差不多，因为它们
# 都来自于同一张图纸，但是它们都有不同的主人，每个人都只可以回到自己的家，
# self就相当于每个房子的门牌号，有了self，就可以轻松的找到自己的房子，Python
# 的self参数就是同样的道理，由同一个类可以生成无数个对象，这些对象都长得
# 很相似，因为它们都是来源于同一个类的属性和方法，当一个对象的方法被调用
# 的时候，对象会将自身作为第一个参数传给self参数，接收到这个self参数的时候，
# Python就知道你是哪一个对象在调用方法了。举例说明：


class Ball:
    def setName(self, name):
        self.name = name

    def kick(self):
        print("我叫%s，该死的，谁踢我..." % self.name)


a = Ball()
a.setName("球A")
b = Ball()
b.setName("球B")
a.kick()
# 我叫球A，该死的，谁踢我...
b.kick()
# 我叫球B，该死的，谁踢我...
# 我们发现，在对象类定义这里，它的这些方法都有一个self，我们生成两个实例化对象
# a和b，这里都调用kick()方法，但是实现结果不一样，是因为a.kick()和b.kick()
# 都有一个隐藏属性self，会找到各自对应的name，这些都是由Python在背后默默的
# 工作，你只需要在类的定义的时候把self写进第一个参数。
# 
# （二）Python的魔法方法
# 你听说过Python的魔法方法吗？据说，Python的对象天生拥有一些神奇的方法，
# 它们是面向对象的Python的一切......它们是可以给你的类增加魔力的特殊方法......
# 如果你的对象实现了这些方法中的某一个，那么这个方法在特殊情况下被Python
# 所调用，而这一切都是自动发生的......Python的这些具有魔力的方法总是会
# 被双下划线所包围，我们今天介绍其中一个最基础的特殊方法：__init__(self)
# 
# 对于Python的其它的魔法方法，我们后面会专门进行讲解。我们把__init__(self)
# 方法称为构造方法，__init__(self)方法的魔力体现在只要实例化一个对象的时候，
# 那么这个方法就会在对象被创建的时候自动调用。有过C + +基础的同学就会知道，
# 这就是构造函数。
# 
# 其实实例化对象的时候是可以存入参数的，这些参数会自动的存入到__init__(self)
# 方法中，
# 
# __init__(self，param1，param2...) # (默认不重写的形式就是__init__(self))
# 
# 也就是我们这个魔法方法中，我们可以通过重写这个方法（如上）来自定义对象的
# 初始化操作，说起来比较复杂，举例说明：


class Ball:
    def __init__(self, name):
        self.name = name

    def kick(self):
        print("我叫%s，该死的，谁踢我..." % self.name)


a = Ball("土豆")  # 因为重写了__init__(self)方法，实例化对象时需要一个参数
a.kick()
# 我叫土豆，该死的，谁踢我...
#b = Ball()  # 这里没有传入参数就会报错，可以在定义类是给name设置默认参数
# Traceback(most recent call last):
# File "<pyshell#84>", line 1, in < module > b = Ball()
# TypeError: __init__() missing 1 required positional argument: 'name'
# （三）公有和私有
# 
# 默认上来说，对象的属性和方法都是公开的，都是共有的，我们可以通过点（.）
# 操作符来进行访问，举例说明：
# 
class Person:
    name = "人生苦短，我用Python3"

p = Person()
print(p.name)
# '人生苦短，我用Python3'
# 为了实现类似于私有变量的特征，Python内部采用了一种叫做namemangling
# （名字改编，名字重整）的技术，在Python中定义私有变量只主要在变量名或函数名
# 前加上“__”两个下划线，那么这个函数或变量就会为私有的了。
# 
# >> >
# 
# class Person:
#     __name = "来自江南的你"
# 
#p = Person()
#p.__name
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#94>", line
# 1, in < module >
# p.__name
# AttributeError: 'Person'
# object
# has
# no
# attribute
# '__name'
#p.name
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#95>", line
# 1, in < module >
# p.name
# AttributeError: 'Person'
# object
# has
# no
# attribute
# 'name'
# 这时，p.__name
# 和
# p.name
# 都无法访问对象的name属性，因为它们都找不到了，这样在外部就会将变量名隐藏起来，理论上如果要访问，就要从内部进行，可以这样写：
# 
# >> >
# 
# class Person:
#     __name = "来自江南的你"
# 
#     def getName(self):
#         return self.__name
# 
#p = Person()
#p.getName()
# '来自江南的你'
# 上面的方法只是理论上的，其实只要你琢磨一下，name
# mangling
# 技术的意思就是名字改编、名字重整，那么应该不难发现，Python只是动了一下手脚，它把双下划线开头的变量改了名字而已，它自动是改成了  _类名__变量名（单下划线 + 类名 + 双下划线 + 变量名），如下 ：
# 
# >> >
# 
# class Person:
#     __name = "来自江南的你"
# 
#p = Person()
#p._Person__name
# '来自江南的你'
#  所以说，Python的私有机制是伪私有，Python是没有权限控制的，所以变量是可以被外部调用的。
# 
# 测试题
# 0.
# 以下代码体现了面向对象编程的什么特征？
#"FishC.com".count('o')
# 1
#[1, 1, 2, 3, 5, 8].count(1)
# 2
#(0, 2, 4, 8, 12, 18).count(1)
# 0
# 答：体现了面向对象编程的多态特征。
# 
# 1.
# 当程序员不想把同一段代码写几次，他们发明了函数解决了这种情况。当程序员已经有了一个类，而又想建立一个非常相近的新类，他们会怎么做呢？
# 答：他们会定义一个新类继承已有的这个类，这样子就只需要简单添加和重写需要的方法即可。
# 例如已有龟类，那么如果要新定义一个甲鱼类，我们只需要让甲鱼类继承已有的龟类，然后重写壳的属性为“软的”即可（据说甲鱼的壳是软的）。
# 
# 2.
# self参数的作用是什么？
# 答：绑定方法，据说有了这个参数，Python
# 再也不会傻傻分不清是哪个对象在调用方法了，你可以认为方法中的
# self
# 其实就是实例对象的唯一标志。
# 
# 3.
# 如果我们不希望对象的属性或方法被外部直接引用，我们可以怎么做？
# 答：我们可以在属性或方法名字前边加上双下划线，这样子从外部是无法直接访问到，会显示AttributeError错误。
# 
# >> >
# 
# class Person:
#     __name = '小甲鱼'
# 
# 
# def getName(self):
#     return self.__name
# 
#p = Person()
#p.__name
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#56>", line
# 1, in < module >
# p.__name
# AttributeError: 'Person'
# object
# has
# no
# attribute
# '__name'
#p.getName()
# '小甲鱼'
# 我们把getName方法称之为“访问器”。Python事实上是采用一种叫“name
# mangling”技术，将以双下划线开头的变量名巧妙的改了个名字而已，我们仍然可以在外部通过“_类名__变量名”的方式访问：
# 
#p._Person__name
# '小甲鱼'
# 当然我们并不提倡这种抬杠较真粗暴不文明的访问形式……
# 
# 4.
# 类在实例化后哪个方法会被自动调用？
# 答：__init__方法会在类实例化时被自动调用，我们称之为魔法方法。你可以重写这个方法，为对象定制初始化方案。
# 
# 5.
# 请解释下边代码错误的原因：
# 
# class MyClass:
#     name = 'FishC'
# 
#     def myFun(self):
#         print("Hello FishC!")
# 
#MyClass.name
# 'FishC'
#MyClass.myFun()
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#6>", line
# 1, in < module >
# MyClass.myFun()
# TypeError: myFun()
# missing
# 1
# required
# positional
# argument: 'self'
# >> >
# 答：首先你要明白类、类对象、实例对象是三个不同的名词。
# 我们常说的类指的是类定义，由于“Python无处不对象”，所以当类定义完之后，自然就是类对象。在这个时候，你可以对类的属性（变量）进行直接访问（MyClass.name）。
# 一个类可以实例化出无数的对象（实例对象），Python
# 为了区分是哪个实例对象调用了方法，于是要求方法必须绑定（通过
# self
# 参数）才能调用。而未实例化的类对象直接调用方法，因为缺少
# self
# 参数，所以就会报错。
# 
# 动动手
# 0.
# 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人 + 1
# 个小孩平日票价。
# 平日票价100元
# 周末票价为平日的120 %
# 儿童半票
# 
# 
# class Ticket():
#     def __init__(self, weekend=False, child=False):
#         self.exp = 100
#         if weekend:
#             self.inc = 1.2
#         else:
#             self.inc = 1
#         if child:
#             self.discount = 0.5
#         else:
#             self.discount = 1
# 
#     def calcPrice(self, num):
#         return self.exp * self.inc * self.discount * num
# 
#adult = Ticket()
#child = Ticket(child=True)
#print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))
# 2
# 个成人 + 1
# 个小孩平日票价为：250.00
# 1.
# 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
# （初学者不一定可以完整实现，但请务必先自己动手，你会从中学习到很多知识的 ^ _ ^）
# 
# 假设游戏场景为范围（x, y）为0 <= x <= 10，0 <= y <= 10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
# 答：参考代码附详细注释，希望先自己认真完成，你会从中学习到很多知识的。
# 
# import random as r
# 
# legal_x = [0, 10]
# legal_y = [0, 10]
# 
# 
# class Turtle:
#     def __init__(self):
#         # 初始体力
#         self.power = 100
#         # 初始位置随机
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
# 
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, 2, -1, -2])
#         new_y = self.y + r.choice([1, 2, -1, -2])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#             # 体力消耗
#         self.power -= 1
#         # 返回移动后的新位置
#         return (self.x, self.y)
# 
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
# 
# 
# class Fish:
#     def __init__(self):
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
# 
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, -1])
#         new_y = self.y + r.choice([1, -1])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#         # 返回移动后的新位置
#         return (self.x, self.y)
# 
# 
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
# 
# while True:
#     if not len(fish):
#         print("鱼儿都吃完了，游戏结束！")
#         break
#     if not turtle.power:
#         print("乌龟体力耗尽，挂掉了！")
#         break
# 
#     pos = turtle.move()
#     # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
#     # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
#     for each_fish in fish[:]:
#         if each_fish.move() == pos:
#             # 鱼儿被吃掉了
#             turtle.eat()
#             fish.remove(each_fish)
#             print("有一条鱼儿被吃掉了...")
# ————————————————
# 版权声明：本文为CSDN博主「来自江南的你」的原创文章，遵循
# CC
# 4.0
# BY - SA
# 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / qq_41556318 / article / details / 84490782