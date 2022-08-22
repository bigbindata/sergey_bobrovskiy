from typing import List

def Football(F:List[int], N:int) -> bool:
    change = True
    for i in range(N-1):
        if F[i] > F[i+1]:
            change = False
    if change:
        return False
    index_x = -1
    index_y = -1
    counter = 0
    for x in range(len(F)-1):
        if F[x] > F[x+1]:
            if index_x == -1:
                index_x = x
                index_y = x+1
                counter += 1
            else:
                index_y = x + 1
                counter += 1
    if counter < 3 and index_x != -1 and index_y != -1:
        F[index_x], F[index_y] = F[index_y], F[index_x]
        counter = -1
    change = True
    for i in range(N-1):
        if F[i] > F[i+1]:
            change = False
    if change:
        return True
    else:
        if counter == -1:
            F[index_x], F[index_y] = F[index_y], F[index_x]
    if change is False:
        if index_x == 0:
            line_F = (index_y - (index_x)) // 2
        else:
            line_F = (index_y - (index_x - 1)) // 2
        for i in range(index_x, index_y + 1):
            if i <= line_F:
                F[i], F[index_y + index_x - i] = F[index_y - index_x - i], F[i]
    change = True
    for i in range(N-1):
        if F[i] > F[i+1]:
            change = False
    return change