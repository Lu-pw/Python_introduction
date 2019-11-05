# 0. 根据说明填写相应的字符串格式化符号
#
#    符   号	   说     明
#      %c	   格式化字符及其ASCII码
#      %s	   格式化字符串
#      %d	   格式化整数
#      %o	   格式化无符号八进制数
#      %x	   格式化无符号十六进制数
#      %X	   格式化无符号十六进制数（大写）
#      %f	   格式化定点数，可指定小数点后的精度
#      %e	   用科学计数法格式化定点数
#      %g	   根据值的大小决定使用%f或者%e
#      %G	   根据值的大小决定使用%F或者%E
#  
#
# 1. 请问以下这行代码会打印什么内容？
# 1.>>> "{{1}}".format("不打印", "打印")
print("{{1}}".format("不打印", "打印"))
#
#
# 2. 以下代码中，a, b, c是什么参数？
# 1.>>> "{a} love {b}.{c}".format(a="I", b="FishC", c="com")
# 2.'I love FishC.com'
# 关键字参数
#
#
# 3. 以下代码中，{0}, {1}, {2}是什么参数？
# 1.>>> "{0} love {1}.{2}".format("I", "FishC", "com")
# 2.'I love FishC.com'
# 位置参数
#
#
# 4. 如果想要显示Pi = 3.14，format前边的字符串应该怎么填写呢？
# 1.''.format('Pi = ', 3.1415)
print("{0}{1:.2f}".format("PI = ",3.1415))
#
#
# 动动手：
#
# 0. 编写一个进制转换程序（提示，十进制转换二进制可以用bin()这个BIF）：
q =  True
while q:
    num = input("please enter a number: ")
    if num != 'q':
        num = int(num)
        print("十进制->十六进制%d -> 0x%x" %(num,num))
        print("十进制 -> 八进制%d -> 0o%o"%(num,num))
        print("十进制 -> 二进制%d ->"%num,bin(num))
