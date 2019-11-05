# 0. 列表都可以存放一些什么东西？
#   我们说 Python 的列表是一个打了激素的数组，
# 如果把数组比喻成集装箱，那么 Python 的列表就是一个大仓库，
# Ta 可以存放我们已经学习过的任何数据类型。
# >>> mix = [1, ‘小甲鱼’, 3.14, [1, 2, 3]]

# 1. 向列表增加元素有哪些方法？
#   append()、extend() 和 insert()。
# 2. append() 方法和 extend() 方法都是向列表的末尾增加元素，请问他们有什么区别？
#   append() 方法是将参数作为一个元素增加到列表的末尾。
#   extend() 方法则是将参数作为一个列表去扩展列表的末尾。
#   
# 3. member.append(['竹林小溪', 'Crazy迷恋']) 和 member.extend(['竹林小溪', 'Crazy迷恋']) 实现的效果一样吗？
member = ["abc"]
member.append(['竹林小溪', 'Crazy迷恋'])
print(member)
member.extend(['竹林小溪', 'Crazy迷恋'])
print(member)
#   
# 4. 有列表 name = ['F', 'i', 'h', 'C']，如果小甲鱼想要在元素 'i' 和 'h' 之间插入元素 's'，应该使用什么方法来插入？
name = ['F', 'i', 'h', 'C']
name.insert(2,'s')
print(name)
#   
# 动动手：
#   
# 0. 自己动手试试看，并分析在这种情况下，向列表添加数据应当采用哪种方法比较好？
#
# 假设给定以下列表：
#
# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
#
# 要求将列表修改为：
#
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
#
# 方法一：使用 insert() 和 append() 方法修改列表。
#
# 方法二：重新创建一个同名字的列表覆盖。
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
#    
#
#     
#   
# 1. 利用 for 循环打印上边 member 列表中的每个内容
# 1.member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# 2.for each in member:
# 3.    print(each)


old = [1,2,3]
new = old
print(old is new)
old = [6]
print(old is new)
print(new)