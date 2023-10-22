import pygame

def squelette(): #fonction qui posséde les valeur de arche
    vitesse=5
    pv_max=20
    attaque=7
    defence=5
    return vitesse,pv_max,attaque,defence

def zombie(): #fonction qui posséde les valeur de arche
    vitesse=5
    pv_max=40
    attaque=1
    defence=1
    return vitesse,pv_max,attaque,defence

def Loup(): #fonction qui posséde les valeur de arche
    vitesse=18
    pv_max=30
    attaque=5
    defence=5
    return vitesse,pv_max,attaque,defence

def Slime(): #fonction qui posséde les valeur de arche
    vitesse=5
    pv_max=10
    attaque=5
    defence=5
    return vitesse,pv_max,attaque,defence


def Chevalier(): #fonction qui posséde les valeur de arche
    vitesse=99
    pv_max=30
    attaque=10
    defence=5
    return vitesse,pv_max,attaque,defence


def Dragon(): #fonction qui posséde les valeur de arche
    vitesse=5
    pv_max=25
    attaque=10
    defence=10
    return vitesse,pv_max,attaque,defence


def Phénix(): #fonction qui posséde les valeur de arche
    vitesse=5
    pv_max=80
    attaque=15
    defence=3
    return vitesse,pv_max,attaque,defence




class monstre:
    def __init__(self,id):
        self.id_monstre=id

        if self.id_monstre==5:
            self.nom="squelette" 
            self.vitesse,self.pv_max,self.attaque,self.defence=squelette()
            self.score = 750  # le score du joeur
            self.image_monstre = pygame.image.load('images/squelette.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))

        elif self.id_monstre==6: 
            self.nom="zombie" 
            self.vitesse,self.pv_max,self.attaque,self.defence=zombie()
            self.score = 500  # le score du joeur
            self.image_monstre = pygame.image.load('images/zombie.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))
            

        elif self.id_monstre==7:
            self.nom="Loup" 
            self.vitesse,self.pv_max,self.attaque,self.defence=Loup()
            self.score = 1000  # le score du joeur
            self.image_monstre = pygame.image.load('images/loup.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))

        elif self.id_monstre==8:
            self.nom="Slime" 
            self.vitesse,self.pv_max,self.attaque,self.defence=Slime()
            self.score = 200  # le score du joeur
            self.image_monstre = pygame.image.load('images/slime.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))

        elif self.id_monstre==9: 
            self.nom="Chevalier" 
            self.vitesse,self.pv_max,self.attaque,self.defence=Chevalier()
            self.score = 2000  # le score du joeur
            self.image_monstre = pygame.image.load('images/chevalier_ennemie.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))

        elif self.id_monstre==10:
            self.nom="Dragon"
            self.vitesse,self.pv_max,self.attaque,self.defence=Dragon()
            self.score = 5000  # le score du joeur
            self.image_monstre = pygame.image.load('images/dragon.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))

        elif self.id_monstre==11:
            self.nom="Phénix" 
            self.vitesse,self.pv_max,self.attaque,self.defence=Phénix()
            self.score = 5000  # le score du joeur
            self.image_monstre = pygame.image.load('images/phenix.png')
            self.image_monstre = pygame.transform.scale(self.image_monstre, (25,25))

        self.pv=self.pv_max #pv seront les pv actuelle du perso
        self.case = [0,0,0]   # la position du personnage

