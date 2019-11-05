# 0.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# •任务：将文件（record.txt）中的数据进行分割并按照以下规律保存起来：
#
# –小甲鱼的对话单独保存为boy_ *.txt的文件（去掉“小甲鱼:”）
#
# –小客服的对话单独保存为girl_ *.txt的文件（去掉“小客服:”）
#
# –文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt,
# girl_2.txt, boy_3.txt, gril_3.txt共6个文件
# （提示：文件中不同的对话间已经使用“ == == == == == ”分割）
#
# 小客服: 小甲鱼，今天有客户问你有没有女朋友？
# 小甲鱼: 咦？？
# 小客服: 我跟她说你有女朋友了！
# 小甲鱼:。。。。。。
# 小客服: 她让你分手后考虑下她！然后我说: "您要买个优盘，我就帮您留意下~"
# 小甲鱼: 然后呢？
# 小客服: 她买了两个，说发一个货就好
# ~
# 小甲鱼: 呃。。。。。。你真牛！
# 小客服: 那是，谁让我是鱼C最可爱小客服嘛
# ~
# 小甲鱼: 下次有人想调戏你我不阻止
# ~
# 小客服: 滚！！！
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 小客服: 小甲鱼，有个好评很好笑哈。
# 小甲鱼: 哦？
# 小客服: "有了小甲鱼，以后妈妈再也不用担心我的学习了~"
# 小甲鱼: 哈哈哈，我看到丫，我还发微博了呢
# ~
# 小客服: 嗯嗯，我看了你的微博丫
# ~
# 小甲鱼: 哟西
# ~
# 小客服: 那个有条回复“左手拿著小甲魚，右手拿著打火機，哪裡不會點哪裡，so
# easy ^ _ ^”
# 小甲鱼: T_T
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 小客服: 小甲鱼，今天一个会员想找你
# 小甲鱼: 哦？什么事？
# 小客服: 他说你一个学生月薪已经超过12k了！！
# 小甲鱼: 哪里的？
# 小客服: 上海的
# 小甲鱼: 那正常，哪家公司？
# 小客服: 他没说呀。
# 小甲鱼: 哦
# 小客服: 老大，为什么我工资那么低啊？？是时候涨涨工资了！！
# 小甲鱼: 啊，你说什么？我在外边呢，这里好吵吖。。。。。。
# 小客服: 滚！！！
'''解决局部变量的方法，一、传参 二、nonlocal 三、global'''
def save_file(boy,girl,count):
    boy_file_name = "boy:" + str(count) + ".txt"
    girl_file_name = "girl" + str(count) + ".txt"
    boy_file = open(boy_file_name,'w',encoding = 'utf8')
    girl_file = open(girl_file_name,'w',encoding='utf8')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()
def split_file():
    record = open('record.txt', encoding='utf8')
    boy = []
    girl = []
    count = 1
    for each_line in record:
        if each_line[:6] != "======":
            name,spoken = each_line.split(sep=":",maxsplit=1)
            if name == "小甲鱼":
                boy.append(spoken)
            else:
                girl.append(spoken)
        else:
            save_file(boy,girl,count)
            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    record.close()
