# 0. 还记得如何定义一个跨越多行的字符串吗（请至少写出两种实现的方法）？
str1 = '''待我长发及腰，将军归来可好？
此身君子意逍遥，怎料山河萧萧。
天光乍破遇，暮雪白头老。
寒剑默听奔雷，长枪独守空壕。
醉卧沙场君莫笑，一夜吹彻画角。
江南晚来客，红绳结发梢。'''
print(str1)
str2 = '待卿长发及腰，我必凯旋回朝。\
昔日纵马任逍遥，俱是少年英豪。\
东都霞色好，西湖烟波渺。\
执枪血战八方，誓守山河多娇。\
应有得胜归来日，与卿共度良宵。\
盼携手终老，愿与子同袍。'
print(str2)
str3 = ('待卿长发及腰，我必凯旋回朝。'
'昔日纵马任逍遥，俱是少年英豪。'
'东都霞色好，西湖烟波渺。'
'执枪血战八方，誓守山河多娇。'
'应有得胜归来日，与卿共度良宵。'
'盼携手终老，愿与子同袍。')
print(str3)

# 1. 三引号字符串通常我们用于做什么使用？
# 三引号字符串不赋值的情况下，通常当作跨行注释使用，例如：
'''这是一个三引号字符串用于注释的例子，
例子虽然只是简简单单的一句话，
却毫无遮掩地体现了作者用情至深，
所谓爱至深处情至简！'''
# 2. file1 = open('C:\windows\temp\readme.txt', 'r')
# 表示以只读方式打开“C:\windows\temp\readme.txt”这个文本文件，
# 但事实上这个语句会报错，知道为什么吗？你会如何修改？
# 只需要使用原始字符串操作符（R或r）即可：
# file1 = open(r'C:\windows\temp\readme.txt', 'r')

# 3. 有字符串：str1 = '<a href="http://www.fishc.com/dvd" target="_blank">
# 鱼C资源打包</a>'，请问如何提取出子字符串：'www.fishc.com'
import  re
str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
print(str1[16:29])
str1 = re.findall("http://(.*?)\" target=",str1,re.S)
print("".join([str(x) for x in str1]))
# 4. 如果使用负数作为索引值进行分片操作，按照第三题的要求你能够正确目测出结果吗？
str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
print(str1[-45:-32])
# 5. 还是第三题那个字符串，请问下边语句会显示什么内容？
print(str1[20:-36])
#
# 6. 据说只有智商高于150的鱼油才能解开这个字符串（还原为有意义的字符串）
# ：str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str1[::3])
#   
# 动动手：
#   
# 0. 请写一个密码安全性检查的脚本代码：check.py
#   
# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
type1 = 0
digit = 0
alpha = 0
sign = 0
signal = '''~!@#$%^&*()_=-/,.?<>;:[]{}|\\'''
secret = input("please enter your password: ")
for i,x in enumerate(secret):
    if(x.isdigit()):
        digit = 1
    if(x.isalpha()):
        alpha = 1
    if(x in signal):
        sign = 1
type1 = digit + alpha + sign
if (i <= 8 and type1 ==1) :
    print("low security")
else:
    if (i>=8 and type1 == 2):
        print("middle security")
    else:
        if(i>=16 and type1 == 3):
            print("high security!")