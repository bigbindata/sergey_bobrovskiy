from typing import List

def MadMax(N: int, Tele: List[int]) -> List[int]:
    sorted(Tele)
    return Tele[:N//2]+Tele[:N//2-1:-1]
