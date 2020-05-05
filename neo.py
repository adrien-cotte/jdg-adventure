import pygame
import random

#création de la classe de l'ennemi
class Neo(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 0.1
        self.image = pygame.image.load('neo_flying.gif')
        self.rect = self.image.get_rect()
        self.rect.x = 1020 + random.randint(20,320)
        self.rect.y = 300 + random.randint(0,40)
        self.velocity = random.randint(8,15)
        
    def damage(self, amount):
        #Infliger les dégats
        self.health -= amount
        if self.health <=0:
            #réaparition comme un nouveau ennemi
            self.rect.x = 1020 + random.randint(20,320)
            self.health = self.max_health
            self.velocity = random.randint(6,14)
        
    #def update_health_bar(self):
    
    def forward(self):   
        #vérification d'une éventuelle collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            #infliger les dégats au joueur
            self.game.player.damage(self.attack)
        if self.rect.x < -50:
            self.rect.x = 1020 + random.randint(20,650)
            self.health = self.max_health
            self.velocity = random.randint(6,14)