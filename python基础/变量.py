#案例
base = 20.7 #基础播放量
increase = 50 #新增加播放量
print("未来一个月播放量:",base + increase)
print("未来两个月播放量:",base + increase + increase)


#升级：一次性可以定义多个变量
base,increase = 20.7,50
print("未来一个月播放量:",base + increase)
print("未来两个月播放量:",base + increase + increase)