"""
    案例1:根据输入的用户名密码执行登入操作，具体要求如下：
    1.正确的用户名和密码为admin/666888、zheng/123456、taoge/886886
    2.输入用户名和密码进行登入，直到登入成功，程序结束运行；如果登入失败，则继续输入用户名和密码进行登入
    3.输入的用户名和密码不能为空！
    4.登入成功：输出“登入成功”
    5.登入失败：输出“用户名和密码错误，请重新输入”
"""
#1. `while True:` 后面所有代码都要往右缩进（4 个空格）
#2. `if / elif / else:` 下面的代码，再往右缩进一格
#break:只能在循环中出现，表示结束跳出循环
#continue:只能在循环中出现,表示中断本循环，进行下一次循环
while True:
    #接收输入的用户名和密码
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")

    # 判断: 不能为空
    if username == "" or password == "":
        print("用户名或密码不能为空！")
        continue  # 这一行必须缩进在if里面！

    # 判断账号密码
    if username == "admin" and password == "666888":
        print("登入成功")
        break
    elif username == "zheng" and password == "123456":
        print("登入成功")
        break
    elif username == "taoge" and password == "886886":
        print("登入成功")
        break
    else:
        print("用户名和密码错误，请重新输入")

