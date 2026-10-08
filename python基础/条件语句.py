mood_index = int(input("蛋蛋今天的心情指数是:"))  #int只能接收整数
if mood_index >= 60:
    print("今晚可以打游戏")
else:   #mood_index < 60
    print("别打了！")