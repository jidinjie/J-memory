height = float(input("请输入您的身高【m】："))
weight = float(input("请输入您的体重【kg】："))
BMI = weight/height**2
print(BMI)
if BMI <= 18.5:
    print("偏瘦")
elif BMI < 24:
    print("正常")
elif BMI < 28:
    print("超重")
#else: 
elif BMI > 28:
    print("肥胖")