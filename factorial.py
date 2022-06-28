def squirrel(N:int)->int:
    """Return first digit from factorial number"""
    fact = 1
    for i in range(1,N+1):
        fact = fact * i
    return int(str(fact)[0])
