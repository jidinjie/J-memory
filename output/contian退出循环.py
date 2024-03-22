#for i in range(1,11):
#    #print(i)
    #if i == 6:
#    if i == 6 or i == 8:
       #break
#        continue
#    print(i)
    #break
#print("process end")
for i in range(1,6):
    print(f"-------{i}层------")
    if i == 3:
        print("-")
        continue
    for j in range(1,9):
        if i == 4 and j == 4:
            print("遇到鬼了。。。")
            break
        #if i == 3:
        #    print("-")
            #continue
        print(f"L{i}-{i}0{j}室")