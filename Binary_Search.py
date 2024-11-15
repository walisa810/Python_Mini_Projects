import random
import time
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
        
    return -1
def binary_search(l, target):
    length = len(l)
    low = 0
    high = length - 1
    while( low <= high ):
        mid = low + (high - low)//2
        
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    
    length = 1000

    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))

    sorted_list = sorted(list(sorted_list))


    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()

    print("Naive_search time: ", (end-start)/length ," seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()

    print("Binary_search time: ", (end-start)/length ," seconds")

          
