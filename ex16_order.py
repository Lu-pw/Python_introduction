# 0. 我们根据列表、元祖和字符串的共同特点，把它们三统称为什么？
# 序列，因为他们有以下共同点：
#     
# 1）都可以通过索引得到每一个元素
# 2）默认索引值总是从0开始（当然灵活的Python还支持负数索引）
# 3）可以通过分片的方法得到一个范围内的元素的集合
# 4）有很多共同的操作符（重复操作符、拼接操作符、成员关系操作符）

# 1. 请问分别使用什么BIF，可以把一个可迭代对象转换为列表、元祖和字符串？
# list([iterable]) 把可迭代对象转换为列表
#   
# tuple([iterable]) 把可迭代对象转换为元祖
#   
# str(obj)  把对象转换为字符串
#   
# 例如：
temp = 'i love python'
temp = list(temp)
print(temp)
temp = tuple(temp)
print(temp)
temp = "".join([str(x) for x in temp])
print(temp)
# 2. 你还能复述出“迭代”的概念吗？
# 所谓迭代，是重复反馈过程的活动，
# 其目的通常是为了接近并到达所需的目标或结果。
# 每一次对过程的重复被称为一次“迭代”，
# 而每一次迭代得到的结果会被用来作为下一次迭代的初始值。

# 3. 你认为调用 max('I love FishC.com') 会返回什么值？为什么？
# 会返回：'v'，因为字符串在计算机中是以ASCII码的形式存储
# （ASCII对照表：http://bbs.fishc.com/thread-41199-1-1.html），
# 参数中ASCII码值最大的是'v'对应的118。
#     
# 
# 4. 哎呀呀，现在的小屁孩太调皮了，邻居家的孩子淘气，把小甲鱼刚写好的代码画了个图案，麻烦各位鱼油恢复下啊，另外这家伙画的是神马吗？怎么那么眼熟啊！？？

# name = input('请输入待查找的用户名：')
# score = [['迷途', 85], ['黑夜', 80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
# IsFind = False
#
# for each in score:
#     if name in each:
#         print(name + '的得分是：', each[1])
#         IsFind = True
#         break
# if IsFind == False:
#     print('查找的数据不存在！')

#     
# 动动手答案：
#    
# 本帖隐藏的内容
# 0. 猜想一下 min() 这个BIF的实现过程
# def min(x):
#     least = x[0]
#
#     for each in x:
#         if each < least:
#             least = each
#
#      return least
#
# print(min('123456789'))
#
# 1. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，
# 请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果
#     
# def sum(x):
#     sum1 = 0
#     for i in x:
#         if(type(i) == int or type(i) == float):
#             sum1 = sum1 + i
#     return  sum1
#
# print(sum([1, 2.1, 2.3, 'a', '1', True]))

def sum(x):
    sum1 = 0
    for i in x:
        if(i.isdigit()):
            sum1 = sum1 + int(i)
    return  sum1

print(sum("sdsf1234f"))

