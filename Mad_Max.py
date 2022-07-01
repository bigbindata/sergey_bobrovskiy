from typing import List

def MadMax(N: int, Tele: List[int]) -> List[int]:
    if len(Tele) == 1:
        return Tele
    Tele=sorted(Tele, reverse = False)
    
    return Tele[:N//2]+Tele[:N//2-1:-1]