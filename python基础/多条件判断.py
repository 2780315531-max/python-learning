#BMI = 体重 / （身高 ** 2）
usere_weight = float(input("请输入您的体重 (单位:kg):"))
usere_height = float(input("请输入您的身高 (单位:m):"))
usere_BMI = usere_weight / (usere_height) ** 2
print("您的BIM值为:" + str(usere_BMI))

#偏瘦： user_BMI<=18.5
#正常: 18.5 < user_BMI<=25
#偏胖：:25 <= user_BMI <=30
#肥胖： user_BMI > 30
if usere_BMI <= 18.5:
    print("偏瘦")
elif 18.5 < usere_BMI <= 25:
    print("正常")
elif 25 < usere_BMI <= 30:
    print("偏胖")
else:
    print("肥胖")