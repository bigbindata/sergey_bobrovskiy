from typing import List

def TransformTransform(A: List[int], N: int) -> bool:
    B = []
    for i in range(N):
        for j in range(N-i):
            k = i + j
            max_number = 0
            for h in range(j, k+1):
                if max_number < A[h]:
                    max_number = A[h]
            B.append(max_number)
    BB = []
    for i in range(len(B)):
        for j in range(len(B)-i):
            k = i + j
            max_number = 0
            for h in range(j, k+1):
                if max_number < B[h]:
                    max_number = B[h]
            BB.append(max_number)
    summ = 0
    for x in range(len(BB)):
        summ += BB[x]
    if summ % 2 == 0:
        return True
    else:
        return False