print("--- 判断是否为闰年 ---")
year = input("请输入一个年份：")
while(year.isdigit()):
    year = int(year)
    if(year % 100 == 0):
        print(year,"年是闰年！")
    else:
        if(year % 100 != 0 and year % 4 == 0):
            print(year,"年是闰年")
        else:
            print(year,"年不是闰年！")
    print("输入非数字结束！")
    year = input("请输入一个年份：")