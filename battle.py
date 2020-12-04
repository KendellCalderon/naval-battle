#!/usr/bin/python3
import pygame_textinput
import pygame

textinput = pygame_textinput.TextInput()
pygame.init()
fuente = pygame.font.Font(None,40)
clock = pygame.time.Clock()
size = (1500,700)
win = pygame.display.set_mode(size)

A = [
    [1,0,0,0,2,0,0,0,0,0],
    [1,0,0,0,2,0,0,0,0,0],
    [1,0,0,0,2,0,0,0,0,0],
    [1,0,0,0,2,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

B = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

coordenada = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
}

def refreshBoard(matriz, color, ini_x, ini_y):
    x = ini_x
    y = ini_y
    for row in matriz:
        for cel in row:
            pygame.draw.rect(win,(0, 0, 0), (x, y, 50, 50))
            if cel == 0:
                
                pygame.draw.rect(win, color,(x, y, 50, 50))
                
            else:
                j = str(cel)
                text1 = fuente.render(j,0,(255,0,0))
                win.blit(text1,(x + 20, y + 12))
   
            x = x + 51
        y = y + 51
        x = ini_x
            
    pygame.display.flip()
    
def attack(matriz, x, y):
    coordenadas = getCoordenada(x,y)
    valor = matriz[coordenadas[0]][coordenadas[1]]
    if valor != 0:
        matriz[coordenadas[0]][coordenadas[1]]='A'
    else:
        matriz[coordenadas[0]][coordenadas[1]]='X'    
    refresh()
    
def getCoordenada(x, y):
    x = x.upper()
    return(coordenada[x], y-1)

def refresh():
    refreshBoard(A,(255,0,0),100,100)
    refreshBoard(B,(0,0,255),710,100)

refresh()

while True:
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 300, 50))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:   
            exit()

    textinput.update(events)
    win.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)





