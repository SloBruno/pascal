
from math import factorial

linhas = 5

for i in range(linhas):
    for j in range(i+1):
        n = factorial(i)//(factorial(j) * factorial(i-j))
        print(n, end='')
    print('')
    


    