from itertools import permutations

def BiggerGreater(input: str) -> str:
    perm = list(sorted(set(''.join(chars) for chars in permutations(input))))
    index_input = perm.index(input)
    if perm[-1] == input:
        return ""
    return perm[index_input+1]