#task2
from bisect import bisect_left
from bisect import bisect_right

def binarysearch(s,x):
    fun=bisect_left(s,x)
    if fun == len(s):
        print("Righ index")
    else: print("Not found")    
s=[1,1,9,8,2,35,9,0,4,6]
x= int(7)
binarysearch(s,x)

#task1

list1=[1,1,9,8,2,8,2,9,9,35,9,0,4,6]
unorderedset= list(dict.fromkeys(list1))
print(unorderedset)