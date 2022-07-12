from typing import List

def UFO(N: int, data: List[int], octal: bool) -> List[int]:
    system_convert = 16
    if octal:
        system_convert = 8

    return list(map(lambda x: int(str(x),system_convert), data))