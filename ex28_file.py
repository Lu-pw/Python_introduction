import sys
import os
sys.path.append(os.path.abspath(os.curdir))
# help(open)
#0.下边只有一种方式不能打开文件，请问是哪一种，为什么？
f = open('E:\Pythonclass\Python_intro/test','w')  #A
# f = open('E:\Pythonclass\Python_intro\test.txt','w')  #B
# f = open('E:\Pythonclass\Python_intro//test.txt','w')  #C
# f = open('E:\Pythonclass\Python_intro\\test.txt','w')  #D
#答：B不能打开文件。
#
#Windows在路径名中既可以接受斜线（/）也可以接受反斜线（\），
#不过如果使用反斜线作为路径名的分隔符的话，要注意使用双反斜线（\\）进行转义，
#否则Python会将反斜线进行转义，例如（\n）看成一个换行符，（\t）
#看作一个制表符等。
#
#1.打开一个文件我们使用open()函数，通过设置文件的打开模式，
#决定打开的文件具有那些性质，请问默认的打开模式是什么呢？
#答：open()函数默认的打开模式是'rt'，即可读、文本的模式打开。
#
#2.请问open('E:\\Test.bin','xb')是以什么样的模式打开文件的？
#答：以“可写入以及二进制模式”打开文件“E:\\Test.bin”。

#这里要注意的是'x'和'w'均是以“可写入”的模式打开文件，但以'x'模式打开的时候，
#如果路径下已经存在相同的文件名，会抛出异常，而'w'模式的话会直接覆盖同名文件。
#
#因此，'w'模式打开文件会比较危险，容易导致此前的内容遗失，
#因此使用'w'模式打开文件前先检查该文件名是否已经存在显得非常重要！
#下节课小甲鱼会教你如何安全的打开一个文件^_^
#
#3.尽管Python有所谓的“垃圾回收机制”，但对于打开了的文件，
#在不需要用到的时候我们仍然需要使用f.close()将文件对象“关闭”，这是为什么呢？
#答：Python拥有垃圾收集机制，会在文件对象的引用计数降至零的时候自动关闭文件，
#所以在Python编程里，如果忘记关闭文件并不会造成内存泄漏那么危险。
#
#但并不是说就可以不要关闭文件，如果你对文件进行了写入操作，
#那么你应该在完成写入之后进行关闭文件。因为Python可能会缓存你写入的数据，
#如果这中间断电了神马的，那些缓存的数据根本就不会写入到文件中。
#所以，为了安全起见，要养成使用完文件后立刻关闭的优雅习惯。
#
f = open('E:\Pythonclass\Python_intro/test.txt','w',encoding='utf-8')
str1 = 'i love python,人生苦短，及时行乐！'
for i in str1:
    f.write(i)
f.close()
# #4.如何将一个文件对象（f）中的数据存放进列表中？
#答：list(f)，是不是非常的方便！
#
#5.如何迭代打印出文件对象（f）中的每一行数据？
#答：直接使用for语句把文件对象迭代出来即可：
#
f = open('test.txt',encoding='utf8')
for i in f:
    print(i)
print(f.tell())
f.close()
#6.文件对象的内置方法f.read([size=-1])作用是读取文件对象内容，
#size参数是可选的，那如果设置了size=10，例如f.read(10)，将返回什么内容呢？
#答：将返回从文件指针开始（注意这里并不是文件头哦）的连续10个字符。
f = open('test.txt','r',encoding='utf-8')
print("文件指针位置： ",f.tell())
print("从该指针读取连续的8个字符",f.read(8))# '\t'被视作一个字符
#7.如何获得文件对象（f）当前文件指针的位置？
#答：f.tell()会告诉你^_^
print("获取文件指针位置：",f.tell())
f.close()
#8.还是视频中的那个演示文件（record.txt），请问为何f.seek(45,0)不会出错，
#但f.seek(46)就出错了呢？
# record = open('record.txt','r',encoding='GBK')
# # print(record.read())
# print(record.seek(45))
# print(record.seek(46))
# 46 #???
# f.readline()
#Traceback(mostrecentcalllast):
#  File"<pyshell#18>",line1,in<module>
#  f.readline()
#UnicodeDecodeError:'gbk'codeccan'tdecodebyte0xe3inposition4:
#illegalmultibytesequence
#答：因为使用f.seek()定位的文件指针是按字节为单位进行计算的，
#演示文件（record.txt）是以GBK进行编码的，按照规则，一个汉字需要占用两个字节，
#f.seek(45)的位置位于字符“小”的开始位置，因此可以正常打印，
#而f.seek(46)的位置刚好位于字符“小”的中间位置，因此按照GBK编码的形式
#无法将其解码！
#
#动动手
#0.尝试将文件（  OpenMe.mp3 (700Bytes,下载次数:7051) ）打印到屏幕上
#答：直接使用打开文本文件的形式打开即可，至于为什么？打开后会告诉你@_@
#f=open('OpenMe.mp3')
#for each_line in f:
#      print(each_line,end='')
#f.close()
#1.编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）
#f1=open('OpenMe.mp3')
#f2=open('OpenMe.txt','x')#使用”x”打开更安全
#f2.write(f1.read())
#f2.close()
#f1.close()
#2.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
#文件打开模式
#
#打开模式	执行操作
#'r'	以只读方式打开文件（默认）
#'w'	以写入的方式打开文件，会覆盖已存在的文件
#'x'	如果文件已经存在，使用此模式打开将引发异常
#'a'	以写入模式打开，如果文件存在，则在末尾追加写入
#'b'	以二进制模式打开文件
#'t'	以文本模式打开（默认）
#'+'	可读写模式（可添加到其他模式中使用）
#'U'	通用换行符支持
#文件对象方法
#
#文件对象方法	执行操作
#f.close()	关闭文件
#f.read([size=-1])	从文件读取size个字符，当未给定size或给定负值的时候，
#读取剩余的所有字符，然后作为字符串返回
#f.readline([size=-1])	从文件中读取并返回一行（包括行结束符），
#如果有size有定义则返回size个字符
#f.write(str)	将字符串str写入文件
#f.writelines(seq)	向文件写入字符串序列seq，seq应该是一个
#返回字符串的可迭代对象
#f.seek(offset,from)	在文件中移动文件指针，从from
#（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
#f.tell()	返回当前在文件中的位置
#f.truncate([size=file.tell()])	截取文件到size个字节，
#默认是截取到文件指针当前位置

# f2 = open('test1.txt',encoding='utf-8')
# print(f2.read())
# f2.close()
# f2 = open('test1.txt',encoding='utf-8')
# print(f2.read(5))
# print(f2.tell())
# print(f2.seek(4,0))
# print(f2.readline())
# print(list(f2))
# print(f2.seek(0,0))
# # 效率低
# # lines = list(f2)
# # for each_line in lines:
# #     print(each_line)
# # 效率高
# for each in f2:
#     print(each)
# f2.close()
#
# ## 文件的写入
# f3 = open('test3.txt','w')
# f3.write('i love python!')
# f3.close()

# # 文件的读取与应用
record = open('record.txt',encoding='utf-8')
boy = []
girl = []
count = 1
def save():
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    # 文件的分别保存操作

    boy_file = open(file_name_boy, 'w', encoding='utf-8')
    girl_file = open(file_name_girl, 'w', encoding='utf8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()
for each_line in record:
    if each_line[:6] != "======":
        # 这里进行字符串分割操作
        # print(each_line.split(sep=":",maxsplit=1))
        (role,line_spoken) = each_line.split(sep=':',maxsplit=1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        save()
        boy = []
        girl = []
        count += 1
save()
record.close()
