from random import randint

def partition(arr, lo ,hi):
    idx = randint(lo,hi)
    arr[idx], arr[hi] = arr[hi], arr[idx]
    i = lo
    pivot = arr[hi]
    for j in range(lo,hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[hi]  = arr[hi], arr[i]
    return i
    
def quick(arr,lo, hi,k):
    pos = partition(arr, lo, hi)
    if pos+1<k:
        return quick(arr, pos+1, hi, k)
    elif pos+1>k:
        return quick(arr, lo, pos-1, k)
    else:
        return arr[pos]

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k = int(input())
    res = quick(arr, 0 ,n-1, k)
    print(res)
    
    
