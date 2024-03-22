while True:
 print("""
  1.前进
  2.攻击 
  3.购买装备
  4.查看地图
  5.回城
""")

 choice = input("请输入你的选择：")
 if choice=="1":
   print("前进...")
 elif choice=="2":
   print("发起攻击...")
 elif choice=="3":
   print("购买装备...")
 elif choice=="4":
   print("查看地图...")
 elif choice=="5":
   print("回城...")
 elif choice > "5":
   print("没有指令...")

#for i in range(1,6):
#    print(f"--------{i}层-------")
#    for j in range(9):
#        print(f"L{i}-{i}0{j}室")