# split_file()
############################################################
# f = open('record.txt')
#
# boy = []
# girl = []
# count = 1
#
# for each_line in f:
#     if each_line[:6] != '======':
#         (role, line_spoken) = each_line.split(':', 1)
#         if role == '小甲鱼':
#             boy.append(line_spoken)
#         if role == '小客服':
#             girl.append(line_spoken)
#     else:
#         file_name_boy = 'boy_' + str(count) + '.txt'
#         file_name_girl = 'girl_' + str(count) + '.txt'
#
#         boy_file = open(file_name_boy, 'w')
#         girl_file = open(file_name_girl, 'w')
#
#         boy_file.writelines(boy)
#         girl_file.writelines(girl)
#
#         boy_file.close()
#         girl_file.close()
#
#         boy = []
#         girl = []
#         count += 1
#
# file_name_boy = 'boy_' + str(count) + '.txt'
# file_name_girl = 'girl_' + str(count) + '.txt'
#
# boy_file = open(file_name_boy, 'w')
# girl_file = open(file_name_girl, 'w')
#
# boy_file.writelines(boy)
# girl_file.writelines(girl)
#
# boy_file.close()
# girl_file.close()
#
# f.close()
# 利用函数优化后的程序：
#
# def save_file(boy, girl, count):
#     file_name_boy = 'boy_' + str(count) + '.txt'
#     file_name_girl = 'girl_' + str(count) + '.txt'
#
#     boy_file = open(file_name_boy, 'w')
#     girl_file = open(file_name_girl, 'w')
#
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
#
#     boy_file.close()
#     girl_file.close()
#
#
# def split_file(file_name):
#     f = open(file_name)
#
#     boy = []
#     girl = []
#     count = 1
#
#     for each_line in f:
#         if each_line[:6] != '======':
#             (role, line_spoken) = each_line.split(':', 1)
#             if role == '小甲鱼':
#                 boy.append(line_spoken)
#             if role == '小客服':
#                 girl.append(line_spoken)
#         else:
#             save_file(boy, girl, count)
#
#             boy = []
#             girl = []
#             count += 1
#
#     save_file(boy, girl, count)
#
#     f.close()
#
#
# split_file('record.txt')
# 0.
# 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图：
#
#
# 从明天起，做一个幸福的人
# 喂马、劈柴、周游世界
# 从明天起，关心粮食和蔬菜
# 我有一所房子，面朝大海，春暖花开
#
# 从明天起，和每一个亲人通信
# 告诉他们我的幸福
# 那幸福的闪电告诉我的
# 我将告诉每一个人
#
# 给每一条河每一座山取一个温暖的名字
# 陌生人，我也为你祝福
# 愿你有一个灿烂的前程
# 愿你有情人终成眷属
# 愿你在尘世获得幸福
# 我只愿面朝大海，春暖花开
def file_input():
    file_name = input("请输入文件名")
    file = open(str(file_name)+".txt",'w',encoding='utf8')
    file.close()
    content = input("请输入文件内容（单独输入':w'退出）")
    while(content != ':w'):
        file = open(str(file_name)+".txt",'a+',encoding='utf8')
        file.write(content)
        file.write('\n')
        file.close()
        content = input()
# file_input()
##################################################################
#
# def file_write(file_name):
#     f = open(file_name, 'w')
#     print('请输入内容【单独输入\':w\'保存退出】：')
#
#     while True:
#         write_some = input()
#         if write_some != ':w':
#             f.write('%s\n' % write_some)
#         else:
#             break
#
#     f.close()
#
#
# file_name = input('请输入文件名：')
# file_write(file_name)
# 1.
# 编写一个程序，比较用户输入的两个文件，如果不同，
# 显示出所有不同处的行号与第一个不同字符的位置，程序实现如图：
def file_differ():
    file1_name = input("请输入文件一的名称：")
    file2_name = input("请输入文件二的名称：")
    file1 = open(file1_name+".txt",encoding='utf-8')
    file2 = open(file2_name+".txt",encoding='utf8')
    count = 0
    differ = dict()
    for each_line in file1:
        line2 = file2.readline()
        count += 1
        if each_line != line2:
            len_line = len(each_line) if len(each_line) < len(line2) else len(line2)
            for i in range(len_line):
                if each_line[i] != line2[i]:
                    differ[count] = (i+1)
                    break
    print(file1_name + "共有" + str(count) + "行")
    count2 = 0
    # 重置指针，计算行数
    file2.close()
    file2 = open(file2_name+".txt",encoding='utf8')
    for each_line in file2:
        count2 += 1
    print(file2_name + "共有" + str(count2) + "行")
    file1.close()
    file2.close()
    for num in differ:
        print("第" + str(num)  + "行的第" + str(differ[num]) + "个字符不一样")
