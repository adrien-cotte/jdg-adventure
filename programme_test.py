import pygame #Importation des bibliothèques nécessaires
from game import Game
from pygame.locals import *
pygame.init() #méthode init -> Initialisation de la bibliothèque Pygame

#générer la fenêtre du jeu
pygame.display.set_caption("jdg's adventure") #permet de nommer notre surface d'affichage
resolution = (1080,720)
window = pygame.display.set_mode((resolution), pygame.RESIZABLE) #Création de la fenêtre
background = pygame.image.load('image_1').convert()

#chargement du jeu
game = Game()

#définition de l'état de saut
isJump = False
jumpCount = 10

continuer = True
while continuer:
    pygame.time.delay(22)
    
    #appliquer l'arrière-plan
    window.blit(background,(0,0))
    
    #appliquer l'image du joueur
    window.blit(game.player.image, game.player.rect)
    
    #récuperation des projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    #récupération des cyclopes
    for cyclope in game.all_cyclopes:
        cyclope.forward()
    
    #appliquer l'image des projectiles
    game.player.all_projectiles.draw(window)
    
    #appliquer l'image des cyclope
    game.all_cyclopes.draw(window)
    
    #verifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < window.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
     
    if not (isJump):   
        if game.pressed.get(pygame.K_SPACE):
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            game.player.rect.y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
            #game.player.rect.y += 1 *0.3
        else:
            isJump = False
            jumpCount = 10
            game.player.rect.y += 5
    
    pygame.display.flip() #rafraichit les nouvelles options d'affichage
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
            print ("fermeture du jeu")
            
        #détection des touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            game.player.launch_projectile()