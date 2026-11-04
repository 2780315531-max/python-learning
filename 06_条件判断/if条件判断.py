#if基础语法
#if条件判断：如果分数超过680，上清华
score = int(input("请输入你的分数："))
if score > 680:
    print("上清华")
    print("也恭喜你即将踏入精彩的大学生活")
print("不管你是否上清华，大学生活都很精彩")


#案例：完成B登入功能的实现（正确账号和密码为：188888/8888）
#1.接收用户账号和密码
ok_accout = 188888
ok_passsword = 8888
accout = int(input("请输入您的账户:"))
password  = int(input(" 请输入您的密码:"))

#2.判断账户和密码是否正确，如果正确则登入成功
if accout == ok_accout and password == ok_passsword:
    print("登入成功")
    print("进入B站")

#3.判断账户密码是否有误，如果有任一错误，则登入失败，提醒错误
if accout != ok_accout or password != ok_passsword:
    print("登入失败") 
    print("账号或密码错误")


#if.....else
k_accout = 188888
ok_passsword = 8888
accout = int(input("请输入您的账户:"))
password  = int(input(" 请输入您的密码:"))
if accout == ok_accout and password == ok_passsword:
    print("登入成功")
    print("进入B站")
else:
    print("登入失败") 
    print("账号或密码错误")


#根据用户输入的数字判断数字是奇数还是偶数
e = int(input("请输入一个数字:"))
if e % 2 == 0:
    print("偶数")
else:
    print("奇数")


#根据用户输入的年龄，判断用户是否成年
y = int(input("请输入你的年龄："))
if y >= 18:
    print("成年")
else:
    print("未成年")

#根据用户输入的数字，判断数字是正数还是负数
num1 = int(input("请输入一个数字:"))
if num1 > 0:
    print("正数")
else:
    print("负数")

#根据用户输入的分数，判断该分是否及格了
num2 = int(input("请输入你的分数:"))
if num2 >= 60:
    print("及格")
else:
    print("不及格")

