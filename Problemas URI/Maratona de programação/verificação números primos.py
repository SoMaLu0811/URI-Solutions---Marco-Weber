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
    saida = 'é primo'
else:
    saida = 'não é primo'
print(f"O número {n} {saida}")