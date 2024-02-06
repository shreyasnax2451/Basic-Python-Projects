import random, time

def naive_search(search_ele, array):
    for i in range(len(array)):
        if array[i] == search_ele:
            return i
    return -1

def binary_search(search_ele, array, low, high):
    if high >= low:
        mid = (low+high)//2
        if array[mid] == search_ele:
            return mid
        elif array[mid] < search_ele:
            low = mid + 1
            return binary_search(search_ele, array, low, high)
        elif array[mid] > search_ele:
            high = mid - 1
            return binary_search(search_ele, array, low, high)
    else:
        return -1

if __name__ == '__main__':
    length = 1000
    new_list = [random.randint(-3*length, 3*length) for _ in range(length)]
    print(new_list)
    new_list.sort()
    search_ele = int(input("Enter the Number to Search: "))

    # Naive Search Time
    start = time.time()
    index_naive = naive_search(search_ele, new_list)
    end = time.time()
    print("Time Taken for Naive: {}".format(end-start))

    if index_naive != -1:
        print("The element is at {}th position".format(index_naive+1))
    else:
        print("Element Not Found!")

    # Binary Search Time
    low = 0
    high = len(new_list)
    start = time.time()
    index_binary = binary_search(search_ele, new_list, low, high)
    end = time.time()
    print("Time Taken for Binary: {}".format(end-start))

    if index_binary != -1:
        print("The element is at {}th position".format(index_binary+1))
    else:
        print("Element Not Found!")