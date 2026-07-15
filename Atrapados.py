from pygame import *

window = display.set_mode((800, 800)) #Cambiar el tamaño de la ventana a 800x800

display.set_caption("Atrapados") #Cambiar el título de la ventana a "Atrapados"

background = transform.scale(image.load('C:/Users/Spark/Desktop/Algorithmics/Python 2/M5/M5L1/Tablero/Fondos/Jardín_simétrico.png'), (800, 800))
#background = transform.scale(image.load('C:/Users/Spark/Desktop/Algorithmics/Python 2/M5/M5L1/Tablero/Fondos/PlantvsZombiesBackground.png'), (800, 800))

#Valores de x1 y y1 para el jugador 1
x1 = 150
y1 = 150

#Valores de x2 y y2 para el jugador 2
x2 = 300
y2 = 300

sprite1 = transform.scale(image.load('C:/Users/Spark/Desktop/Algorithmics/Python 2/M5/M5L1/Tablero/Fondos/zombie1.png'), (100, 100))
sprite2 = transform.scale(image.load('C:/Users/Spark/Desktop/Algorithmics/Python 2/M5/M5L1/Tablero/Fondos/crazydave.png'), (100, 100))
sprite3 = transform.scale(image.load('C:/Users/Spark/Desktop/Algorithmics/Python 2/M5/M5L1/Tablero/Fondos/zombie2.png'), (100, 100))

game = True #Variable para controlar el ciclo del juego
clock = time.Clock() 
FPS = 60 #Cambiar el valor de FPS a 60 para un juego más fluido
speed = 5 #Velocidad de movimiento de los jugadores

while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    window.blit(sprite3, (x3, y3))


    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()  

    if keys[K_LEFT] and x1 > 5: 
        x1 -= speed
    if keys[K_RIGHT] and x1 < 695:  
        x1 += speed
    if keys[K_UP] and y1 > 5:
        y1 -= speed
    if keys[K_DOWN] and y1 < 695:   
        y1 += speed

    if keys[K_a] and x2 > 5: 
        x2 -= speed
    if keys[K_d] and x2 < 695:
        x2 += speed
    if keys[K_w] and y2 > 5:
        y2 -= speed
    if keys[K_s] and y2 < 695:    
        y2 += speed    
    
    display.update()
    clock.tick(FPS)

