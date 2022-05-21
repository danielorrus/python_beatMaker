import pygame
from pygame import mixer

pygame.init()

#variables para tamaño de la ventana
WIDTH = 1400
HEIGHT = 800

#variables para colores rgb
black = (0,0,0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)

#propiedades ventana
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)

# frames por segundo y temporizador
fps = 60
timer = pygame.time.Clock()
beats = 8 # número inicial de pasos en pantalla?
instruments = 6 # número de instrumentos
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

# funciones
def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 195], 5) # menú izquierdo
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 5]) # menú inferior
    boxes = []
    colors = [gray, white, gray]
    # textos de instrumentos
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30,30)) # dibuja el hi_hat_text en screen
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30,130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30,230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30,330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30,430))
    floor_tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_tom_text, (30,530))
    # pintamos líneas para separar los instrumentos
    for i in range (instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (195, (i * 100) + 100), 3)
    
    # creamos las zonas de cada beat e instrumento
    for i in range(beats):
        for j in range(instruments):
            if clicked[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color,
                [i * ((WIDTH - 200) // beats) + 205, (j * 100) + 5, ((WIDTH - 200) // beats) - 10,
                ((HEIGHT - 200) // instruments) - 10], 0, 3)
            pygame.draw.rect(screen, gold,
                [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black,
                [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                ((HEIGHT - 200) // instruments)], 2, 5)
            boxes.append((rect, (i,j)))
    return boxes

# bucle principal
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid()
    
    # este for controla todos los eventos que se producen durante el juego
    # (ratón, teclado, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # para la ejecución
            run = False
        # si hacemos click en un cuadro de un beat lo activa si no lo estaba
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos): # collidepoint comprueba si las coordenadas del click coinciden con alguna de las cajas
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1 

    # envía todo a la pantalla
    pygame.display.flip()
pygame.quit()