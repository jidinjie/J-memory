import random
import string
#s = ""
#验证码
#for i in range(5):
#    print(string.digits)
    #prnit(string.ascii_uppercase)
#    for j in range(1 ):
#     print(string.ascii_uppercase)

#    all_chars =string.ascii_uppercase+string.digits
#    random_char = random.choice(all_chars)
#    print("random_char:",random_char)
#    s += random_char
#print(s)
#车牌号
#a = random.choice("ABCDE")
#b = random.choice(string.digits)
#c = random.choice(string.digits)
#d = random.choice(string.digits)
#print(f"琼B{a}{b}{c}{d}")
#s = random.randint(1,100)
#print(s)
count = 0
while count < 3:
    car_nums = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_uppercase+string.digits,5))
        car_num = f"琼{n1}-{n2}"
        car_nums.append(car_num)
        print(car_num)
        
    choice = input("输入你喜欢的号:").strip()
    if choice in car_nums:
        print(f"恭喜你选择了新车牌号：{choice}")
        exit("good luck")
    else:
        print("不合法的...")
    count += 1