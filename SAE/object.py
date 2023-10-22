import pygame, math

class liste_object:
    def __init__(self,id: int):
        self.casque_equipe  = False
        self.pastron_equipe = False
        self.botte_equipe   = False
        self.main1_equipe   = False
        self.main2_equipe   = False

        self.casque_stats  = False
        self.pastron_stats = False
        self.botte_stats   = False
        self.main1_stats   = False
        self.main2_stats   = False

        self.casque  = pygame.image.load('images/backgroud.jpg')
        self.pastron = pygame.image.load('images/backgroud.jpg')
        self.botte   = pygame.image.load('images/backgroud.jpg')
        self.main1   = pygame.image.load('images/backgroud.jpg')
        self.main2   = pygame.image.load('images/backgroud.jpg')



        if id==1:
            self.casque = pygame.image.load('images/casque_en_fer.png')
            self.casque = pygame.transform.scale(self.casque, (50,50))
            self.Image_casque_rect = self.casque.get_rect()
            self.Image_casque_rect.x = math.ceil(150)
            self.Image_casque_rect.y = math.ceil(150)

            self.pastron = pygame.image.load('images/plastron_en_fer.png')
            self.pastron = pygame.transform.scale(self.pastron, (50,50))
            self.Image_pastron_rect = self.pastron.get_rect()
            self.Image_pastron_rect.x = math.ceil(250)
            self.Image_pastron_rect.y = math.ceil(150)

            self.botte = pygame.image.load('images/botte_en_fer.png')
            self.botte = pygame.transform.scale(self.botte, (50,50))
            self.Image_botte_rect = self.botte.get_rect()
            self.Image_botte_rect.x = math.ceil(350)
            self.Image_botte_rect.y = math.ceil(150)

            self.main1 = pygame.image.load('images/Epee.png')
            self.main1 = pygame.transform.scale(self.main1, (50,50))
            self.Image_main1_rect = self.main1.get_rect()
            self.Image_main1_rect.x = math.ceil(450)
            self.Image_main1_rect.y = math.ceil(150)

            self.main2 = pygame.image.load('images/Bouclier.png')
            self.main2 = pygame.transform.scale(self.main2, (50,50))
            self.Image_main2_rect = self.main2.get_rect()
            self.Image_main2_rect.x = math.ceil(550)
            self.Image_main2_rect.y = math.ceil(150)



        elif id==2:
            self.casque = pygame.image.load('images/casque_en_cuir.png')
            self.casque = pygame.transform.scale(self.casque, (50,50))
            self.Image_casque_rect = self.casque.get_rect()
            self.Image_casque_rect.x = math.ceil(150)
            self.Image_casque_rect.y = math.ceil(150)

            self.pastron = pygame.image.load('images/armure_en_cuir.png')
            self.pastron = pygame.transform.scale(self.pastron, (50,50))
            self.Image_pastron_rect = self.pastron.get_rect()
            self.Image_pastron_rect.x = math.ceil(250)
            self.Image_pastron_rect.y = math.ceil(150)

            self.botte = pygame.image.load('images/botte_de_voleur.png')
            self.botte = pygame.transform.scale(self.botte, (50,50))
            self.Image_botte_rect = self.botte.get_rect()
            self.Image_botte_rect.x = math.ceil(350)
            self.Image_botte_rect.y = math.ceil(150)

            self.main1 = pygame.image.load('images/dague1.png')
            self.main1 = pygame.transform.scale(self.main1, (50,50))
            self.Image_main1_rect = self.main1.get_rect()
            self.Image_main1_rect.x = math.ceil(450)
            self.Image_main1_rect.y = math.ceil(150)

            self.main2 = pygame.image.load('images/dague2.png')
            self.main2 = pygame.transform.scale(self.main2, (50,50))
            self.Image_main2_rect = self.main2.get_rect()
            self.Image_main2_rect.x = math.ceil(550)
            self.Image_main2_rect.y = math.ceil(150)


        elif id==3:
            self.casque = pygame.image.load('images/casque_de_mage.png') # Défense supplémentaire
            self.casque = pygame.transform.scale(self.casque, (50,50))
            self.Image_casque_rect = self.casque.get_rect()
            self.Image_casque_rect.x = math.ceil(150)
            self.Image_casque_rect.y = math.ceil(150)

            self.pastron = pygame.image.load('images/tenue_de_mage.png') # Point de vie max supplémentaire
            self.pastron = pygame.transform.scale(self.pastron, (50,50))
            self.Image_pastron_rect = self.pastron.get_rect()
            self.Image_pastron_rect.x = math.ceil(250)
            self.Image_pastron_rect.y = math.ceil(150)

            self.botte = pygame.image.load('images/botte_de_mage.png') # Point de vitesse supplémentaire
            self.botte = pygame.transform.scale(self.botte, (50,50))
            self.Image_botte_rect = self.botte.get_rect()
            self.Image_botte_rect.x = math.ceil(350)
            self.Image_botte_rect.y = math.ceil(150)

            self.main1 = pygame.image.load('images/bagette_magique.png')  # Attaque supplémentaire
            self.main1 = pygame.transform.scale(self.main1, (50,50))
            self.Image_main1_rect = self.main1.get_rect()
            self.Image_main1_rect.x = math.ceil(450)
            self.Image_main1_rect.y = math.ceil(150)

            self.main2 = pygame.image.load('images/Livre.png') # Attaque supplémentaire
            self.main2 = pygame.transform.scale(self.main2, (50,50))
            self.Image_main2_rect = self.main2.get_rect()
            self.Image_main2_rect.x = math.ceil(550)
            self.Image_main2_rect.y = math.ceil(150)


        elif id==4:
            self.casque = pygame.image.load('images/gagoule_en_cuir.png') # Défense supplémentaire
            self.casque = pygame.transform.scale(self.casque, (50,50))
            self.Image_casque_rect = self.casque.get_rect()
            self.Image_casque_rect.x = math.ceil(150)
            self.Image_casque_rect.y = math.ceil(150)

            self.pastron = pygame.image.load('images/tenue_en_cuir.png') # Point de vie max supplémentaire
            self.pastron = pygame.transform.scale(self.pastron, (50,50))
            self.Image_pastron_rect = self.pastron.get_rect()
            self.Image_pastron_rect.x = math.ceil(250)
            self.Image_pastron_rect.y = math.ceil(150)

            self.botte = pygame.image.load('images/botte_en_cuir.png') # Point de vitesse supplémentaire
            self.botte = pygame.transform.scale(self.botte, (50,50))
            self.Image_botte_rect = self.botte.get_rect()
            self.Image_botte_rect.x = math.ceil(350)
            self.Image_botte_rect.y = math.ceil(150)

            self.main1 = pygame.image.load('images/Arc.png') # Attaque supplémentaire
            self.main1 = pygame.transform.scale(self.main1, (50,50))
            self.Image_main1_rect = self.main1.get_rect()
            self.Image_main1_rect.x = math.ceil(450)
            self.Image_main1_rect.y = math.ceil(150)

            self.main2 = pygame.image.load('images/fleche.png') # Attaque supplémentaire
            self.main2 = pygame.transform.scale(self.main2, (50,50))
            self.Image_main2_rect = self.main2.get_rect()
            self.Image_main2_rect.x = math.ceil(550)
            self.Image_main2_rect.y = math.ceil(150)