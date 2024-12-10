import matplotlib.pyplot as plt
import numpy as np
from random import randint

def generation(world_size: int, node_number: int) -> np.array:
    # Generamos una matriz de las dimensiones deseadas
    matriz = np.zeros((world_size, world_size))
    # Definimos altura y probabilidad de descenso (a futuro puede que estos parametros se obtengan en la GUI)
    altura: int = 10; probabilidad_descenso:float = 0.575

    '''Declaramos la lista con las opciones a expandir.
    Una opcion tiene posicion x, posicion y, ademas de altura de su opcion original
    
    >>> (4, 5, 3), posicionado en (4, 5) y su opcion origen tenia 3 de altura'''
    options: list[tuple] = []

    # Generamos los nodos dentro de la matriz
    for _ in range(node_number):
        # Se genera una posicion dentro de las dimensiones de la matriz
        x, y = randint(0, world_size-1), randint(0, world_size-1)
        matriz[x][y] = altura # Se asigna el valor de altura a la posicion 
        options.append((x, y, altura)) # Se anade la opcion a opciones

    # Recorremos las opciones (la lista va a aumentar mientras se recorre)
    for option in options:
        x, y, altura_org = option[0], option[1], option[2] 
        
        if x > 0: # Si no esta fuera del limite de la matriz
            # Si la altura es menor que la de la casilla anterior y mayor que 0
            if matriz[x-1][y] < altura_org and matriz[x-1][y] >= 0:
                # Si supera la probabilidad de descenso
                if randint(0, 100) < probabilidad_descenso * 100:
                    matriz[x-1][y] = altura_org-1
                    options.append((x-1, y, altura_org-1))
                else:
                    matriz[x-1][y] = altura_org
                    options.append((x-1, y, altura_org))

        if y > 0: # Si no esta fuera del limite de la matriz
            # Si la altura es menor que la de la casilla anterior y mayor que 0
            if matriz[x][y-1] < altura_org and matriz[x][y-1] >= 0:
                # Si supera la probabilidad de descenso
                if randint(0, 100) < probabilidad_descenso * 100:
                    matriz[x][y-1] = altura_org-1
                    options.append((x, y-1, altura_org-1))
                else:
                    matriz[x][y-1] = altura_org
                    options.append((x, y-1, altura_org))

        if x < world_size-1: # Si no esta fuera del limite de la matriz
            # Si la altura es menor que la de la casilla anterior y mayor que 0
            if matriz[x+1][y] < altura_org and matriz[x+1][y] >= 0:
                # Si supera la probabilidad de descenso
                if randint(0, 100) < probabilidad_descenso * 100:
                    matriz[x+1][y] = altura_org-1
                    options.append((x+1, y, altura_org-1))
                else:
                    matriz[x+1][y] = altura_org
                    options.append((x+1, y, altura_org))

        if y < world_size-1: # Si no esta fuera del limite de la matriz
            # Si la altura es menor que la de la casilla anterior y mayor que 0
            if matriz[x][y+1] < altura_org and matriz[x][y+1] >= 0:
                # Si supera la probabilidad de descenso
                if randint(0, 100) < probabilidad_descenso * 100:
                    matriz[x][y+1] = altura_org-1
                    options.append((x, y+1, altura_org-1))
                else:
                    matriz[x][y+1] = altura_org
                    options.append((x, y+1, altura_org))

    return matriz