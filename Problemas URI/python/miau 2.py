def amp_enter():
    amp_test = int(input())
    if amp_test > 9:
        amp_test = 9
    return amp_test
    
def caso():
    amp = amp_enter()
    freq = int(input())
    return amp, freq

def amp_print(amp):
    lt = []
    
    for x in range(amp):
        lt.append(x+1)
    for x in lt:
        print(f"{x}"*x)

    lt.reverse()
    lt.remove(amp)
    for x in lt:
        print(f"{x}"*x)

    
def caso_print(amp, freq):
    for x in range(freq):
        print("")
        amp_print(amp)


def entrada():    
    n_casos = int(input())
    entrada_final = []
    for i in range(n_casos):
        print("")
        caso_i = caso()
        entrada_final.append(caso_i)
    return entrada_final

lista_casos = entrada()

for x in range(len(lista_casos)):
    caso_in = lista_casos[x]
    caso_print(caso_in[0], caso_in[1])
