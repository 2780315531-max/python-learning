"""
    案例2:猜数字
    1.系统随机生成一个随机数
    2.用户根据提示猜数字，并将所谓的数字输入
    3.如果猜错，系统提示猜大或猜小了，然后继续输入猜的数字
    4.如果猜对，系统自动退出，游戏结束
"""
import random
random_num = random.randint(1,100)#生成的随机数

while True:
#输入数字
    num = int(input("请输入一个数字:"))

#比较
    if num > random_num:
         print("你输入的数字太大了！")
    elif num < random_num:
        print("你输入的数字太小了！")
    else:
        print("恭喜你，猜到了")
        break

print("随机生成的数字：",random_num )


# 需求1 while版本：1~1000 所有5的倍数累加
total = 0
i = 1
while i <= 1000:
    if i % 5 == 0:
        total += i
    i += 1
print("1-1000所有5的倍数累加和：", total)



# 需求2 while版本：统计a和k的个数
str_data = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
a_count = 0
k_count = 0
index = 0
while index < len(str_data):
    char = str_data[index]
    if char == 'a':
        a_count += 1
    elif char == 'k':
        k_count += 1
    index += 1
print(f"a的数量：{a_count}，k的数量：{k_count}")