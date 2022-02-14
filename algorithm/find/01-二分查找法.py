def binary_search(list_name, item):
    low = 0
    high = len(list_name) - 1
    while low <= high:
        mid = (low+high)/2
        guess = list_name[int(mid)]
        # print("mid值为%d，guess值为%d" % (int(mid), guess))
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 10, 11]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
