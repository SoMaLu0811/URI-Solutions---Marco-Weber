from sys import stdin 
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)):
        if n%i==0:
            return False
        return True
n = int(stdin.readline())
primo(n)
if primo(n):
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')