import pygame, math

class game: # la class game sert à gére les différent menu du jeu
    def __init__(self):
        self.status = False
        self.nombre_joeur = 1
        self.time = [15]
        self.tour_joeur = 1

    def lancement(): # lancement et le programme qui cert à lancer le jeu
        menu1=game()
        pygame.init()
        screen = pygame.display.set_mode((1500, 800)) #1600, 850
        pygame.display.set_caption("le vide")
        background = pygame.image.load('images/backgroud.jpg').convert()


        #on crée prend et définit l'image du bouton start
        button_start = pygame.image.load('images/start.png')
        button_start = pygame.transform.scale(button_start, (200,200))
        button_start_rect = button_start.get_rect()
        button_start_rect.x = math.ceil(screen.get_width() / 2.5)
        button_start_rect.y = math.ceil(screen.get_height() / 4)

        #on prend les images et on définit l'image pour choisir le nombre de joeur
        button_p1 = pygame.image.load('images/p1.png')
        button_p1 = pygame.transform.scale(button_p1, (350,200))
        button_p1_rect = button_p1.get_rect()
        button_p1_rect.x = math.ceil(300)
        button_p1_rect.y = math.ceil(400)

        button_p2 = pygame.image.load('images/p2.png')
        button_p2 = pygame.transform.scale(button_p2, (375,200))
        button_p2_rect = button_p2.get_rect()
        button_p2_rect.x = math.ceil(500)
        button_p2_rect.y = math.ceil(400)


        button_p3 = pygame.image.load('images/p3.png')
        button_p3 = pygame.transform.scale(button_p3, (350,200))
        button_p3_rect = button_p3.get_rect()
        button_p3_rect.x = math.ceil(700)
        button_p3_rect.y = math.ceil(400)

        button_p4 = pygame.image.load('images/p4.png')
        button_p4 = pygame.transform.scale(button_p4, (350,200))
        button_p4_rect = button_p4.get_rect()
        button_p4_rect.x = math.ceil(900)
        button_p4_rect.y = math.ceil(400)


        run = True # run gére la premier page
        run2 = True # run2 gére la deuxiéme page
        run3 = False
        while run==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print(event)
                        run = False
                        run2 = False
                        menu1.status = False

            screen.blit(background,(0,0))
            screen.blit(button_start,button_start_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start_rect.collidepoint(event.pos):
                    run = False

            pygame.display.flip()

        while run2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(event)
                    run2 = False
                    menu1.status = False
            if menu1.status ==False:
                screen.blit(background,(0,0))        
                screen.blit(button_p1,button_p1_rect)
                screen.blit(button_p2,button_p2_rect)
                screen.blit(button_p3,button_p3_rect)
                screen.blit(button_p4,button_p4_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_p1_rect.collidepoint(event.pos):
                        menu1.nombre_joeur = 1
                        menu1.status = True
                        run2 = False
                        run3 = True

                    if button_p2_rect.collidepoint(event.pos):
                        menu1.nombre_joeur = 2
                        menu1.status = True
                        run2 = False
                        run3 = True

                    if button_p3_rect.collidepoint(event.pos):
                        menu1.nombre_joeur = 3
                        menu1.status = True
                        run2 = False
                        run3 = True

                    if button_p4_rect.collidepoint(event.pos):
                        menu1.nombre_joeur = 4
                        menu1.status = True
                        run2 = False
                        run3 = True
                        
            pygame.display.flip()
        return menu1, run3