import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tkinter as tk
from tkinter import Frame

def draw_rectangle(ax, width, height):
    """Dibuja el rectángulo principal"""
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_xticks(range(0, width + 1, 1))
    ax.set_yticks(range(0, height + 1, 1))
    ax.set_aspect('equal')
    plt.grid(True)
    rect = patches.Rectangle((0, 0), width, height, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(rect)

def euclidean_tiling(width, height, ax, label_ax):
    """Dibuja la tilización y calcula el MCD con el paso a paso"""
    x, y = 0, 0  # Coordenadas iniciales
    original_width, original_height = width, height  # Guardar valores originales
    label_ax.clear()
    label_ax.axis('off')
    
    steps = []  # Lista para almacenar los pasos
    mcd = 0  # Inicializar MCD

    while height > 0 and width > 0:
        square_size = min(width, height)
        
        # Calcular el paso de Euclides
        division_result = width // height
        multiplication_result = height * division_result
        subtraction_result = width - multiplication_result
        
        step = f"{width} / {height} = {width / height:.2f} -> {division_result}\n"
        step += f"{height} * {division_result} = {multiplication_result}\n"
        step += f"{width} - {multiplication_result} = {subtraction_result}\n"
        steps.append(step)

        # Actualizar el panel izquierdo con los pasos
        label_ax.clear()
        label_ax.axis('off')
        label_ax.text(0, 0.5, '\n'.join(steps), fontsize=10, color='blue', ha='left', va='top')
        plt.draw()

        # Dibujar las baldosas (tilización)
        for i in range(0, width, square_size):
            for j in range(0, height, square_size):
                color = 'lightblue'
                if width == height:  # El último cuadrado (última tilización)
                    color = 'orange'
                rect = patches.Rectangle((x + i, y + j), square_size, square_size, 
                                         linewidth=1.5, edgecolor='black', facecolor=color)
                ax.add_patch(rect)
                plt.pause(0.5)  # Pausa para visualizar el proceso

        # Reducir el área a cubrir
        if width > height:
            width -= square_size
            x += square_size
        else:
            height -= square_size
            y += square_size

    mcd = square_size  # El MCD final es el tamaño del último cuadrado
    label_ax.text(0.5, 0.5, f"MCD: {mcd}", fontsize=14, color='red', ha='center', va='center')
    label_ax.axis('off')
    plt.draw()

def create_interface():
    """Crea la interfaz gráfica"""
    root = tk.Tk()
    root.title("Tiling Rectangle with Euclidean Algorithm")
    
    # Panel izquierdo para entrada
    left_panel = Frame(root)
    left_panel.grid(row=0, column=0, padx=10, pady=10)
    
    base_label = tk.Label(left_panel, text="Base:")
    base_label.grid(row=0, column=0, padx=5, pady=5)
    base_entry = tk.Entry(left_panel)
    base_entry.grid(row=0, column=1, padx=5, pady=5)
    
    height_label = tk.Label(left_panel, text="Altura:")
    height_label.grid(row=1, column=0, padx=5, pady=5)
    height_entry = tk.Entry(left_panel)
    height_entry.grid(row=1, column=1, padx=5, pady=5)
    
    def on_submit():
        base = int(base_entry.get())
        altura = int(height_entry.get())
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].axis('off')  # Panel izquierdo donde se muestra el texto
        draw_rectangle(ax[1], base, altura)
        euclidean_tiling(base, altura, ax[1], ax[0])  # Llamamos a la función con los ejes
        plt.show()

    submit_button = tk.Button(left_panel, text="Calcular", command=on_submit)
    submit_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

# Ejecutar la interfaz
create_interface()
