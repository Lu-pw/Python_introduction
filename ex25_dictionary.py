# 0.
# 当你听到小伙伴们在谈论“映射”、“哈希”、“散列”或者“关系数组”
# 的时候，事实上他们就是在讨论什么呢？
# 答：是的，事实上他们就是在讨论我们这一讲介绍的“字典”，都是一个概念！
# （切记，装X的本质就是把同一个东西说成各种不同的事物~）
#
# 1.
# 尝试一下将数据（'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115）
# 创建为一个字典并访问键 'C'对应的值？
Dict = {'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115}
print("type = ",type(Dict)," Dict['C'] = ",Dict['C'])
MyDict = dict((('F', 70), ('i', 105), ('s', 115), ('h', 104), ('C', 67)))
print("type = ",type(Dict)," Dict['C'] = ",Dict['C'])
#  MyDict = dict((('F', 70), ('i', 105), ('s', 115), ('h', 104), ('C', 67)))
#  MyDict_2 = {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}
#  type(MyDict)

# class 'dict'>
#  type(MyDict_2)
#
# class 'dict'>
#
#  MyDict['C']
# 67
# 2.
# 用方括号（“[]”）括起来的数据我们叫列表，那么使用大括号（“{}”）
# 括起来的数据我们就叫字典，对吗？
# 答：不对。
#
#  NotADict = {1, 2, 3, 4, 5}
#  type(NotADict)
# <
#
# class 'set'>
#
#
# 不难发现，虽然我们用大括号（“{}”）把一些数据括起来了，
# 但由于没有反映出这些数据有映射的关系，所以创建出来的不是字典，
# 而是叫’set’的东西，那’set’到底又是啥玩意儿呢？请看第027讲
# | 集合：在我的世界里，你就是唯一！
#
# 3.
# 你如何理解有些东西字典做得到，但“万能的”列表却难以实现（臣妾做不到T_T）？
# 举个例子：
num = [1,2,3,4,5]
alpha = ['a','b','c','d','e']
print("c in num : ",num[alpha.index('c')])
Dict = {1:'a',2:'b',3:'c',4:'d',5:'e'}
print("1 = ",Dict[1])

#  brand = ['李宁', '耐克', '阿迪达斯', '鱼C工作室']
#  slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing',
# '让编程改变世界']
#  print('鱼C工作室的口号是：', slogan[brand.index('鱼C工作室')])
# 鱼C工作室的口号是： 让编程改变世界
# 列表brand、slogan的索引和相对的值是没有任何关系的，
# 我们可以看出唯一有联系的就是两个列表间，索引号相同的元素是有关系的
# （品牌对应口号嘛），所以这里我们通过brand.index('鱼C工作室')
# 这样的语句，间接的实现通过品牌查找对应的口号的功能。
#   
# 这确实是一种可实现方法，呃……但用起来呢，多少有些别扭，效率还不高咧。
# 况且Python是以简洁为主，这样子的实现肯定是不能让人满意的，所以呢
# ，我们需要有字典这种映射类型的出现：
#
#  dict1 = {'李宁': '一切皆有可能', '耐克': 'Just do it',
# '阿迪达斯': 'Impossible is nothing', '鱼C工作室': '让编程改变世界'}
#  print('鱼C工作室的口号是：', dict1['鱼C工作室'])
# 鱼C工作室的口号是： 让编程改变世界
# 4.
# 下边这些代码，他们都在执行一样的操作吗？你看得出差别吗？
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict((('one',1),('two',2),('three',3),('four',4),('five',5)))
print(a['one'],b['one'],c['one'],d['one'],e['one'],f['one'])
# 答：是的，他们都在创建字典：a = dict(one=1, two=2, three=3)，
# 呃，我是看不出差别啦
#
# 5.
# 如图，你可以推测出打了马赛克部分的代码吗？
#
data = "1000,小甲鱼,男"
MyDict = {}
'''还记得字符串的分割方法吧，别学过就忘啦^_^'''
(MyDict['id'], MyDict['name'], MyDict['sex']) = data.split(',')

print("ID:   " + MyDict['id'])
print("Name: " + MyDict['name'])
print("Sex   " + MyDict['sex'])
# 动动手
# 0.
# 尝试利用字典的特性编写一个通讯录程序吧，功能如图：
print("|--- 欢迎进入通讯录程序 ---|\n|--- 1:查询已有联系人  ---|"
      "\n|--- 2:插入新的联系人  ---|\n|--- 3：删除已有联系人 ---|"
      "\n|--- 4:退出通讯录程序  ---|")
contacts = {}

while(1):
    q = input("请输入相关的指令代码")
    if(int(q) == 1):
        name = input("请输入要查询的名称：")
        if name in contacts:
            print(name,": ",contacts[name])
        else:
            print("通讯录未录入此人")
    if(int(q) == 2):
        name = input("请输入要添加的联系人姓名")
        if name in contacts:
            print("通讯录中已有该联系人")
            print(name,": ",contacts[name])
            answer = input("是否修改联系人信息，y/n")
            if(answer.lower() == 'y'):
                contacts[name] = input("请输入该联系人的号码")
        else:
            contacts[name] = input("请输入该联系人的号码")
    if(int(q) == 3):
        name = input("请输入要删除的联系人姓名")
        if name in contacts:
            # del(contacts[name])
            contacts.pop(name)
        else:
            print("通讯录未录入该人")
    if(int(q) == 4):
        break
print('|--- 感谢使用通讯录程序 ---|')
#
# 1.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# Python中的字典与日常生活中的字典进行比较是：将单词称为键（key），
# 把这个单词对应的含义称为值（value）。另外，Python的字典在很多地方称为哈希。
# Python中的字典为映射类型。
#
# （1）创建和访问字典
#
# 字典的标志性符号是大括号。字典由多个键和其对应的值共同构成，
# 每一对键值组合称之为项，
#
# 创建一个空字典：dict1 = {}
# 一般创建字典方法：dict1 = {1: 'one', 2: 'two', 3: 'three'}
# 通过映射关系创建字典：dict1 = dict( ((1, 'one'), (2, 'two'),
# (3, 'three')) )或者dict1 = dict([(1, 'one'), (2, 'two'), (3, 'three')])
# 或者dict1 = dict([[1, 'one'], [2, 'two'], [3, 'three']])
#
# 其中，最里面的几组小括号或者中括号是表示映射关系，第二层的小括号或
# 中括号是将其组合成元组或列表，然后使用dict()
# 函数根据映射关系创建字典。
#
# 修改字典键对应的值：dict1[2] = 'double'
# 增加一组键值：在上一行修改字典键对应值中，如果没有找到对应的键，
# 就增加一组键值：dict1[4] = ‘four’
