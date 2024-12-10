import tkinter as tk
from tkinter import ttk
from generation_new import generation
from visualization import visualizacion_3D, visualizacion_2D

# Parametros basicos de TKinter
root = tk.Tk()
root.title('Island Generator')
root.geometry('325x325+1200+150')
frame = ttk.Frame(root, padding=10)
frame.grid()

# Variables de los Scales
tamanho = tk.IntVar()
num_nodos = tk.IntVar()
dimension = tk.IntVar()

# Elementos de la GUI
tk.Label(frame, text="Tamaño", font=("Arial", 10)).grid(column=1, row=0)
tk.Scale(frame, length=300, from_=20, to=200, orient='horizontal', tickinterval=20, variable=tamanho, resolution=10).grid(column=1, row=1, pady=(0, 15))

tk.Label(frame, text="Numero de nodos", font=("Arial", 10)).grid(column=1, row=3)
tk.Scale(frame, length=300, from_=1, to=10, orient='horizontal', variable=num_nodos).grid(column=1, row=4, pady=(0, 15))

tk.Label(frame, text="Dimensiones", font=("Arial", 10)).grid(column=1, row=6, )
tk.Scale(frame, length=300, from_=2, to=3, orient='horizontal', variable=dimension, takefocus=True).grid(column=1, row=7, pady=(0, 15))

tk.Button(frame, text='Generar', command=lambda: modo_vision(generation(tamanho.get(), num_nodos.get()), dimension.get())).grid(column=1, row=9, pady=(10, 0))
# Funcion asociada al boton
def modo_vision(matrix, dimension): # Selecciona al modo de visualizacion correspondiente
    visualizacion_2D(matrix) if dimension == 2 else visualizacion_3D(matrix)  

root.mainloop()