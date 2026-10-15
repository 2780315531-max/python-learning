#获取键盘上输入的数据 -- input(..)
#name = input("请输入你的名字：")
#age = input("请输入你的年龄：")
#print(f"大家好，我是{name}，今年{age}岁")

#案例：ATM机取款
#总金额
total_money = 10000
#输入密码
password = input("请输入密码：")
print(f"您输入的密码是：{password}")
#取款金额
withdraw_money = int(input("请输入取款金额："))#num转化为int类型--->int(..)
#计算余额
balance = total_money - withdraw_money
print(f"您取款{withdraw_money}元，余额为{balance}元")


num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
#将输入的字符串转化为int类型
num1 = int(num1)
num2 = int(num2)
#计算两个数字的和
sum = num1 + num2
print(f"两个数字的和为：{sum}")
