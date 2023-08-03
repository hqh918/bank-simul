with open("C:\\Users\hqh_c\Desktop\info.txt") as f1:
    date1 = f1.readlines()[0]  # 效验合法性
with open("C:\\Users\hqh_c\Desktop\info.txt") as f2:
    date2 = f2.readlines()[1]  # 账号
with open("C:\\Users\hqh_c\Desktop\info.txt") as f3:
    date3 = f3.readlines()[2]  # 密码
with open("C:\\Users\hqh_c\Desktop\info.txt") as f4:
    date4 = f4.readlines()[3]  # 余额
with open("C:\\Users\hqh_c\Desktop\info.txt") as f5:
    date5 = f5.readlines()[4]  # 剩余密码次数

'''------------------读取用户数据------------------'''

date1 = int(date1)
date2 = int(date2)
date3 = int(date3)
date4 = int(date4)
date5 = int(date5)

'''----------------将数据转换为int类型---------------'''

name = int(input('输入账号：'))

if name == date2:
    if date1 == 0:
        print('账户已被冻结')
    else:
        while date5 > 0:
            pw = int(input('输入密码['+str(date5)+']：'))
            if pw != date3:
                print('密码错误！')
                date5 = date5 - 1
                f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
                flist = f.readlines()
                flist[4] = ''+str(date5)+'\n'  # []里为行数，''内为内容
                f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
                f.writelines(flist)
            else:
                print('存款d')
                print('取款w')
                print('查询s')  # 功能提示
                opt = input('选择操作：')  # 选择要办理的业务
                if opt == 'd' or opt == 'w':
                    if opt == 'd':
                        dm = int(input('输入存款金额：'))
                        date4 = date4 + dm
                    else:
                        wm = int(input('输入取款金额['+str(date4)+']:'))
                        if wm > date4:
                            print('余额不足')
                            break
                        else:
                            date4 = date4 - wm
                    f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
                    flist = f.readlines()
                    flist[3] = ''+str(date4)+'\n'  # []里为行数，''内为内容
                    f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
                    f.writelines(flist)
                    print('成功！余额'+str(date4)+'元')
                    break
                elif opt == 's':
                    print('余额为：'+str(date4)+'')
                    break
        if date5 == 0:
            date1 = 0
            print('账户已被冻结')
            f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
            flist = f.readlines()
            flist[0] = ''+str(date1)+'\n'  # []里为行数，''内为内容
            f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
            f.writelines(flist)
else:
    print('未找到该账户！')
print('end')
