import pygame

#création de la classe du projectile
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 15
        self.player = player
        self.image = pygame.image.load('canard.gif')
        self.image = pygame.transform.scale(self.image, (40, 24))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 50
        self.rect.y = player.rect.y + 44
        
    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity
        #vérification d'une collision entre le projectile et un ennemi + infliger des dégats
        for cyclope in self.player.game.check_collision(self, self.player.game.all_cyclopes):
            self.remove()
            cyclope.damage(self.player.attack)
            
        #vérification de la sortie du projectile de l'écran puis suppression
        if self.rect.x > 1080:
            self.remove()           