import datetime
with open("C:\\Users\hqh_c\Desktop\info.txt") as f1:
    date1 = f1.readlines()[0]  # 获取账户状态
with open("C:\\Users\hqh_c\Desktop\info.txt") as f2:
    date2 = f2.readlines()[1]  # 获取账号
with open("C:\\Users\hqh_c\Desktop\info.txt") as f3:
    date3 = f3.readlines()[2]  # 获取密码
with open("C:\\Users\hqh_c\Desktop\info.txt") as f4:
    date4 = f4.readlines()[3]  # 获取余额
with open("C:\\Users\hqh_c\Desktop\info.txt") as f5:
    date5 = f5.readlines()[4]  # 获取剩余密码次数

'''------------------获取用户数据------------------'''

date1 = int(date1)
date2 = int(date2)
date3 = int(date3)
date4 = int(date4)
date5 = int(date5)

'''----------------将数据转换为int类型---------------'''

datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')  # 获取当前时间并存储到datetime1
name = int(input('输入账号：'))
if name == date2:
    fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
    print('时间:', datetime1, '   操作：尝试登录', file=fp)
    fp.close()
    if date1 == 0:
        datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
        print('时间:', datetime1, '   操作：登录失败，该账户已被冻结', file=fp)
        fp.close()
        print('账户已被冻结')
    else:
        while date5 > 0:
            pw = int(input('输入密码['+str(date5)+']：'))
            if pw != date3:
                datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                print('时间:', datetime1, '   操作：密码输入错误', file=fp)
                fp.close()
                print('密码错误！')
                date5 = date5 - 1
                f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
                flist = f.readlines()
                flist[4] = ''+str(date5)+'\n'  # []里为行数，''内为内容
                f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
                f.writelines(flist)
            else:
                f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
                flist = f.readlines()
                flist[4] = '3\n' 
                f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
                f.writelines(flist)
                datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                print('时间:', datetime1, '   操作：登录成功', file=fp)
                fp.close()
                print('存款d')
                print('取款w')
                print('查询s')  # 功能提示
                opt = input('选择操作：')  # 选择要办理的业务
                if opt == 'd' or opt == 'w' or opt == 'D' or opt == 'W':
                    if opt == 'd' or opt == 'D':
                        datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                        fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                        print('时间:', datetime1, '   操作：尝试存款', file=fp)
                        fp.close()
                        dm = int(input('输入存款金额：'))
                        date4 = date4 + dm
                        datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                        fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                        print('时间:', datetime1, '   操作：存款'+str(dm)+'元', file=fp)
                        fp.close()

                    else:
                        datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                        fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                        print('时间:', datetime1, '   操作：尝试取款', file=fp)
                        fp.close()
                        wm = int(input('输入取款金额['+str(date4)+']:'))
                        if wm > date4:
                            datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                            fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                            print('时间:', datetime1, '   操作：余额不足，取款失败', file=fp)
                            fp.close()
                            print('余额不足')
                            break
                        else:
                            datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                            fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                            print('时间:', datetime1, '   操作：取款'+str(wm)+'元', file=fp)
                            fp.close()
                            date4 = date4 - wm
                    f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
                    flist = f.readlines()
                    flist[3] = ''+str(date4)+'\n'  # []里为行数，''内为内容
                    f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
                    f.writelines(flist)
                    print('成功！余额'+str(date4)+'元')
                    break
                elif opt == 's':
                    datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                    fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
                    print('时间:', datetime1, '   操作：查询余额', file=fp)
                    fp.close()
                    print('余额为：'+str(date4)+'')
                    break
        if date5 == 0:
            date1 = 0
            datetime1 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
            fp = open('C:\\Users\hqh_c\Desktop\history.txt', 'a+')
            print('时间:', datetime1, '   操作：密码错误次数过多，该账户被冻结', file=fp)
            fp.close()
            print('账户已被冻结')
            f = open('C:\\Users\hqh_c\Desktop\info.txt', 'r+')
            flist = f.readlines()
            flist[0] = ''+str(date1)+'\n'  # []里为行数，''内为内容
            f = open('C:\\Users\hqh_c\Desktop\info.txt', 'w+')
            f.writelines(flist)
else:
    print('未找到该账户！')
print('end')
