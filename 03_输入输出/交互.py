#BMI = 体重 / （身高 ** 2）
usere_weight = float(input("请输入您的体重 (单位:kg):"))
usere_height = float(input("请输入您的身高 (单位:m):"))
usere_BMI = usere_weight / (usere_height) ** 2
print("您的BIM值为:" , usere_BMI)