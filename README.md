# Simulación de la Máquina de Galton

 
##### Este proyecto simula el comportamiento de una máquina de Galton, donde las canicas caen a través de niveles y se distribuyen en contenedores. Al final, genera un gráfico que muestra cuántas canicas caen en cada contenedor. 

#### ¿Qué hace?
-   Generación de números aleatorios: Usamos la biblioteca `random` para decidir si cada canica cae a la izquierda o a la derecha en cada nivel. 
    
-   Gráficos: Con `matplotlib.pyplot`, creamos un gráfico de barras que muestra la cantidad de canicas en cada contenedor.

#### ¿Cómo funciona?

-   `def sim_galton(canicas, niveles):`
    
    -   Esta función toma dos argumentos: el número de canicas y el número de niveles de la máquina.
    -   Inicia la lista de contenedores en cero.
    -   Simula la caída de cada canica a través de los niveles y actualiza el contenedor correspondiente.

-   `def histograma(res):`
    
    -   Toma la lista que contiene la cantidad de canicas en cada contenedor y genera un gráfico de barras.
    -   Se añaden etiquetas y un título para que sea fácil de entender.
    -   Muestra la cantidad de canicas que hay por cada contenedor

### Acerca del Bootcamp
La experiencia adquirida hasta ahora ha sido muy importante. Cada clase, cada ejercicio y cada proyecto han sido oportunidades para aplicar lo que hemos aprendido. El enfoque práctico y sus explicaciones claras realmente han hecho la diferencia en mi comprensión del lenguaje y en mi habilidad para resolver problemas.
