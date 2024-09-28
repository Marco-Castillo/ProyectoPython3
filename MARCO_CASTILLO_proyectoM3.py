# Se importa biblioteca ramdom para generar numeros aleatorios
import random
#se importa biblioteca matplotib.pyplot para la generación de graficos
import matplotlib.pyplot as plt
#Se crea una función para colocar 2 los argumentos de canicas y niveles
def sim_galton(canicas, niveles):
    #Se inicializa una lista que contiene elementos inicializados en 0
    cont = [0] * (niveles + 1)
    #se inicia el bucle que repetirá el numero de canicas para simular su caida
    for _ in range(canicas):
        #se indica que la variable inicia en 0 y comienza en la parte superior de la máquina
        pos = 0  
        #se inicia el bucle que repetirá el numero de canicas atraves de los niveles
        for _ in range(niveles):
             #se utiliza para indicar aleatoriamente si la canica cae en la izquiera o la derecha
            mov = random.choice([0, 1])
            #incrementa en 1 si el movimiento de la canica es a la derecha o permanece igual si es a la izquierda
            pos += mov 
            # Después de que la canica ha pasado por los niveles, se incrementa en el contenedor segun la posición indicando que ha caido en ese contenedor
        cont[pos] += 1
    #Devuelve la lista contenedores, que contiene la cantidad de canicas en cada contenedor
    return cont
#Se crea una función que toma el argumento que tiene la lista con la candidad de canicas en cada contenedor
def histograma(res):
    # Crea un gráfico de barras, donde el eje X representa los contenedores y el eje Y el numero de canicas en el contenedor
    plt.bar(range(len(res)), res)
    #Se agrega el nombre de la etiqueta en el eje X
    plt.xlabel('Contenedores')
    #Se agrega el nombre de la etiqueta en el eje Y
    plt.ylabel('Canicas')
    #Se agrega el nombre de la etiqueta título
    plt.title('Máquina de Galton')
    #Las etiquetas del eje X muestran todos los contenedores
    plt.xticks(range(len(res)))
    # Se añade cuadriculas en el eje Y para mejorar la legibilidad
    plt.grid(axis='y')
    # Se añade iterancia para mostrar la cantidad de canicas por contenedor
    for i, cant in enumerate(res):
        # Se ajusta el espacio entre el numero y la barra
        plt.text(i, cant + 1, str(cant), ha='center')

    # Se muestra el grafíco en una nueva ventana
    plt.show()

# Variable para la cantidad de canicas
canicas = 3000
# Variable para la cantidad de niveles
niveles = 12
#se llama a la función simulación y posteriormente se guarda en grafica
grafica = sim_galton(canicas, niveles)
# Se llama a la función para realizar la grafíca
histograma(grafica)