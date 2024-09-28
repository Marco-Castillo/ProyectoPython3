import random
import matplotlib.pyplot as plt

def sim_galton(canicas, niveles):
    cont = [0] * (niveles + 1)
    for _ in range(canicas):
        pos = 0  
        for _ in range(niveles):
            mov = random.choice([0, 1])
            pos += mov 
        cont[pos] += 1
    return cont

def histograma(res):
    plt.bar(range(len(res)), res)
    plt.xlabel('Contenedores')
    plt.ylabel('Canicas')
    plt.title('Máquina de Galton')
    plt.xticks(range(len(res)))
    plt.grid(axis='y')
    plt.show()


canicas = 3000
niveles = 12

grafica = sim_galton(canicas, niveles)
histograma(grafica)