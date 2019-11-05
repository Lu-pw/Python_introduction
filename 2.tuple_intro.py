# 元组：带上了枷锁的列表
tuple1 = (0,1,2,3,4,5)
# 下标同样从0开始
print(tuple1[1])
print(tuple1[:5])
tuple2 = tuple1[2:]
print(tuple2)

# tuple1[1] = 3 # 报错，元组内容不可直接改

temp = (1)
print(type(temp))
# 加，表示元组
temp = (1,)
print(type(temp))
temp = 1,
print(type(temp))
print(8*(8))
print(8*(8,))

temp = ("fish","duck","chicken","meat")
temp = temp[:2] + ("like",) + temp[2:]
print(temp)
# del temp  #删除后输出报错
# print(temp)
# #不支持删除单个内容，可以切片
# del temp[2]
