"""第 1 天：猜数字游戏

运行：python3 day01_guess_number.py
"""
import random

answer = random.randint(1, 100)
count = 0
print("我想了一个 1~100 的数字，你猜猜看！")

while True:
    raw = input("请输入你的猜测（输入 q 退出）：").strip()
    if raw.lower() == "q":
        print(f"答案是 {answer}，下次再见~")
        break
    if not raw.isdigit():
        print("请输入一个整数哦。")
        continue
    guess = int(raw)
    count += 1
    if guess < answer:
        print("小了，再大一点")
    elif guess > answer:
        print("大了，再小一点")
    else:
        print(f"猜对啦！你一共猜了 {count} 次。")
        break
