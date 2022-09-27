import pygame as pg

class Player(pg.sprite.Sprite):
  def __init__(self, *groups):
    super().__init__(*groups)

    self.image = pg.image.load("GameTutorial/img/nave.png") # Adiciona a imagem do sprite
    self.image = pg.transform.scale(self.image, [100, 100]) # Modifica o tamanho da imagem
    self.rect = pg.Rect(50, 50, 100, 100) # Defini o tamanho e a posição da imagem