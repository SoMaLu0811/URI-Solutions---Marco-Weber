a = 0
casos = int(input())
print("")

for x in range(casos + 1):
    amplitude = int(input())
    repeticoes = int(input())
    print("")
    for y in range(repeticoes + 1):
        for z in range(amplitude + 1):
            a += 1
            print(f"{a}"*a)
        for r in range(amplitude):
            a -= 1
            print(f"{a}"*a)
            
    a = 0
    print("")