#Problem:
#Given two sorted arrays, find the kth element in 2 arrays combined.
#(when we say kth we expect element present at k-1th position ignoring the duplicates)
#
#Algorithm (Recursive):
#FIND_KTH(A, B, K)
#1. IF K < 0 or K > len of A + len of B, THEN No Solution
#2. IF any of array is of ZERO length, THEN K-1th element of other Array
#3. IF Last Element of A is smaller than First Element of B 
#	IF K is greater than length of Array A
#	THEN (K - 1 - Len of A)th Element of B
#	ELSE (K-1)th Element of A
#   Vice-Versa for Last(B) and First(A)
#4. a = Len(A)/2, b = Len(B)/2
#5. IF K is less than or equal to a + b 
#   THEN IF IF A(a) <= B(b) THEN We need to search our K element only in 
#		A, First_Half(B) Call  Fun Recursively 
#        ELSE IF A(a) > B(b) THEN FIND_KTH(FIRST_HALF(A), B, K)
#   ELSE IF K is greater than a + b
#   THEN IF A(a) <= B(b) THEN FIND_KTH(SECOND_HALF(A), B, K-Len of Deducted Part of A)
#   ELSE Vice-Versa
#
#
#if Len(A) and Len(B) are M, N respectevely
#then run-time complexity of this algo would be of order of (logM + logN) 



def find_kth(arr, brr, k):
   a_len = len(arr)
   b_len = len(brr)
   if k <= 0 or k > a_len + b_len : return -1
   if b_len ==0: return arr[k-1]
   if a_len == 0: return brr[k-1] 
   if k == a_len + b_len : return max(arr[-1], brr[-1])
   #if a_len == 1: return max(arr[0], brr[k-2])
   #if b_len == 1: return max(arr[k-2], brr[0])  
   if arr[-1] <= brr[0]: 
       if k > len(arr): return brr[k - len(arr) - 1]
       else: return arr[k-1]
   if brr[-1] <= arr[0]: 
       if k > len(brr): return arr[k - len(brr) - 1]
       else: return brr[k-1]
   a = len(arr)/2
   b = len(brr)/2
   if k <= a + b :
       if arr[a-1] <= brr[b-1] : return find_kth(arr, brr[:b], k)
       else: return find_kth(arr[:a], brr, k)
   else:
       if a == 0: a = 1
       elif b == 0: b = 1
       if arr[a-1] <= brr[b-1] : return find_kth(arr[a:],brr,k-a)
       else : return find_kth(arr, brr[b:], k - b)
