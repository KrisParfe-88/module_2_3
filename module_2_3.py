my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = 0
while True:
    if ind < len(my_list) and my_list[ind] > 0:
        print(my_list[ind])
        ind += 1
        continue

    elif ind < len(my_list) and my_list[ind] == 0:
        ind += 1
        continue

    else:
        break