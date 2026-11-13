#for关注的是遍历每一个元素
#for循环：遍历输入的字符串

msg = input("请输入需要遍历的字符串:")

for s in msg:
    print(f"元素:{s}")
else:
    print("遍历结束！")

#案例：计算1-100之间所有奇数之和
total = 0

for i in range(1,101):
    if i % 2 == 1:
        total += i
print("1-100之间的奇数累加之和:",total)

#简化
total = 0

for i in range(1,101,2):
    total += i
print("1-100之间的奇数累加之和:",total)

#案例2:计算100-500之间所有3的倍数的数字之和
total = 0
for i in range(100,501):
    if i % 3 == 0:      #i是3的倍数
        total += i
print("100-500之间所有3的倍数的数字之和:",total)

#range(..)语句用法：
#range(end),range(start,end),range(start,end,step)
