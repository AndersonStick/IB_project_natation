import pygame  # Importa la librería pygame, que se utiliza para crear videojuegos en Python.
import sys  # Importa sys para manejar la salida del programa.

# Inicialización de pygame
pygame.init()  # Inicializa todos los módulos de pygame necesarios para ejecutar el juego.

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600  # Define el ancho y alto de la ventana del juego.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la ventana del juego con las dimensiones especificadas.
pygame.display.set_caption("Videojuego Educativo - Natación")  # Establece el título de la ventana.

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
