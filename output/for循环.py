#(1)
#s = "hello ji"
#for i in s:
#    print("hello ji")
#    print(i) 
#I = [1,2,3,4,5,6,7,8,9,10]
#for i in I:
#    print(i)

#for i in range(1,101):
#    print(i)

#for i in range(2,101,2):
#    print(i)

#for i in range(100,0,-1):
#    print(i)
#(2)
#girl_age = 26
#    guess = int(input("请输入你的猜测："))
#    if guess > 26:
#        print("你讨厌...")
#    elif guess < 26:
#        print("你好坏...")
#    else:
#        exit("猜对了...")    
#for i in range(100):
#    if i % 2 == 0:
#     print("偶数",i)
#    else: 
#     print("奇数",i)
#(3)
#for i in range(1,6):
#    print(f"--------{i}层-------")
#    for j in range(9):
#        print(f"L{i}-{i}0{j}室")
#(4)打印三角形
for i in range(10):
    if i <=5:
     print("*"*i)
    else:
       print((10-i)*"*")