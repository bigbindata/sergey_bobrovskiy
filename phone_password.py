from typing import List

dict_coordinates = {6: (1,1),                   1: (1,2),                    9: (1,3),
                    5: (2,1),                   2: (2,2),                    8: (2,3),
                    4: (3,1),                   3: (3,2),                    7: (3,3)
                    }

def PatternUnlock(N: int, hits: List[int]) -> str:
    distance = 0
    if N <= 1 or len(hits) <= 1:
        return ""

    for index, number in enumerate(hits[1:],1):
        past_coordinates_height, past_coordinates_weght = dict_coordinates[hits[index-1]]
        current_coordinates_height, current_coordinates_weght = dict_coordinates[hits[index]]
        if (past_coordinates_height != current_coordinates_height) and (past_coordinates_weght != current_coordinates_weght):
            distance += 2**0.5
        else:
            distance += 1
    return str(round(distance, ndigits=5)).replace("0","").replace(".","")


