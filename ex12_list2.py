# 1. 请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = '小鱿鱼'
print(list1)

# 2. 要对一个列表进行顺序排序，请问使用什么方法？
list1 = [5,2,3,6,9,1,2]
list1.sort()
print(list1)
# 3. 要对一个列表进行逆序排序，请问使用什么方法？
list1.reverse()
print(list1)
# 4. 列表还有两个内置方法没给大家介绍，不过聪明的你应该可以自己摸索使用的门道吧：copy() 和 clear()
list2 = list1.copy()
print(list2)
# copy() 方法跟使用切片拷贝是一样的：

# 5. 你有听说过列表推导式或列表解析吗？
#   
# 没听过？！没关系，我们现场来学习一下吧，看表达式：
# 1.>>> [ i*i for i in range(10) ]
# 复制代码
# 你觉得会打印什么内容？
print([i*i for i in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 复制代码
# 居然分别打印了0到9各个数的平方，然后还放在列表里边了有木有？！
#   
# 列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言
# Haskell。Ta 是一个非常有用和灵活的工具，可以用来动态的创建列表，语法如：
#   
# [有关A的表达式 for A in B]
#   
# 例如
# 1.>>> list1 = [x**2 for x in range(10)]
# 2.>>> list1
# 3.[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 复制代码
# 相当于
# 1.list1 = []
# 2.for x in range(10):
# 3.    list1.append(x**2)
# 复制代码
#
# 问题：请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。
# 1.>>> list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list1)
list2 = []
for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 != 0:
                list2.append((x,y))
print(list2)

# 请使用列表推导式补充被小甲鱼不小心涂掉的部分
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]