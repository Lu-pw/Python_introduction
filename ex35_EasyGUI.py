# 0.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# 图形用户界面入门：EasyGui，也就是我们常说的GUI编程，（GUI：Graphical
# User Interface）。
#
# easygui官网：http: // easygui.sourceforge.net/easygui
# 各功能的使用请查阅：EasyGui学习文档
# https://blog.csdn.net/qq_41556318/article/details/84433698
#
# 动动手
# 0.
# 先练练手，把我们的刚开始的那个猜数字小游戏加上界面吧？
#
import random
# noinspection PyUnresolvedReferences
import easygui as g

# g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
# secret = random.randint(1, 10)
# msg = "不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）："
# title = "数字小游戏"
# guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
# while True:
#     if guess == secret:
#         g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
#         g.msgbox("哼，猜中了也没有奖励！")
#         break
#     else:
#         if guess > secret:
#             g.msgbox("哥，大了大了~~~")
#         else:
#             g.msgbox("嘿，小了，小了~~~")
#         guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
#
# g.msgbox("游戏结束，不玩啦^_^")
#
# 1.
# 如下图，实现一个用于登记用户账号信息的界面（如果是带 * 号的必填项，
# 要求一定要有输入并且不能是空格）。
# msg = "请填写以下联系方式！"
# title = "账号中心"
# fieldNames = ["*用户名","*真实姓名","固定电话","*手机号码","QQ","E-mail"]
# fieldValues = []
# fieldValues = g.multenterbox(msg,title,fieldNames)
# while 1:
#     if fieldValues == None:
#         break
#     errmsg = ""
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == "" and option[0] == "*":
#             errmsg += ('[%s]为必填项。\n\n' % fieldNames[i])
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
# print("用户资料如下：%s" % str(fieldValues))
#####################################################################
# import easygui as g
#
# msg = "请填写以下联系方式"
# title = "账号中心"
# fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
# fieldValues = []
# fieldValues = g.multenterbox(msg, title, fieldNames)
#
# while 1:
#     if fieldValues == None:
#         break
#     errmsg = ""
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == "" and option[0] == "*":
#             errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
#
# print("用户资料如下：%s" % str(fieldValues))
#
# 实现效果如下：
#
#
#
# 当有带 * 号的信息未填写就按下OK时，会弹出题目所示提示窗口，并继续输入信息。
#
# 2.
# 提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容。
# import os
# import sys
# file_list = g.fileopenbox()
# with open(file_list,encoding='utf8') as f1:
#     content = f1.read()
#     title = "文件[%s]的内容如下：" % f1
#     g.msgbox(content,title)
####################################################
# import easygui as g
# import os
#
# file_path = g.fileopenbox(default="*.txt")
#
# with open(file_path, encoding='utf-8') as f:
#     title = os.path.basename(file_path)
#     msg = "文件【%s】的内容如下：" % title
#     text = f.read()
#     g.textbox(msg, title, text)
# 3.
# 在上一题的基础上增强功能：当用户点击“OK”按钮的时候，比较当前文件是否修改过，
# 如果修改过，则提示“覆盖保存”、”放弃保存”或“另存为…”并实现相应的功能。
# （提示：解决这道题可能需要点耐心，因为你有可能会被一个小问题卡住，
# 但请坚持，自己想办法找到这个小问题所在并解决它！）
# import os
# file_path = g.fileopenbox(default="*.txt")
# with open(file_path,encoding='utf8') as f:
#     file_name = os.path.basename(file_path)
#     title = os.path.basename(file_path)
#     msg = "文件【%s】的内容如下："% title
#     text_old = f.read()
#     text_after = g.textbox(msg,title,text_old)
# if text_old != text_after:
#     choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：","警告",("覆盖保存","放弃保存","另存为.."))
#     if choice == "覆盖保存":
#         f = open(file_path,'w',encoding='utf8')
#         f.write(text_after)
#         f.close()
#     if choice == "放弃保存":
#         pass
#     if choice == "另存为..":
#         another_path = g.filesavebox(default=".txt")
#         if os.path.splitext(another_path)[1] != '.txt':
#             another_path += '.txt'
#         with open(another_path,'w',encoding='utf8') as new_file:
#             new_file.write(text_after)
#
###################################################################
# 答：这道题会出现的一个小问题就是
# easygui.textbox
# 函数会在返回的字符串后边追加一个行结束符（“\n”），
# 因此在比较字符串是否发生改变的时候我们需要人工将这个行结束符忽略。
# （但是貌似我现在使用的版本没有这个问题，所以我将其代码改了）
#
# import easygui as g
# import os
#
# file_path = g.fileopenbox(default="*.txt")
#
# with open(file_path, encoding='utf-8') as old_file:
#     title = os.path.basename(file_path)
#     msg = "文件【%s】的内容如下：" % title
#     text = old_file.read()
#     text_after = g.textbox(msg, title, text)
#
# if text != text_after:  # text_after[:-1]
#     # 小甲鱼的答案说textbox 的返回值会追加一个换行符，我运行的结果不会，
#     故将text_after[:-1]改为了text_after
#
#     choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
#     if choice == "覆盖保存":
#         with open(file_path, "w", encoding='utf-8') as old_file:
#             old_file.write(text_after)  # text_after[:-1]
#     if choice == "放弃保存":
#         pass
#     if choice == "另存为...":
#         another_path = g.filesavebox(default=".txt")
#         if os.path.splitext(another_path)[1] != '.txt':
#             another_path += '.txt'
#         with open(another_path, "w", encoding='utf-8') as new_file:
#             new_file.write(text_after)  # text_after[:-1]
# 另外，Python构建文本文档的默认编码方式为GB2312，但是我们自己写的txt文档的
# 编码方式为utf - 8，在读取文件信息时须注意。建议一直使用utf - 8的编码方式。
#
# 就算在构建一个新的文档并写入时，也可以改为utf - 8的编码方式：
#
# file = open('newfile.txt', 'w', encoding='utf-8')
#
# file.write('你好，AoboSir.')
#
# file.close()
#
# 这里新建的newfile.txt就是以utf - 8的编码方式，
# 与我们自己右键新建的编码方式相同，在读取时：
# file = open('newfile.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()
# 这样就可以避免编码出错而报错
#
# 4.
# 写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
# 要求一：递归搜索各个文件夹
# 要求二：显示各个类型的源文件和源代码数量
# 要求三：显示总行数与百分比
# 截图1：
#
#
#
# 截图2：
# import os
# import easygui as g
# target = ['.c','.cpp','.py','.txt',".asm",'.cc']
# code_dict = dict()
# code_num = {'.txt':0,".py":0}
# def search_file(floder):
#     os.chdir(floder)
#
#     for each in os.listdir(os.curdir):
#         if os.path.isdir(each):
#             search_file(each)
#             os.chdir(os.pardir)
#         else:
#             if os.path.splitext(each)[1] in target:
#                 code_dict.setdefault(os.path.splitext(each)[1],0)
#                 code_dict[os.path.splitext(each)[1]] += 1
#                 with open(each,encoding='utf-8') as f:
#                     try:
#                         for each_line in f:
#                             code_num[os.path.splitext(each)[1]] += 1
#                     except:
#                         pass
# floder = g.diropenbox()
# search_file(floder)
# text = ""
# code_count = 0
# for each in code_dict:
#     text += ("[%s]文件共有%s个，源代码%s行"%(each,code_dict[each],code_num[each])) + "\n"
#     code_count += int(code_num[each])
# title = "统计结果"
# msg = "您目前共写了%d行代码，完成进度：%.2f%%\n离2万行代码还差%d" \
#       "行，请继续努力！"%(code_count,(code_count / 100000) * 100,(100000
#                                                          - code_count))
# g.textbox(msg,title,text)

