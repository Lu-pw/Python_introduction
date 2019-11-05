# 0.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# （一）对象
# 这节课给大家介绍对象。我们之前说过Python无处不对象，Python到处都是对象，
# 然而我们很多人不理解对象到底是什么？他们只是在学习的时候有听过面向对象编程
# 这么一回事，但是他们仍然在使用对象。
#
# 对象是模拟真实世界，把数据和代码都封装在一起。
# 下面是关于类的一个简单的例子：
#
class Turtle:  # Python中的类名约定以大写字母开头
    "-----关于类的一个简单例子----"
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print('我正在努力地向前爬.......')

    def run(self):
        print('我正在努力地向前爬.......')

    def bite(self):
        print('咬死你咬死你！！！')

    def eat(self):
        print('有吃的，真满足^_^')

    def sleep(self):
        print('累了，困了，睡觉了zzzzz')
#
#
# 上面的语句就定义好了一个类。
#
tt = Turtle()  # 实例化一个类对象
# 调用类和调用函数相同，Python的类名以大写字母开头，函数以小写字母开头，方便区分。
#
# 这里实例化了一个对象，并用tt这个变量给指过去，下面的语句用于调用对象里的方法：
#
tt.climb()
# 我正在努力地向前爬.......
tt.bite()
# 咬死你咬死你！！！
# （二）面向对象的特征
#
# OO = Object
# Oriented（面向对象）
#
# Python就是一门纯粹的面向对象编程的语言，面向对象编程有什么特征呢？
#
# 第一个特征就是封装
# 表面上看，对象封装了属性（也就是变量）和方法（也就是函数），
# 成为了一个独立性很强的模块，封装更是一种信息隐蔽技术，使得我们的数据更加安全，
# 举例说明：
# Python的列表实际上就是一个对象，它提供了若干种方法供我们根据需求来调整
# 整个列表，但是我们知道列表对象里边的这些方法是如何实现的吗？我们不知道。
# 我们也不知道列表对象里有哪些变量。这就是所谓的封装，它封装起来，
# 只给我们需要的方法的名字，然后我们调用这个名字，知道它可以实现就OK了。
# 但是不会告诉我们具体的实现过程。
# 第二个特征就是继承
# 继承是子类自动共享父类之间数据和方法的机制。
#
# 定义子类的方法为：
#
# class 子类名 （父类名）:
#
# >> >
#
# class Mylist(list):
#     pass
#
#  list1 = Mylist()
#  list1.append(5)
#  list1.append(3)
#  list1.append(7)
#  list1
# [5, 3, 7]
#  list1.sort()
#  list1
# [3, 5, 7]
# 这里我们自定义一个list的子类Mylist，我们发现子类Mylist也能调用父类list的方法
# 第三个特征就是多态
# 多态的概念是不同对象对同一方法响应不同的行动。
#
class A:
    def fun(self):
        print('我是小A')

class B:
    def fun(self):
        print('我是小B')

a = A()
b = B()
a.fun()
# 我是小A
b.fun()
# 我是小B
# 测试题
# 0.
# 对象中的属性和方法，在编程中实际是什么？
# 答：变量（属性）和函数（方法）。
#
# 1.
# 类和对象是什么关系呢？
# 答：类和对象的关系就如同模具和用这个模具制作出的物品之间的关系。
# 一个类为它的全部对象给出了一个统一的定义，而他的每个对象则是符合这种定义的
# 一个实体，因此类和对象的关系就是抽象和具体的关系。
#
# 2.
# 如果我们定义了一个猫类，那你能想象出由“猫”类实例化的对象有哪些？
# 答：叮当猫，咖啡猫，Tom（Tom & Jerry），Kitty（Hello Kitty）……
#
# 3.
# 类的定义有些时候或许不那么“拟物”，有时候会抽象一些，例如我们定义一个矩形类，
# 那你会为此添加哪些属性和方法呢？
# 答：属性可以是长和宽，方法可以是计算周长、面积等。
#
# 4.
# 类的属性定义应该尽可能抽象还是尽可能具体？
# 答：正确的做法是应该尽可能的抽象，因为这样更符合面向对象的思维。
#
# 5.
# 请用一句话概括面向对象的几个特征？
# 封装
# 对外部隐藏对象的工作细节
# 继承
# 子类自动共享父类之间数据和方法的机制
# 多态
# 可以对不同类的对象调用相同的方法，产生不同的结果
# 6.
# 函数和方法有什么区别？
# 答：细心的童鞋会发现，方法跟函数其实几乎完全一样，但有一点区别是方法
# 默认有一个self参数，这个参数是什么意思？请听下一讲详细分解。
#
# 动动手
# 0.
# 按照以下提示尝试定义一个Person类并生成类实例对象。
# 属性：姓名（默认姓名为“小甲鱼”）
# 方法：打印姓名
# 提示：方法中对属性的引用形式需加上
# self，如self.name
class Person:
    name = '小甲鱼'

    def print_name(self):
        print(self.name)

people = Person()
print(people.name)
people.print_name()

###########################################
# class Person:
#     name = '小甲鱼'
#
#     def printName(self):
#         print(self.name)
#
#
# 1.
# 按照以下提示尝试定义一个矩形类并生成类实例对象。
# 属性：长和宽
# 方法：设置长和宽 -> setRect(self)，获得长和宽 -> getRect(self)，
# 获得面积 -> getArea(self)
# 提示：方法中对属性的引用形式需加上self，如self.width
class Rect:
    length = 0
    width = 0

    def setRect(self):
        self.length = float(input("请输入矩形的长："))
        self.width = float(input("请输入矩形的宽："))
    def getRect(self):
        print(self.length,self.width)
    def getArea(self):
        print(self.length * self.width)


rect1 = Rect()
rect1.length = 2
rect1.width = 3
rect1.setRect()
rect1.getRect()
rect1.getArea()

# 程序截图：
#
# class Rectangle:
#     length = 5
#     width = 4
#
#     def setRect(self):
#         print("请输入矩形的长和宽...")
#         self.length = float(input('长：'))
#         self.width = float(input('宽：'))
#
#     def getRect(self):
#         print('这个矩形的长是：%.2f，宽是：%.2f' % (self.length, self.width))
#
#     def getArea(self):
#         return self.length * self.width
#
