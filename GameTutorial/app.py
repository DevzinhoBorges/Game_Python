import pygame as pg
from player import Player

pg.init() # Inicializa o pygame
screen = pg.display.set_mode([840, 480]) # Cria a tela para exibição do jogo
pg.display.set_caption("Spacedown") # Defini o nome na barra de titulo da pagina

objectGroup = pg.sprite.Group() # Cria um grupo para adição de sprites

player = Player(objectGroup) # Insere o sprite ao grupo

def draw(): # Função para desenhar objetos na tela
  screen.fill((19,173,235)) # Defini a cor de fundo da tela
  objectGroup.draw(screen) # Desenha os sprites na tela

gameloop = True
if __name__ == "__main__":
  while gameloop:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        gameloop = False

    keys = pg.key.get_pressed()

    draw()
    pg.display.update()