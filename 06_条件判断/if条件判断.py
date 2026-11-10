"""
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

#if...elif....eles...案例：根据用户输入的数字，判断数字是真数还是负数还是0
num = int(input("请输入数字:"))
if num > 0:
    print(f"{num}是个正数")
elif num < 0:
    print(f"{num}是负数")
else:
    print(f"{num}是0")  
"""

"""
#案例：根据输入的用户名和密码进行系统登入
username = input("请输入用户名:")
userpass = input("请输入密码:")

if username == "admin" and userpass == "6666":
    print("登入成功")
elif username == "root" and userpass == "66667":
    print("登入成功")
elif username == "zyk" and userpass == "12345":
    print("登入成功")
else:
    print("登入失败")
"""
"""
案例：三角形类型判断
1。构成三角形的条件:两边之和大于第三边
2.三边相等：等边三角形
两边相等：等腰三角形
三边都不相等：普通三角形
"""
"""
#第一种
#1.接收输入的三角形三个边的边长
a = int(input("请输入第一条边边长:"))
b = int(input("请输入第二条边边长:"))
c = int(input("请输入第三条边边长:"))
#判断三角形类型
if a == b == c:
    print("等边三角形")
elif a == b or b == c or a == c:
    print("等腰三角形")
else:
    print("普通三角形")


#第二种
a = int(input("请输入第一条边边长:"))
b = int(input("请输入第二条边边长:"))
c = int(input("请输入第三条边边长:"))
if a + b >c and a +c > b and b + c >a:
    if a == b and b == c:
        print(f"{a}{b}{c}这三个构成等边三角形~")
    elif a == b or b ==c or a == c:
        print(f"{a}{b}{c}这三个构成等腰三角形~")
    else:
        print(f"{a}{b}{c}这三个构成普通三角形~")
else:
    print(f"{a}{b}{c}这三个不能构成三角形！！")
"""
#练习：计算电费
#第一档：2880度以下，电费单价0.4883元/度
#第二档：2880-4800度，电费单价0.5383元/度
#第三档：4800度以上，电费单价0.7883元/度
# 获取输入用电度数
num = float(input("请输入年度用电度数："))
if num <= 2880:
    fee = num * 0.4883
elif num <= 4800:
    # 2880度按一档，剩下的按二档
    fee = 2880 * 0.4883 + (num - 2880) * 0.5383
else:
    # 一档全部 + 二档全部 + 超出4800部分三档
    fee = 2880 * 0.4883 + (4800 - 2880) * 0.5383 + (num - 4800) * 0.7883

print(f"总电费为：{fee:.2f} 元")



    
