def white_walkers(village: str) -> bool:
    list_vil = []
    for i in range(0, len(village)):
        if village[i].isdigit() == True:
            list_vil.append(int(village[i]))
        elif village[i] == "=":
            list_vil.append(village[i])
    k = 0
    b = 0
    for j in range(0, len(list_vil)-4):
        if type(list_vil[j]) == int:
            k += list_vil[j]
            if type(list_vil[j+4]) == int:
                k += list_vil[j+4]
                if k == 10:
                    b += 1
            k = 0
    midle_list = []
    num_of_couple = 0
    for q in range(0, len(list_vil)):
        if type(list_vil[q]) == int:
            midle_list.append(list_vil[q])
    for p in range(0, len(midle_list)-1):
        if (midle_list[p] + midle_list[p+1]) == 10:
            num_of_couple += 1
    
    if (b == num_of_couple) and b != 0:
        return True
    else:
        return False