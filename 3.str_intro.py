str1 = "I love python"
print(str1[:5])
print(str1[2])
str2 = str1[:6] + " add string" + str1[6:]
print(str2)

# 全部字符改小写
str1 = str1.casefold()
print(str1)
# 首字母大写
str1 = str1.capitalize()
print(str1)
# 字符出现的次数
print(str1.count('o'))
# 编码格式
str1 = str1.encode(encoding='utf-8',errors='strict')
print(str1)
# 检查字符串以sub子字符串结束,是则返回TRUE
print(str2.endswith("ve",0,6))
# 将字符串中的TAB符号\t化为空格，如不指定长度则默认8
str2 = str2[:3] + "\t" + str2[3:]
print(str2)
str2 = str2.expandtabs(tabsize=6)
print(str2)

print(str2.find("add"))
print(str2.find("ass"))
# index与find区别是找不到抛异常
print(str2.index("add"))

print("str1类型：",type(str1))
print("str2类型",type(str2))
str3 = "12".join("join")
print(str3)
print(str3.replace("12","0",2))
str3 = str3.replace("12","\t")
print(str3)
print(str3.partition('o'))

# 字节转字符串
print(str(str1,encoding="utf-8"))
# 字符串转字节
print(bytes(str2,encoding="utf-8"))

