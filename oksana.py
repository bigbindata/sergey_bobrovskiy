from typing import List

def odometer(data: List[int])-> int:
    "Return distanse from start"
    distance = 0

    for i in range(0, len(data), 2):
        if i == 0:
            distance += data[i]*data[i+1]
        else:
            distance += data[i]*(data[i+1]-data[i-1])

    return distance