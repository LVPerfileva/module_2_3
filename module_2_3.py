my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
_index = -1
while _index < len(my_list):
    _index += 1
    if _index == len(my_list):
        break
    if my_list[_index] > 0:
        print(my_list[_index])
    elif my_list[_index] == 0:
        continue
    else:
        break
