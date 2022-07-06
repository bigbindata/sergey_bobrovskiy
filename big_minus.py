from math import fabs

def BigMinus(s1: str, s2: str) -> str:
    return str(int(fabs(int(s1) - int(s2))))
