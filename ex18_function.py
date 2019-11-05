# 1、函数文档和“#”为函数有什么不同？
# 给函数写文档是为了让别人更好的理解你的函数
def myFirstFunction():
    "利用help(myFirstFunction)打印我"
    print("测试")
# 我们看到在函数开头写下的字符串是不会打印出来的，但ta会作为函数的
# 一部分存储起来，我们称之为函数文档字符串，他的功能和注释一样
help(myFirstFunction)
# 或
print(myFirstFunction.__doc__)


# 2、使用关键字参数，可以有效避免什么问题的出现？
# 关键字参数，是指函数在调用的时候，带上参数的名字去指定具体调用的哪个
# 参数，从而可以不用按照参数的顺序调用函数，如：
def say(name,word):
    print(name,word)
say(word="love python",name="i")
# 使用关键字参数，可以有效避免因不小心搞乱参数顺序而导致的bug



# 3.使用help(print）重看print。这个BIF有哪些默认参数分别起到什么作用？
help(print)

# 4.	默认参数和关键字参数表面最大的区别是什么？
# 关键字参数是在函数调用的时候，通过参数名制定需要赋值的参数，这样做就不怕
# 因为搞不清参数的顺序而导致函数调用出错，而默认参数是在函数定义的时候，为
# 形参赋初值，当函数调用的时候，不传递实参，则默认使用形参的初始值代替


# 1、编写一个符合以下要求的函数：
# a、计算打印所有参数的和乘以基数（base=3）的结果
# b、如果参数中最后一个参数为（base = 5），则设定基数为5，基数不参与求和计算
def base(*param,base = 3):
    result = 0
    for each in param:
        result += each

    result *= base
    print(result)
base(1,2,3,5,base=5)


# 2、如果一个数的每位的立方总和等于该数，则该数为水仙花数，编程找出所有水仙花数
def Narcissus():
    for i in range(100,1000):
        if(((i%10)**3+(i//10%10)**3+(i//100)**3) == i):
            print(i,end='\t')
    print()
Narcissus()


# 3、编写一个函数findstr(),该函数统计一个长度为2(改?)的字符串在另一个字符串中出现的次数
# 如：假定输入“you cannot improve your past,but you can improve your future.
# once time is wasted,life is wasted.”子字符串为“im”，函数执行显示共有三次
def findstr(str,sub_str):
    sub_len = len(sub_str)
    len1 = len(str)
    result = 0
    for i,each in enumerate(str):
        if(i < len1 - sub_len+1):
            if(str[i:i+sub_len] == sub_str):
                result += 1
    print("字符串共出现：",result,"次")
findstr("helhelohelo","hel")


