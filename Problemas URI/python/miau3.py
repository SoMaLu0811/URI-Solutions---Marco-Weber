def primo(n):
    for i in range(2, n//2):
        if n%i==0:
            return False
        return True
n=0
while True:
    n+=1
    primo(n)
    if primo:
        print(n)    