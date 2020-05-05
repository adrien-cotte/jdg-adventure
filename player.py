import pygame
from projectile import Projectile

#création de la classe joueur
class Player(pygame.sprite.Sprite):   
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image_immobileD = pygame.image.load('jdg_immobileD.gif')
        self.image_immobileG = pygame.image.load('jdg_immobileG.gif')
        self.image_D = pygame.image.load('jdgD.gif')
        self.image_G = pygame.image.load('jdgG.gif')
        self.image_S = pygame.image.load('jdgD_saut.gif')
        self.image = self.image_immobileD
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 425
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            print("game over")
        if self.health <= 50:
            self.remove()
            
    def health_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [15, 15, 104, 19])
        pygame.draw.rect(surface, (50, 50, 50), [17, 17, self.max_health, 15])
        pygame.draw.rect(surface, (50, 230, 30), [17, 17, self.health, 15])
        
    def launch_projectile(self):
        #création d'une instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        
    def move_right(self):
        #vérification d'une éventuelle collision
        if not self.game.check_collision(self, self.game.all_cyclopes):
            self.rect.x += self.velocity
            self.image = self.image_D

    def move_left(self):
        self.rect.x -= self.velocity
        self.image = self.image_G