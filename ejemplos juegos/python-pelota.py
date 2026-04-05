import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pelota Rebotando")

# Colores (R, G, B)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de la pelota
pelota_radio = 20
pelota_x = ANCHO // 2
pelota_y = ALTO // 2
vel_x = 4
vel_y = 4

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover la pelota
    pelota_x += vel_x
    pelota_y += vel_y

    # Rebotar en los bordes
    if pelota_x - pelota_radio <= 0 or pelota_x + pelota_radio >= ANCHO:
        vel_x *= -1
    if pelota_y - pelota_radio <= 0 or pelota_y + pelota_radio >= ALTO:
        vel_y *= -1

    # Dibujar en pantalla
    VENTANA.fill(NEGRO)
    pygame.draw.circle(VENTANA, BLANCO, (pelota_x, pelota_y), pelota_radio)
    pygame.display.flip()

    # Controlar FPS
    clock.tick(60)