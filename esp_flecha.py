import pygame  # Importa la librería pygame, que se utiliza para crear videojuegos en Python.
import sys  # Importa sys para manejar la salida del programa.

# Inicialización de pygame
pygame.init()  # Inicializa todos los módulos de pygame necesarios para ejecutar el juego.

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600  # Define el ancho y alto de la ventana del juego.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la ventana del juego con las dimensiones especificadas.
pygame.display.set_caption("Videojuego Educativo - Natación")  # Establece el título de la ventana.

# Colores
WHITE = (255, 255, 255)  # Color blanco
BLUE = (0, 0, 255)  # Color azul
SKIN_COLOR = (253, 221, 202) # Color piel para el jugador
RED = (255, 0, 0)  # Color rojo para el circuito

# Crear el jugador (rectángulo)
player_width, player_height = 50, 50  # Dimensiones del jugador
player_x, player_y = WIDTH // 2, HEIGHT // 2  # Posición inicial del jugador (centro de la pantalla)
player = pygame.Rect(player_x, player_y, player_width, player_height)  # Crear el rectángulo del jugador

# Velocidad del jugador
player_speed = 5  # Cantidad de píxeles que se moverá el jugador

# Crear la meta (rectángulo)
goal_width, goal_height = 100, 50  # Dimensiones de la meta
goal_x, goal_y = WIDTH // 2 - goal_width // 2, 100  # Posición de la meta (parte superior del circuito)
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)  # Crear el rectángulo de la meta

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
            running = False

        # Detectar teclas presionadas
        if event.type == pygame.KEYDOWN:  # Evento de tecla presionada
            if event.key == pygame.K_UP:  # Si se presiona la flecha arriba
                player.y -= player_speed  # Mover al jugador hacia arriba
            if event.key == pygame.K_DOWN:
                player.y += player_speed
            if event.key == pygame.K_LEFT:
                player.x -= player_speed
            if event.key == pygame.K_RIGHT:
                player.x += player_speed
            if event.key == pygame.K_SPACE:  # 
                print("Respirando...")  # Simular la acción de respirar

    # Dibujar el fondo y el jugador
    screen.fill(BLUE)  # Rellenar la pantalla con color blanco
    pygame.draw.rect(screen, SKIN_COLOR, player)  # Dibujar el rectángulo del jugador

    # Verificar si el jugador ha llegado a la meta
    if player.colliderect(goal):  # Detectar colisión entre el jugador y la meta
        print("¡Has llegado a la meta! Has ganado el juego.")
        running = False  # Terminar el juego

    # Dibujar la meta
    pygame.draw.rect(screen, (0, 255, 0), goal)  # Dibujar la meta en color verde

    # Actualizar la pantalla
    pygame.display.flip()  # Actualiza el contenido de la ventana

# Salir de pygame
pygame.quit()
sys.exit()