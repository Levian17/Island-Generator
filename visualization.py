import numpy as np
import matplotlib.pyplot as plt

def visualizacion_3D(matrix): # Representa la matriz en 3D
    # Basados en la shape de la matriz creamos los valores X e Y
    x = np.arange(matrix.shape[1])
    y = np.arange(matrix.shape[0])
    X, Y = np.meshgrid(x, y)

    # Creamos la figura en modo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, matrix, cmap='terrain')
    plt.show()

def visualizacion_2D(matrix): # Representa la matriz en 2D
    plt.matshow(matrix, cmap='terrain')
    plt.show()