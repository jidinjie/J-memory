#from cal_time import *
#顺序查找
def linear_search(li,val):
    for ind,v in enumerate(li):
     if v==val:
        return ind
     else:
        return None
 #二分查找
def binary_search(li,val):
   left = 0
   right = len(li) - 1
   while left <= right:
      mid = (left + right)//2
      if li[mid] == val:
         return mid
      elif li[mid] >val:
          right = mid - 1
      else:
         left = mid + 1
   else:
      return None
li = list(range(10000))
print(linear_search(li,3000))
print(binary_search(li,3000))