#Problem: Find kth smallest element in a given random array of integers.
#(ignore the case of duplicates, kth means element in kth position in sorted array)
#
#Selection Algorithm:
#Look Wikipedia for the algorithm
#http://en.wikipedia.org/wiki/Selection_algorithm
#Its similar to Quick-sort

import random

def part(arr, l, r, p):
    p_val = arr[p]
    arr[p], arr[r] = arr[r], arr[p]
    ind = l
    for i in range(l,r+1):
	if arr[i] < p_val:
	    arr[i], arr[ind] = arr[ind], arr[i]
            ind += 1
    arr[ind], arr[r] = arr[r], arr[ind]
    return ind

def select(arr, l, r, k):
    if l == r: return arr[l]
    p = random.randint(l,r)
    new_p = part(arr, l, r, p)
    pivot = new_p -l + 1
    if pivot == k: return arr[new_p]
    elif pivot < k :
	return select(arr, new_p + 1, r, (k - pivot))
    else:
        return select(arr, l, new_p - 1, k)

def find_kth(arr,k):
    l = 0
    r = len(arr) - 1
    return select(arr, l, r, k)
