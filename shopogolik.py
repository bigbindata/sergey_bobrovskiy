from typing import List

def MaximumDiscount(N: int, price:List[int]) -> int:
    price = sorted(price,reverse = True)
    return sum(price[2::3])