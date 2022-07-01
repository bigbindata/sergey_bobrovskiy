import random
from typing import List

def generate_ids_and_salary(N):

    ids = []
    salary = []
    for _ in range(N):
        number = random.randint(1,100000)
        salary.append(random.randint(1,100000))
        while number in ids:
            number = random.randint(1,10000)
        ids.append(number)
    return ids, salary

def SynchronizingTables(N: int, ids: List[int], salary: List[int]) -> List[int]:
    if N == 1:
        return salary
    return [dict(zip(sorted(ids), sorted(salary)))[i] for i in ids]
