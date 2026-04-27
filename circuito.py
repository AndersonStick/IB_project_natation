import pygame  # Importa la librería pygame para crear videojuegos
import sys  # Importa sys para manejar la salida del programa

# Inicialización de pygame
pygame.init()  # Inicializa todos los módulos de pygame necesarios para ejecutar el juego

# Dimensiones de la ventana
WIDTH, HEIGHT = 1000, 800  # Define el ancho y alto de la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la ventana del juego con las dimensiones especificadas
pygame.display.set_caption("Videojuego Educativo - Natación")  # Establece el título de la ventana

# Colores
WHITE = (255, 255, 255)  # Color blanco
BLUE = (0, 0, 255)  # Color azul
SKIN_COLOR = (253, 221, 202)  # Color piel para el jugador
RED = (255, 0, 0)  # Color rojo para los puntos de control
GREEN = (0, 255, 0)  # Color verde para la meta y puntos alcanzados

# Crear el jugador (rectángulo)
player_width, player_height = 50, 50  # Dimensiones del jugador
player_x, player_y = WIDTH // 2, HEIGHT - 150  # Posición inicial del jugador (parte inferior de la pantalla)
player = pygame.Rect(player_x, player_y, player_width, player_height)  # Crear el rectángulo del jugador

# Velocidad del jugador
player_speed = 60  # Cantidad de píxeles que se moverá el jugador en cada dirección

# Circuito (puntos de control)
checkpoints = [
    pygame.Rect(200, 700, 100, 50),  # Punto de control 1
    pygame.Rect(800, 700, 100, 50),  # Punto de control 2
    pygame.Rect(800, 300, 100, 50),  # Punto de control 3
    pygame.Rect(200, 300, 100, 50)   # Punto de control 4
]
current_checkpoint = 0  # Índice del punto de control actual

# Crear la meta (rectángulo)
goal_width, goal_height = 100, 50  # Dimensiones de la meta
goal_x, goal_y = 500 - goal_width // 2, 100  # Posición de la meta (parte superior de la pantalla)
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)  # Crear el rectángulo de la meta

# Bucle principal
running = True  # Variable para controlar si el juego sigue ejecutándose
clock = pygame.time.Clock()  # Reloj para limitar los FPS

while running:
    screen.fill(BLUE)  # Rellenar la pantalla con color azul (agua)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
            running = False  # Salir del bucle principal

        if event.type == pygame.KEYDOWN:  # Detectar teclas presionadas
            if event.key == pygame.K_UP:  # Mover hacia arriba
                player.y -= player_speed
            if event.key == pygame.K_DOWN:  # Mover hacia abajo
                player.y += player_speed
            if event.key == pygame.K_LEFT:  # Mover hacia la izquierda
                player.x -= player_speed
            if event.key == pygame.K_RIGHT:  # Mover hacia la derecha
                player.x += player_speed
            if event.key == pygame.K_SPACE:  # Simular la acción de respirar
                print("Respirando...")

    # Verificar si el jugador está en el punto de control actual
    if current_checkpoint < len(checkpoints) and player.colliderect(checkpoints[current_checkpoint]):
        current_checkpoint += 1  # Avanzar al siguiente punto de control
        print(f"Punto de control {current_checkpoint} alcanzado")

        # Si se alcanzaron todos los puntos de control, activar la meta
        if current_checkpoint == len(checkpoints):
            print("¡Meta activada!")

    # Verificar si el jugador ha llegado a la meta
    if current_checkpoint == len(checkpoints) and player.colliderect(goal):  # Si el jugador colisiona con la meta
        print("¡Has llegado a la meta! Has ganado el juego.")
        running = False  # Terminar el juego

    # Dibujar los puntos de control
    for i, checkpoint in enumerate(checkpoints):
        color = GREEN if i < current_checkpoint else RED  # Cambiar el color según si el punto fue alcanzado
        pygame.draw.rect(screen, color, checkpoint)  # Dibujar el punto de control

    # Dibujar la meta
    pygame.draw.rect(screen, GREEN, goal)  # Dibujar la meta en color verde

    # Dibujar el jugador
    pygame.draw.rect(screen, SKIN_COLOR, player)  # Dibujar el rectángulo del jugador

    # Actualizar la pantalla
    pygame.display.flip()  # Actualizar el contenido de la ventana
    clock.tick(60)  # Limitar a 60 FPS

# Salir de pygame
pygame.quit()
sys.exit()