# file_differ()
############################################################
# def file_compare(file1, file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     count = 0  # 统计行数
#     differ = []  # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#     return differ
#
#
# file1 = input('请输入需要比较的头一个文件名：')
# file2 = input('请输入需要比较的另一个文件名：')
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print('两个文件完全一样！')
# else:
#     print('两个文件共有【%d】处不同：' % len(differ))
#     for each in differ:
#         print('第 %d 行不一样' % each)
# 2.
# 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，
# 程序实现如图：
def display():
    file_name = input("请输入文件名：")
    file = open(file_name + ".txt",encoding="utf8")
    N = input("请输入要打印的行数N：")
    count = 0
    for each_line in file:
        count += 1
        if count <= int(N):#注意字符串转数字
            print(each_line)
    file.close()
# display()
#################################################################
# def file_view(file_name, line_num):
#     print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
#     f = open(file_name)
#     for i in range(int(line_num)):
#         print(f.readline(), end='')
#
#     f.close()
#
#
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示该文件前几行：')
# file_view(file_name, line_num)
# 3.
# 呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，
# 用户可以随意输入需要显示的行数。
# （如输入13: 21
# 打印第13行到第21行，输入: 21
# 打印前21行，输入21: 则打印从第21行开始到文件结尾所有内容）
def file_display():
    file_name = input("请输入要打印的文件名")
    file = open(file_name + ".txt",encoding="utf8")
    num = input("请输入要打印的行，用\"：\"分隔")
    if ":" in num:
        print(num.split(sep = ":",maxsplit=2))
        (num1,num2) = num.split(sep = ":",maxsplit=2)
        if num2 != '':
            count = 0
            for each_line in file:
                count += 1
                if count >= int(num1) and count <= int(num2):
                    print(each_line)
        else:
            count = 0
            for each_line in file:
                count += 1
                if count >= int(num1):
                    print(each_line)
    else:
        for i in range(int(num)):
            print(file.readline())
    file.close()
# file_display()
####################################################
def file_view(file_name, line_num):
    if line_num.strip() == ':':
        begin = '1'
        end = '-1'

    (begin, end) = line_num.split(':')

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'

    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始到%s' % end
    elif end == '-1':
        prompt = '从%s到结束' % begin
    else:
        prompt = '从第%s行到第%s行' % (begin, end)

    print('\n文件%s%s的内容如下：\n' % (file_name, prompt))

    begin = int(begin) - 1
    end = int(end)
    lines = end - begin

    f = open(file_name,encoding='utf8')

    for i in range(begin):  # 用于消耗掉begin之前的内容
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(), end='')

    f.close()


# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
# file_view(file_name, line_num)
# 4.
# 编写一个程序，实现“全部替换”功能，程序实现如图：
def newfile_replace():
    file_name = input("请输入文件名：")
    file = open(file_name + ".txt",encoding='utf8')
    file_rep = open("record_replace.txt",'w',encoding='utf8')
    file_rep.close()
    file_rep = open("record_replace.txt",'a',encoding='utf8')
    file_reword = input("请输入要替换的单词或字符：")
    file_newword = input("请输入新的单词或字符：")
    count = 0
    word_len = len(file_reword)
    for each_line in file:
        for j in range(len(each_line) - word_len + 1):
            if each_line[j:(j + word_len)] == file_reword:
                count += 1
                each_line = each_line.replace(file_reword,file_newword)
        file_rep.write(each_line)
    print("文件" + file_name + "共有" + str(count) + "个[" + file_reword + "]")
    file.close()
    file_rep.close()
# newfile_replace()
###########################################################
def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name,encoding='utf8')

    content = []
    count = 0

    for eachline in f_read:
        if rep_word in eachline:
            count += eachline.count(rep_word)  # count感觉应该用这个
            eachline = eachline.replace(rep_word, new_word)
        content.append(eachline)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w',encoding='utf8')
        f_write.writelines(content)
        f_write.close()

    f_read.close()

file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)