#######################################################################
#
# import easygui as g
# import os
#
#
# def show_result(start_dir):
#     lines = 0
#     total = 0
#     text = ""
#
#     for i in source_list:
#         lines = source_list[i]
#         total += lines
#         text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines)
#     title = '统计结果'
#     msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total / 1000, 100000 - total)
#     g.textbox(msg, title, text)
#
#
# def calc_code(file_name):
#     lines = 0
#     with open(file_name,encoding = "utf8") as f:
#         print('正在分析文件：%s ...' % file_name)
#         try:
#             for each_line in f:
#                 lines += 1
#         except UnicodeDecodeError:
#             pass  # 不可避免会遇到格式不兼容的文件，这里忽略掉......
#     return lines
#
#
# def search_file(start_dir):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             lines = calc_code(each_file)  # 统计行数
#             # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
#             # 统计文件数
#             try:
#                 file_list[ext] += 1
#             except KeyError:
#                 file_list[ext] = 1
#             # 统计源代码行数
#             try:
#                 source_list[ext] += lines
#             except KeyError:
#                 source_list[ext] = lines
#
#         if os.path.isdir(each_file):
#             search_file(each_file)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
#
#
# target = ['.c', '.cpp', '.py', '.cc',".txt", '.java', '.pas', '.asm']
# file_list = {}
# source_list = {}
#
# g.msgbox("请打开您存放所有代码的文件夹......", "统计代码量")
# path = g.diropenbox("请选择您的代码库：")
#
# search_file(path)
# show_result(path)
