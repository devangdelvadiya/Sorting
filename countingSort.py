#    Name: Ghasadiya Manthan
#    ID: 201951065
#    Section: 2-B

import time
import random

def countSort(array):
    # declare length of array
    n = len(array)
    
    # find maximum element from array
    Max = max(array)

    # count array of length man+1 and with all elements 0
    count = [0 for i in range(Max+1)]

    # final array with all element 0 and size of main array(n)
    farray = [0 for i in range(n)]
    
    # store count of each character
    for i in array:
        count[i] += 1
    temp = 1
    while temp<= Max:
        count[temp] += count[temp-1]
        temp += 1
    for i in range(n-1,-1,-1):
        farray[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
    for i in range(n):
        array[i] = farray[i]
# Driver code:
array = []
for i in range(10000):
    array.append(random.randint(1,10000))
# count run time
t1 = time.time()
countSort(array)
t2 = time.time()
print("time taken for 10000 elements is: ", t2-t1, "sec")
print("time taken in microseconds is: ", (t2-t1)*1000000, "micro sec")
