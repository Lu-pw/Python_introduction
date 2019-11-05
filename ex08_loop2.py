# 0. if not (money < 100): 上边这行代码相当于？
#  if(money >= 100)
# 1. assert 的作用是什么？
# assert这个关键字我们称之为“断言”，当这个关键字后边的条件为假的时候，
# 程序自动崩溃并抛出AssertionError的异常。
# 什么情况下我们会需要这样的代码呢？当我们在测试程序的时候就很好用，
# 因为与其让错误的条件导致程序今后莫名其妙地崩溃，
# 不如在错误条件出现的那一瞬间我们实现“自爆”。
# 一般来说我们可以用Ta再程序中置入检查点，当需要确保程序中的某个条件一定为真
# 才能让程序正常工作的话，assert关键字就非常有用了。

# 2. 假设有 x = 1，y = 2，z = 3，请问如何快速将三个变量的值互相交换？
x,y,z = 1,2,3
x,y,z = y,z,x
print(x,y,z)
# 3. 猜猜 (x < y and [x] or [y])[0] 实现什么样的功能？
# 这其实是 Python 的作者还没有为 Python 加入三元操作符之前，
# Python 社区的小伙伴们灵活的使用 and 和 or  
# 搭配来实现三元操作符的功能，这里边有涉及到列表和切片的知识，
# 这部分知识很快就会讲解，迫不及待的朋友可以先稍微预习下。

# 4. 你听说过成员资格运算符吗？
# Python 有一个成员资格运算符：in，用于检查一个值是否在序列中，
# 如果在序列中返回 True，否则返回 False。
# 例如：
name = '小甲鱼'
print('鱼' in name)
# 3.True
print('肥鱼' in name)
# 5.False
#   
# 动动手：
#   
# 0. 视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高，
# 但根据一般的统计规律，一个班的成绩一般服从正态分布，
# 也就是说平均成绩一般集中在 70~80 分之间，
# 因此根据统计规律，我们还可以改进下程序以提高效率。
#   
# 题目备忘：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，
# 写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
score = input("please enter your score: ")
while(score.isdigit()):
    score = int(score)
    if(score  > 90):
        print('A')
    else:
        if(score > 80):
            print('B')
        else:
            if(score > 60):
                print('C')
            else:
                print('D')
    score = input("please enter your score: ")

# 1. Python 的作者在很长一段时间不肯加入三元操作符就是怕跟C语言
# 一样搞出国际乱码大赛，蛋疼的复杂度让初学者望而生畏，不过，如果你一旦搞清楚了
# 三元操作符的使用技巧，或许一些比较复杂的问题反而迎刃而解。
# 请将以下代码修改为三元操作符实现：
# 1.small = x if (x < y and x < z) else (y if y < z else z)
x,y,z = 15,21,3
small = x if (x < y and x < z) else (y if y < z else z)
print(small)