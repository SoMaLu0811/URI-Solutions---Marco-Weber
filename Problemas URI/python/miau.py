n = int(input())
carga_somada = 0
lista = []
for x in range(n):
    f = int(input())
    for y in range(f):
        z = input().split()
        t_cural, animais, compatili  = int(z[0]), int(z[1]), int(z[2])
        media = t_cural/animais
        premio_per_a = media*compatili
        premio_total = premio_per_a*animais
        carga_somada += premio_total
    lista.append(int(carga_somada))
    carga_somada = 0
for i in range(len(lista)):
    print(lista[i])
