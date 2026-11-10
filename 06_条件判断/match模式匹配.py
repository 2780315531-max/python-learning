#match...case模式匹配:工作日程安排
day = input("请输入星期几(1-7):")

match day:
    case "1":
        print("周一:工作会议日")
    case "2":
        print("周二:学习培训日")
    case "3":
        print("周三:项目开发日")
    case "4":
        print("周四:代码审查日")
    case "5":
        print("周五:总结规划日")
    case "6" | "7":
        print("输入有误")

#案例：基于match...case 实现一个简易计算器
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
oper = input("请输入运算符(+ - * /):")

match oper:
    case "+":
       print(f"{num1} + {num2} = {num1 + num2}")      #`pass` 是一个**空语句**，作用：**什么都不做，占位**
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}") 
    case "/" if num2 != 0:      #if条件成立，才匹配这个case
        print(f"{num1} / {num2} = {num1 / num2}") 
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}") 
    case _:
        print(操作不支持) 
    
# 游戏角色移动控制系统
cmd = input("请输入指令：")

if cmd == "上" or cmd == "w" or cmd == "W":
    print("角色向上移动")
elif cmd == "下" or cmd == "s" or cmd == "S":
    print("角色向下移动")
elif cmd == "左" or cmd == "a" or cmd == "A":
    print("角色向左移动")
elif cmd == "右" or cmd == "d" or cmd == "D":
    print("角色向右移动")
elif cmd == "跳" or cmd == " ":
    print("角色跳跃")
elif cmd == "攻击" or cmd == "j" or cmd == "J":
    print("角色发动攻击")
elif cmd == "退出" or cmd == "esc" or cmd == "ESC":
    print("角色退出游戏")
else:
    print("无效指令")
