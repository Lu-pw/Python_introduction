print("{0} love {1} {2}".format("i","use","python"))
print("{a} love {b} {c}".format(a = "i",b = "use",c = "python"))
# print("{a} love {b} {0}".format(a= "i",b = "use","python"))

print("{{0}}".format("不打印"))

print('{0:.1f}{1}'.format(27.658,"GB"))
print("---- 字符串格式化  ----")
print('%c %c %c'%(97,98,99))  # 转字符

print("%s"%"i love python") # 格式化字符串

print("%d + %d = %d" %(4,5,9)) # 十进制

print("8进制 %o"%10)

print('%#o'%12)

print('%+d'%5)