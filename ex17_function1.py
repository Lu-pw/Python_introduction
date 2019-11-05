# 0. 你有听说过DRY吗？
#        
# DRY是程序员们公认的指导原则：Don't Repeat Yourself. 
# 快快武装你的思维吧，拿起函数，不要再去重复拷贝一段代码了！
#     
#    
# 1. 都是重复一段代码，为什么我要使用函数（而不使用简单的拷贝黏贴）呢？
#      
# 使用函数:
# 0) 可以降低代码量（调用函数只需要一行，而拷贝黏贴需要N倍代码）
# 1) 可以降低维护成本（函数只需修改def部分内容，而拷贝黏贴则需要
# 每一处出现的地方都作修改）
# 2) 使序更容易阅读（没有人会希望看到一个程序重复一万行“I love FishC.com”）
#
# 2. 函数可以有多个参数吗？
#       
# 可以的，理论上你想要有多少个就可以有多少个，只不过如果函数的参数过多，
# 在调用的时候出错的机率就会大大提高，因而写这个函数的程序员
# 也会被相应的问候祖宗，所以，尽量精简吧，在Python的世界里，精简才是王道！
#      
#      
# 3. 创建函数使用什么关键字，要注意什么？
#     
# 使用“def”关键字，要注意函数名后边要加上小括号“()”，
# 然后小括号后边是冒号“:”，然后缩进部分均属于函数体的内容，例如：
# 1.def MyFun():
# 2.    # 我是函数体
# 3.    # 我也是函数体
# 4.    # 我们都属于函数MyFun()
# 5.
# 6.# 噢，我不属于MyFun()函数的了
# 复制代码
#
#
# 4. 请问这个函数有多少个参数？
# 1.def MyFun((x, y), (a, b)):
# 2.    return x * y - a * b
# 复制代码
#
# 如果你回答两个，那么恭喜你错啦，答案是0，因为类似于这样的写法是错误的！
# 我们分析下，函数的参数需要的是变量，而这里你试图用“元祖”的形式来传递是不可行的。
#      
def myFun(x,y):
    return x[0] * x[1] - y[0] * y[1]
a = (1,2)
b = (3,4)
print(myFun(a,b))
# 我想你如果这么写，你应该是要表达这么个意思：
# 1.>>> def MyFun(x, y):
# 2.        return x[0] * x[1] - y[0] * y[1]
# 3.
# 4.>>> MyFun((3, 4), (1, 2))
# 5.10
# 复制代码
#
#
# 5. 请问调用以下这个函数会打印什么内容？
# 1.>>> def hello():
# 2.        print('Hello World!')
# 3.        return
# 4.        print('Welcome To FishC.com!')
def hello():
    print("hello world!")
    return
    print("i love python")
hello()
#
# 会打印：
# 1.>>> hello()
# 2.Hello World!
# 复制代码
#
# 因为当Python执行到return语句的时候，Python认为函数到此结束，
# 需要返回了（尽管没有任何返回值）。
#
#     
#           
# 动动手答案：
#    
# 本帖隐藏的内容
# 0. 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
def power(x,y):
    if(y == 0 and x != 0):
        return 1
    if(y < 0):
        result = 1
        for i in range(-y):
            result = result *(x)
        return  1/result
    if(y > 0):
        result = 1
        for i in range(y):
            result = result * x
        return  result
print(power(2,-2))

#
#
# 1. 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，
# 例如gcd(x, y)返回值为参数x和参数y的最大公约数。
def gcd(x,y):
    result = 1
    a,b = (x,y) if x < y else (y,x)
    for i in range(2,a+1):
        if(a % i ==0 and b % i == 0):
             result = result * i
             a = a / i
             b = b / i
             i = i - 1
    return result
print(gcd(144,166))


# 1.def gcd(x, y):
# 2.    while y:
# 3.        t = x % y
# 4.        x = y
# 5.        y = t
# 6.
# 7.    return x
# 8.    
# 9.print(gcd(4, 6))
# 复制代码
#
#
# 2. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接
# 的方式，结果与调用bin()一样返回字符串形式。
def Dec2bin(x):
    result = ""
    while x != 0:
        result = str(x % 2) + result
        x = x // 2
    return result
print(Dec2bin(2))
# 1.def Dec2Bin(dec):
# 2.    temp = []
# 3.    result = ''
# 4.    
# 5.    while dec:
# 6.        quo = dec % 2
# 7.        dec = dec // 2
# 8.        temp.append(quo)
# 9.
# 10.    while temp:
# 11.        result += str(temp.pop())
# 12.    
# 13.    return result
# 14.
# print(Dec2Bin(62))