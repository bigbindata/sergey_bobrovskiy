from typing import List

def MatrixTurn(Matrix:List[str], M:int, N:int, T:int) -> None:
    for a in range(M):
        Matrix[a] = list(Matrix[a])

    if M <= N:
        circles = M // 2
    else:
        circles = N // 2
    for k in range(T):  
        for m in range(circles): 
            for i in range(m + 1, N - m):
                if i == 1 + m:
                    a = Matrix[m][i - 1]
                else:
                    a = b
                b = Matrix[m][i]
                Matrix[m][i] = a
            for j in range(m + 1, M - m):
                a = b
                b = Matrix[j][N - m - 1]
                Matrix[j][N - m - 1] = a
            for q in range(N - m - 2, m - 1, -1):
                a = b
                b = Matrix[M - m - 1][q]
                Matrix[M - m - 1][q] = a
            for w in range(M - m - 2, m - 1, -1):
                a = b
                b = Matrix[w][m]
                Matrix[w][m] = a
    for i in range(M):
        Matrix[i] = ''.join(Matrix[i])
