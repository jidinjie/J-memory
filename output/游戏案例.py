while True:
 print("""
 进入第一关：
 选择：
  1.攻击 
  2.购买装备
""")
 experience = 10
 choice1 = input("请输入你的选择：")
  #choice1 = input("请输入你的选择：")
 if choice1=="1":
   print("进攻...")
   experience += 10
   print("experience",experience)
 elif choice1=="2":
   print("发起攻击...")
   experience += 10
   print("experience",experience)


#引导用户是否继续
 choice2 = input("""
      1.回到第一关
      2.退出游戏
      3.继续
""")
 if choice2=="1":
   continue
 elif choice2=="2":
   break

 print("""
 进入第二关：
 选择：
  1.前进
  2.查看地图
  3.回城
""")

 choice3 = input("请输入你的选择：")
 if choice3=="1":
   print("前进...")
   experience += 10
   print("experience",experience)
 elif choice3=="2":
   print("查看地图...")
   experience += 10
   print("experience",experience)
 elif choice3=="3":
   print("回城...")
   experience += 10
   print("experience",experience)

 break
print("process end")