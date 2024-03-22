def sift(li,low,high):#li:列表，low：堆的堆顶位置，high：堆的最后一个元素的位置
    i=low  #i最开始指向根节点
    j=2*i + 1 #左子节点
    tmp = li[low] #把堆顶存起来
    while j<=high: #只要j位置有数，
        if j+1 <= high and li[j+1]<li[j]: #如果右还在有且比较大
            j = j+1 #j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j   #往下看一层
            j = 2*i+1
        else:  #tmp更大，把tmp放到i的位置
            break 
        li[i] = tmp
def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(li)-1):
        if li[i]>heap[0]:
           heap[0]=li[i]
           sift(heap,0,k-1)
    #print(heap)
    for i in range(k-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap,0,i-1)
    return heap

#li=[i for i in range(100)]
import random
li=list(range(1000))
random.shuffle(li)
#print(li)
print(topk(li,10))
#print(li)