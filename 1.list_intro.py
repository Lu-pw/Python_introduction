member = ["hello","my","first"]
print(member)
# //添加
member.append("class")
print(member)
# //扩展
member.extend(["for",1])
print(member)
# //插入
member.insert(1,"one")
print(member)
print("------2--------")
print(member[0])
print(member[2])
# //调换
temp = member[2]
member[2] = member[0]
member[0] = temp
print(member)
# //删除
member.remove("for")
print(member)

del member[1]
print(member)
# 踢出1
member.pop()
#  踢出class
print(member.pop())
print(member)

member.pop(1)
print(member)

member.extend([1,2,3,4,5,6])
# 输出索引值1至4的内容
print(member[1:5])


print("------3、操作符------")
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 > list2)

list3 = list1
print((list1<list2) and (list1 == list3))

list5 = list1 + list2
print(list5)
# 运算
print(list2 + ["hello"])
# 运算
print(list2 * 3)
# 包含
print( 5 in list2)

# 试试与extend的不同
list2.append(["hello","xiaojiayu"])
print(list2)
print("hello" not in list2)
print(list2[3][1])

print(dir(list2))

print("内置方法",list2.count)
list2 *= 2
print(list2.count(5))
print(list2)
#  查找
print(list2.index(5))
#  指定位置开始查
print(list2.index(6,3,7))
del list2[3]
list2.remove(['hello', 'xiaojiayu'])
print(list2)
# 翻转
list2.reverse()
print("反转",list2)
# 排序
list2.sort()
print("排序",list2)
# 反转+排序
list2.sort(reverse=True)
print("反转+排序",list2)

# copy
list6 = list2[:]
list8 = list2
list2.sort()
print(list2)
print(list6)
print(list8)
print(list2 is list6)
print(list2 is list8)