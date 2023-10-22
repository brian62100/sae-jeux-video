import pygame, math, time
import personnage

class choix_perso: # la class game sert à gére les différent menu du jeu
    def __init__(self):
        self.status = False
        self.nombre_joeur = 1
        self.time = [15]
        self.tour_joeur = 1

    def choix(menu1): # lancement et le programme qui permet de choisir sa class
        J1=personnage.perso()
        J1.id_perso=1
        
        J2=personnage.perso()
        J2.id_perso=2

        J3=personnage.perso()
        J3.id_perso=3

        J4=personnage.perso()
        J4.id_perso=4

        pygame.init()
        screen = pygame.display.set_mode((1500, 800)) #1600, 850
        pygame.display.set_caption("le vide")
        background = pygame.image.load('images/backgroud.jpg').convert()


        #on crée prend et définit l'image du bouton start
        button_joeur = pygame.image.load('images/j1.png')
        button_joeur = pygame.transform.scale(button_joeur, (200,200))
        button_joeur_rect = button_joeur.get_rect()
        button_joeur_rect.x = math.ceil(600)
        button_joeur_rect.y = math.ceil(200)

        button_p1 = pygame.image.load('images/chevalier.png')
        button_p1 = pygame.transform.scale(button_p1, (200,200))
        button_p1_rect = button_p1.get_rect()
        button_p1_rect.x = math.ceil(300)
        button_p1_rect.y = math.ceil(400)

        #on prend les images et on définit l'image pour choisir le nombre de joeur
        button_p2 = pygame.image.load('images/mage.png')
        button_p2 = pygame.transform.scale(button_p2, (200,200))
        button_p2_rect = button_p2.get_rect()
        button_p2_rect.x = math.ceil(500)
        button_p2_rect.y = math.ceil(400)

        button_p3 = pygame.image.load('images/assasin.png')
        button_p3 = pygame.transform.scale(button_p3, (200,200))
        button_p3_rect = button_p3.get_rect()
        button_p3_rect.x = math.ceil(700)
        button_p3_rect.y = math.ceil(400)


        button_p4 = pygame.image.load('images/archer.png')
        button_p4 = pygame.transform.scale(button_p4, (200,200))
        button_p4_rect = button_p4.get_rect()
        button_p4_rect.x = math.ceil(900)
        button_p4_rect.y = math.ceil(400)


        run=False
        run2=False
        run3=False
        run4=False
        if menu1.nombre_joeur>=1:
            run = True # run gére la premier page
        if menu1.nombre_joeur>=2:
            run2 = True # run2 gére la deuxiéme page
        if menu1.nombre_joeur>=3:
            run3 = True # run gére la premier page
        if menu1.nombre_joeur==4:
            run4 = True # run2 gére la deuxiéme page
        time.sleep(0.4)
        while run==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print(event)
                        run = False
                        run2 = False
                        run3 = False
                        run4 = False
                        menu1.status = False

            screen.blit(background,(0,0))
            screen.blit(button_joeur,button_joeur_rect)
            screen.blit(button_p1,button_p1_rect)
            screen.blit(button_p2,button_p2_rect)
            screen.blit(button_p3,button_p3_rect)
            screen.blit(button_p4,button_p4_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_p1_rect.collidepoint(event.pos):
                    J1.choix_de_la_class("guerrier")
                    run = False
                elif button_p2_rect.collidepoint(event.pos):
                    J1.choix_de_la_class("mage")
                    run = False
                elif button_p3_rect.collidepoint(event.pos):
                    J1.choix_de_la_class("voleur")
                    run = False
                elif button_p4_rect.collidepoint(event.pos):
                    J1.choix_de_la_class("archer")
                    run = False

            pygame.display.flip()
        time.sleep(0.4)

        button_joeur = pygame.image.load('images/j2.png')
        while run2==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print(event)
                        run = False
                        run2 = False
                        run3 = False
                        run4 = False
                        menu1.status = False

            screen.blit(background,(0,0))
            screen.blit(button_joeur,button_joeur_rect)
            screen.blit(button_p1,button_p1_rect)
            screen.blit(button_p2,button_p2_rect)
            screen.blit(button_p3,button_p3_rect)
            screen.blit(button_p4,button_p4_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_p1_rect.collidepoint(event.pos):
                    J2.choix_de_la_class("guerrier")
                    run2 = False
                elif button_p2_rect.collidepoint(event.pos):
                    J2.choix_de_la_class("mage")
                    run2 = False
                elif button_p3_rect.collidepoint(event.pos):
                    J2.choix_de_la_class("voleur")
                    run2 = False
                elif button_p4_rect.collidepoint(event.pos):
                    J2.choix_de_la_class("archer")
                    run2 = False

            pygame.display.flip()

        time.sleep(0.4)

        button_joeur = pygame.image.load('images/j3.png')

        while run3==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print(event)
                        run = False
                        run2 = False
                        run3 = False
                        run4 = False
                        menu1.status = False

            screen.blit(background,(0,0))
            screen.blit(button_joeur,button_joeur_rect)
            screen.blit(button_p1,button_p1_rect)
            screen.blit(button_p2,button_p2_rect)
            screen.blit(button_p3,button_p3_rect)
            screen.blit(button_p4,button_p4_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_p1_rect.collidepoint(event.pos):
                    J3.choix_de_la_class("guerrier")
                    run3 = False
                elif button_p2_rect.collidepoint(event.pos):
                    J3.choix_de_la_class("mage")
                    run3 = False
                elif button_p3_rect.collidepoint(event.pos):
                    J3.choix_de_la_class("voleur")
                    run3 = False
                elif button_p4_rect.collidepoint(event.pos):
                    J3.choix_de_la_class("archer")
                    run3 = False

            pygame.display.flip()

        time.sleep(0.4)

        button_joeur = pygame.image.load('images/j4.png')


        while run4==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print(event)
                        run = False
                        run2 = False
                        run3 = False
                        run4 = False
                        menu1.status = False

            screen.blit(background,(0,0))
            screen.blit(button_joeur,button_joeur_rect)
            screen.blit(button_p1,button_p1_rect)
            screen.blit(button_p2,button_p2_rect)
            screen.blit(button_p3,button_p3_rect)
            screen.blit(button_p4,button_p4_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_p1_rect.collidepoint(event.pos):
                    J4.choix_de_la_class("guerrier")
                    run4 = False
                elif button_p2_rect.collidepoint(event.pos):
                    J4.choix_de_la_class("mage")
                    run4 = False
                elif button_p3_rect.collidepoint(event.pos):
                    J4.choix_de_la_class("voleur")
                    run4 = False
                elif button_p4_rect.collidepoint(event.pos):
                    J4.choix_de_la_class("archer")
                    run4 = False

            pygame.display.flip()
        return(J1,J2,J3,J4)