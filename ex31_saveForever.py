# 测试题：
# 0.
# pickle的实质是什么？
#    pickle的实质是利用一些算法，将你的数据对象腌制成二进制文件，
# 存储在磁盘上，也可以放在数据库或者传到另一台电脑上
# 1.
# 使用pickle的什么方法存储数据？
#    pickle.dump(data, file), 第一个参数是待存储的数据对象，
# 第二个参数是目标存储的文件对象，注意要先使用“wb”的模式open文件
# 2.
# 使用pickle的什么方法读取数据？
#    pickle.load(file)
# 参数是目标存储的文件对象，注意要先使用“rb”模式open文件
# 3.
# 使用pickle能不能保存为“.txt”类型的文件？
#    可以，不过打开后是乱码，因为是以二进制的模式写入的
# 动动手：
# 0.
# 编写一个程序，这次要求使用pickle将文件里的对话按照以下要求腌制成不同文件
# （没错，是第29讲的内容小改，考考你自己能写出来吗？）
#        ·小甲鱼的对话单独保存为boy_ *.txt的文件（去掉“小甲鱼”）
#        ·小客服的对话单独保存为girl_ *.txt的文件（去掉“小客服”）
#        ·文件中总共有三段对话，分别保存为boy_1.txt，girl_1.txt，boy_2.txt，girl_2.txt，boy_3.txt，girl_3.txt共6个文件（提示：文件中不同的对话间已使用“ == == == == =”分割）
import pickle
def save(boy,girl,count):
    boy_file_name = 'ex31_boy_' + str(count) + ".txt"
    girl_file_name = 'ex31_girl_' + str(count) + '.txt'

    boy_file = open(boy_file_name,'wb')
    girl_file = open(girl_file_name,'wb')

    pickle.dump(boy,boy_file)
    pickle.dump(girl,girl_file)

    boy_file.close()
    girl_file.close()

def record_split():
    boy = []
    girl = []
    count = 1
    record_file = open("record.txt",encoding='utf8')
    for each_line in record_file:
        if each_line[:6] != "======":
            if each_line.split(sep=':')[0] == "小甲鱼":
                boy.append(each_line.split(sep=':')[1])
            else:
                if each_line.split(sep=':')[0] == "小客服":
                    girl.append(each_line.split(sep=':')[1])
        else:
            save(boy,girl,count)
            boy = []
            girl = []
            count += 1
    save(boy, girl, count)
    record_file.close()
# record_split()
# ################################################
import pickle


def save_file(boy, girl, count):
    file_name_boy = 'ex31_boy_' + str(count) + '.txt'
    file_name_girl = 'ex31_girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'wb')  # must wb
    girl_file = open(file_name_girl, 'wb')

    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    count = 1
    boy = []
    girl = []

    f = open(file_name,encoding='utf8')
    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1
    save_file(boy, girl, count)
    f.close()


# split_file('record.txt')
