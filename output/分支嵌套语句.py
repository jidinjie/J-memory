#pid = input("请输入您的身份证号：")

#if len(pid)==18:
   #print("打印个人基本信息")
   #num = int(pid[17])
   #if num % 2 == 0:
   #   print("性别：女性")
   #else:
   #   print("性别：男性")
   #jiGuanCode = pid[:6]
   #print("jiGuanCode",jiGuanCode)
   #if jiGuanCode=="110000":
   #   print("籍贯：北京")
   #elif jiGuanCode=="120000":
   #   print("籍贯：天津")  
   #elif jiGuanCode=="310000":
    #  print("籍贯：上海")
   #elif jiGuanCode=="460200":
    #  print("籍贯：海南")
   #else:
   #   print("不是直辖市！")
#else:
 #     print("输入位数有误！")
#print("程序结束！")


girl_age = 26
guess= int(input("请输入你的猜测："))
if guess > 26:
   print("你讨厌。。。")
elif guess< 26:
   print("你好坏....") 
else:
   print("猜对了")
print("end...")