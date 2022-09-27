import pygame as pg
from player import Player

pg.init() # Inicializa o pygame
screen = pg.display.set_mode([840, 480]) # Cria a tela para exibição do jogo
pg.display.set_caption("Spacedown") # Defini o nome na barra de titulo da pagina

objectGroup = pg.sprite.Group() # Cria um grupo para adição de sprites

player = Player(objectGroup) # Insere o sprite ao grupo

pg.mixer.music.load("GameTutorial/sounds/space.wav")
pg.mixer.music.play(-1)

shoot = pg.mixer.Sound("GameTutorial/sounds/shoot1.mp3")

def draw(): # Função para desenhar objetos na tela
  screen.fill((19,173,235)) # Defini a cor de fundo da tela
  objectGroup.draw(screen) # Desenha os sprites na tela
  objectGroup.update()

gameloop = True
if __name__ == "__main__":
  while gameloop:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        gameloop = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
          shoot.play()

    draw()
    pg.display.update()