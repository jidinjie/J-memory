#count = 100
#while count > -1 :
   #print("hello ji")
#   print(count)
   #print("count",count)
#   count -= 1
   #print(count)
count = 0
while count < 3:
    count += 1
    guess = int(input("请输入你的猜测："))
    if guess > 26:
       print("你讨厌...")
    elif guess < 26:
        print("你好坏...")
    else:
        exit("猜对了...")   