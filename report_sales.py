from typing import List

def ShopOLAP(N: int, items: List[str]) -> List[str]:
    done_dict = {}
    for string in items:
        item, count = string.split()
        if done_dict.get(item):
            done_dict[item] += int(count)
        else:
            done_dict[item] = int(count)
            
    reverse_done_dict = {}
    for key, value in sorted(done_dict.items()):
        if reverse_done_dict.get(value):
            reverse_done_dict[value].append(key)
        else:
            reverse_done_dict[value] = [key]

    done_list = []
    for i in sorted(reverse_done_dict.items(), reverse = True):
        for j in i[1]:
            done_list.append(f"{j} {i[0]}")

    return done_list
