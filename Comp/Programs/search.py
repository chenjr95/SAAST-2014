import random

def linear_search(seq, n):
    for i in range(0, len(seq)):
        if seq[i] == n:
            return i
    return-1

print linear_search(x1,22)

def bs_helper(seq, n, lo, hi):
    mid = (lo+hi)/2
    if lo>hi:
        return -1
    elif seq[mid] > n:
        return bs_helper(seq, n, lo, mid-1)
    elif seq[mid] < n:
        return bs_helper(seq, n, mid+1, hi)
    else:
        return mid
    
def binary_search(seq,n):
    return bs_helper(seq, n, 0, len(seq))

print binary_search(x1, 9)




def linear_search_count(seq, n):
    count = 0
    for i in range(0, len(seq)):
        count = count + 1
        if seq[i] == n:
            return count
    return count



def bs_helper_count(seq, n, lo, hi):
    mid = (lo+hi)/2
    if lo>hi:
        return 1
    elif seq[mid] > n:
        return 1 + bs_helper_count(seq, n, lo, mid-1)
    elif seq[mid] < n:
        return 1 + bs_helper_count(seq, n, mid+1, hi)
    else:
        return 1
    
def binary_search_count(seq,n):
    return bs_helper_count(seq, n, 0, len(seq))





x1= range(0,100000)

for i in range(0,10):
    n = random.randint(0,99999)
    print linear_search_count(x1,n)
    print binary_search_count(x1,n)


