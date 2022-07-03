from typing import List

def SumOfThe(N: int, data: List[int]) -> int:
    if N == 1:
        return data[0]
    for index, number in enumerate(data):
        if number == sum(data[:index]+data[index+1:]):
            return number