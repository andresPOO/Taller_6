import numpy as np
import matplotlib.pyplot as plt

'''
import numpy as np: Importa la biblioteca NumPy bajo el alias np. NumPy es una biblioteca de Python 
para cálculos numéricos que proporciona estructuras de datos y funciones para trabajar con matrices y 
arreglos de manera eficiente.
import matplotlib.pyplot as plt: Importa la subbiblioteca pyplot de Matplotlib bajo el alias plt. Matplotlib 
es una biblioteca de trazado en 2D de Python que produce figuras de alta calidad en una variedad de formatos y 
entornos.'''

def mandelbrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    
''' def mandelbrot(h, w, maxit=20, r=2):: Define una función llamada mandelbrot que toma cuatro 
parámetros: h y w que representan la altura y el ancho de la imagen, maxit que representa el 
número máximo de iteraciones y r que representa el radio máximo de divergencia.'''

    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)
    
    '''x = np.linspace(-2.5, 1.5, 4*h+1): Crea un arreglo unidimensional x que contiene 4*h+1 puntos 
    igualmente espaciados en el rango de -2.5 a 1.5.'''
    
    
y = np.linspace(-1.5, 1.5, 3*w+1): Crea un arreglo unidimensional y que contiene 3*w+1 puntos igualmente espaciados en el rango de -1.5 a 1.5.
A, B = np.meshgrid(x, y): Crea una malla bidimensional A y B usando los arreglos x e y respectivamente.
C = A + B*1j: Crea una matriz compleja C combinando A y B como partes real e imaginaria respectivamente.
z = np.zeros_like(C): Crea una matriz z de la misma forma que C pero llena de ceros.
divtime = maxit + np.zeros(z.shape, dtype=int): Crea una matriz divtime de la misma forma que z pero llena con el valor de maxit y de tipo entero."

for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    '''for i in range(maxit):: Comienza un bucle que itera maxit veces.
z = z**2 + C: Actualiza los valores de z utilizando la fórmula del conjunto de Mandelbrot.
diverge = abs(z) > r: Encuentra los puntos donde la magnitud de z excede r.
div_now = diverge & (divtime == maxit): Encuentra los puntos que están divergiendo ahora y que no 
han divergido antes.
divtime[div_now] = i: Actualiza los tiempos de divergencia de los puntos que están divergiendo ahora.
z[diverge] = r: Evita que los valores de z diverjan demasiado.'''
    
    
return divtime
'''return divtime: Devuelve la matriz divtime, que contiene los tiempos de divergencia de cada punto en la cuadrícula.'''

plt.clf()
plt.imshow(mandelbrot(400, 400))

'''plt.clf(): Borra la figura actual.
plt.imshow(mandelbrot(400, 400)): Muestra la imagen generada por la función 
mandelbrot con una resolución de 400x400 píxeles.'''