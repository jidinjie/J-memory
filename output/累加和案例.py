#ret = 0
#for i in range(1,101):
#    ret += i
#print(ret)

#ret = 0
#for i in range(1,101):
#    if i % 2==0:
#        ret += i
#    else:
#        pass
#print(ret)


ret = 0
for i in range(1,101):
    if i % 13==0:
        print("i",i)
        ret += i
    else:
        pass
print(ret)