#    Name: Ghasadiya Manthan
#    ID: 201951065
#    Section: 2-B

import time 
import random
def insertionSort(ele): 
	for i in range(1, len(ele)): 
		up = ele[i] 
		k = i - 1
		while k >=0 and ele[k] > up: 
			ele[k + 1] = ele[k] 
			k -= 1
		ele[k + 1] = up	 
	return ele			
def bucketSort(array):
    arr = []
    num = 10

    #2D array, containing 10 buckets/array
    for i in range(num):
        arr.append([])

    #creating index of particular bucket
    #and appending that value in bucket simultaneously
    for i in array:
        index = int(num * i)
        arr[index].append(i)

    #quicksort to solve each bucket
    for i in range(num):
        arr[i] = insertionSort(arr[i])
    
    #Updating the given array to sorted array
    k = 0
    for i in arr:
        for j in i:
            array[k] = j
            k += 1
    
    return array
 

# Driver code:
array = []
for i in range(10):
    array.append(round(random.uniform(0 , 1) , 4))
print("GIVEN ARRAY IS: ", array)
# count run time
bucketSort(array)
print("SORTED ARRAY IS: ", array)
# print("time taken for 2000 elements is: ", t2-t1, "sec")
# print("time taken in microseconds is: ", (t2-t1)*1000000, "micro sec")