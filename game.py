import pygame
from player import Player
from cyclope import Cyclope
from neo import Neo

#création de la classe du jeu
class Game:
    def __init__(self):
        #chargement du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de cyclopes
        self.all_cyclopes = pygame.sprite.Group()
        self.all_neo = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_cyclope()
        self.spawn_cyclope()
        self.spawn_neo()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_cyclope(self):
        cyclope = Cyclope(self)
        self.all_cyclopes.add(cyclope)
        
    def spawn_neo(self):
        neo = Neo(self)
        self.all_neo.add(neo)