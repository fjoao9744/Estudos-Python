lista1 = [
    [1, 2, 3] ,
    [4, 5, 6] ,
    [7, 8, 9] ,
    ]


print('''\033[34;40;1m  0 1 2 
0\033[30;40;0m 1 2 3
\033[34;40;1m1\033[30;40;0m 4 5 6
\033[34;40;1m2\033[30;40;0m 7 8 9
\033[30;40;0m
      ''')


n = list(input('que posição você deseja acessar?'))
n1 = int(n[0])
n2 = int(n[2])



print(lista1[n1][n2])



