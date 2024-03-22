#冒泡排序bubble
import random
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
li = [random.randint(0,100)for i in range(100)]
print(li)
bubble_sort(li)
#print(li)
#选择排序select
def select_sort_simple(li):
    li_new=[]
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


#def select_sort(li):
#    for i in range(len(li)-1):
 #       min_local = i
  #      for j in range(i,len(li)):
   #         if li[j] < li[min_local]:
    #            min_local = j
     #   li[i],li[min_local] = li[min_local],li[i]
      #  print(li)
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i,len(li)):
            if li[j] < li[min_loc]:
                min_loc=j
        li[i],li[min_loc] = li[min_loc],li[i]
        print(li)

li = [3,2,4,1,5,6,7,9,8]
print(li)
print(select_sort(li))
#插入排序
def insert_sort(li):
    for i in range(1,len(li)):#摸到的牌的下标
        tmp = li[i]
        j = i-1  #j手里摸到的牌
        while j >= 0 and li[j]>tmp:
            li[j+1] = li[j] 
            j -= 1
        li[j+1] = tmp
        print(li)
li = [2,3,1,5,4,9,8,7,6]
print(li)
insert_sort(li)
#快速排序
def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:#从右边找比tmp小的数
            right -= 1  #往左走一步
        li[left]=li[right]#把右边的值写到左边空位上
        #print(li,'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]#把左边的值写到右边空位
        #print(li,'left')
    li[left] = tmp  #把tmp归位
    return left

def quick_sort(li,left,right):
    if left<right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)


li=[5,7,4,6,3,8,1,2,9]
#print(li)
#partition(li,0,len(li)-1)
quick_sort(li,0,len(li)-1)
print(li)
#堆排序
def sift(li,low,high):#li:列表，low：堆的堆顶位置，high：堆的最后一个元素的位置
    i=low  #i最开始指向根节点
    j=2*i + 1 #左子节点
    tmp = li[low] #把堆顶存起来
    while j<=high: #只要j位置有数，
        if j+1 <= high and li[j+1]>li[j]: #如果右还在有且比较大
            j = j+1 #j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j   #往下看一层
            j = 2*i+1
        else:  #tmp更大，把tmp放到i的位置
            li[i] = tmp # 把tmp放到某一级领导的位置
            break 
    else:
        li[i] = tmp #把tmp放到叶节点上

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):
        #i表示建堆的时候调整的部分的根的下标
        sift(li,i,n-1)
        #建堆完成
        for i in range(n-1,-1,-1):
            #i指向当前堆的最后一个元素
            li[0],li[i]=li[i],li[0]
            sift(li,0,i-1)  #i-1是新的high
        #print(li)

li=[i for i in range(100)]
import random
random.shuffle(li)
print(li)
heap_sort(li)
#print(li)
#归并排序
def merge(li,low,mid,high):
    i = low
    j = mid+1
    ltmp =[]
    while i <=mid and mid<=high: #只要左右两边都有数 
        if li[i] < li[j]:
           ltmp.append(li[i])
           i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <=mid:
        ltmp.append(li[i])
        i += 1
    while j <=high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp
#li = [2,4,5,8,1,3,6,9]
#merge(li,0,3,7)
#print(li)
    

def merge_sort(li,low,high):
     if low < high: #至少有俩
         mid = (low + high)//2
         merge_sort(li,low,mid)
         merge_sort(li,mid+1,high)
         merge(li,low,mid,high)

li = list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)

#希尔排序
def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):#摸到的牌的下标
        tmp = li[i]
        j = i-gap  #j手里摸到的牌
        while j >= 0 and li[j]>tmp:
            li[j+gap] = li[j] 
            j -= gap
        li[j+gap] = tmp
        #print(li)
def shell_sort(li):
    d = len(li)//2
    while d >=1:
        insert_sort_gap(li,d)
        d //=2

li = list(range(1000))
import random
random.shuffle(li)
shell_sort(li)
print(li)

#计数排序
def count_sort(li,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0,100)for _ in range(1000)]
print(li)
count_sort(li)
print(li)
#
def count_sort(li,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)
import random
li = [random.randint(0,100) for _ in range(1000)]
print(li)
count_sort(li)
print(li)
#桶排序
def bucket_sort(li,n=100,max_num=10000):
    buckets = [[] for _ in range(n)]# 创建桶
    for var in li:
        i = min(var // (max_num // n),n-1)#i 表示var放到几号桶里
        buckets[i].append(var)
        #保持桶内有序
        for j in range(len(buckets[i]-1),0,-1):
            if buckets[i][j] < buckets[i][j-1]:
               buckets[i][j],buckets[i][j-1]= buckets[i][j-1],buckets[i][j]
            else:
                break
    sort_li= []
    for buc in buckets:
        sort_li.extend(buc)
        return sort_li

import random
li= [random.randint(0,10000) for i in range(100000)]
li = bucket_sort(li)
print(li)    
#基排序
def radix_sort(li):
    max_num = max(li) # 最大值99 -> 2,888->3,10000->5
    it = 0
    while 10**it <= max_num:
        buckets = [[]for _ in range(10)]
        for var in li:
            #987 it = 1 987//10->98 98%10->8; it=3 987//100->9 9%10=9  
            digit = (var // 10** it)%10
            buckets[digit].append(var)
        #分桶完毕
        li.clear()
        for buc in buckets:
            li.extend(buc)
        #把数重新写回li 
             
        it += 1

import random
#random.shuffie(li)
li = list(range(1000))
random.shuffie(li)
radix_sort(li)
print(li)