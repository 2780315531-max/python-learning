i = 0
while i < 10:       #i<10----->循环条件
    print("人生")
    i += 1      #i=i+1
else:
    print("循环正常结束")

#案例：计算1-100之间有偶数的累加之和
total = 0       #记录累加之和
i =1        #循环开始数据

while i <= 100:
    if i % 2 == 0:  #偶数
        total += 1
    i += 1
print(f"1-100之间所有偶数的累加之和:{total}")