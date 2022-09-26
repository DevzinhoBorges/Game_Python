import pygame as pg

pg.init() # Inicializa o pygame
screen = pg.display.set_mode([840, 480]) # Cria a tela para exibição do jogo
pg.display.set_caption("Spacedown") # Defini o nome na barra de titulo da pagina

drawGroup = pg.sprite.Group() # Cria um grupo para adição de sprites

player = pg.sprite.Sprite(drawGroup) # Insere o sprite ao grupo
player.image = pg.image.load("GameTutorial/img/nave.png") # Adiciona a imagem do sprite
player.image = pg.transform.scale(player.image, [100, 100]) # Modifica o tamanho da imagem
player.rect = pg.Rect(50, 50, 100, 100) # Defini o tamanho e a posição da imagem

def draw(): # Função para desenhar objetos na tela
  screen.fill((19,173,235)) # Defini a cor de fundo da tela
  drawGroup.draw(screen) # Desenha os sprites na tela

gameloop = True
if __name__ == "__main__":
  while gameloop:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        gameloop = False

    draw()
    pg.display.update()