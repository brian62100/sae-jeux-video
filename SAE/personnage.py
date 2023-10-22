import object, ennemie
import pygame, random, math

def guerrier(): #fonction qui posséde les valeur de guerrier
    vitesse=5
    pv_max=100
    reg_pv=5
    attaque=10
    defence=15
    equipement_type=1 # 1=guerrier, 2=voleur, 3=mage, 4=archer
    image='images/chevalier.png'
    return vitesse,pv_max,reg_pv,attaque,defence,equipement_type,image

def mage(): #fonction qui posséde les valeur de mage
    vitesse=10
    pv_max=30
    reg_pv=10
    attaque=20
    defence=5
    equipement_type=3 # 1=guerrier, 2=voleur, 3=mage, 4=archer
    image='images/mage.png'
    return vitesse,pv_max,reg_pv,attaque,defence,equipement_type,image

def voleur(): #fonction qui posséde les valeur de voleur
    vitesse=12
    pv_max=30
    reg_pv=5
    attaque=30
    defence=0
    equipement_type=2 # 1=guerrier, 2=voleur, 3=mage, 4=archer
    image='images/assasin.png'
    return vitesse,pv_max,reg_pv,attaque,defence,equipement_type,image

def archer(): #fonction qui posséde les valeur de arche
    vitesse=20
    pv_max=50
    reg_pv=5
    attaque=15
    defence=5
    equipement_type=4 # 1=guerrier, 2=voleur, 3=mage, 4=archer
    image='images/archer.png'
    return vitesse,pv_max,reg_pv,attaque,defence,equipement_type,image

class perso:    # la class perso est utilisé pour les stats des joeurs
        def __init__(self):
            self.nom="test"    #input("choisir le nom du joeur 1 : ")
            self.classe="guerrier"     #input("choisir la class entre 'guerrier', 'voleur', 'mage', 'arché' : ")

            if self.classe=="guerrier": #si le joeur choisit la class guerrier alors on appele la fonction guerrier qui prend les valeur par défaut de la class
                self.vitesse,self.pv_max,self.reg_pv,self.attaque,self.defence,self.equipement_type,self.image1=guerrier()

            elif self.classe=="mage": # on refarde si c'est un mage si ou on fait comme en haut
                self.vitesse,self.pv_max,self.reg_pv,self.attaque,self.defence,self.equipement_type,self.image1=mage()

            elif self.classe=="voleur":
                self.vitesse,self.pv_max,self.reg_pv,self.attaque,self.defence,self.equipement_type,self.image1=voleur()

            elif self.classe=="archer":
                self.vitesse,self.pv_max,self.reg_pv,self.attaque,self.defence,self.equipement_type,self.image1=archer()

            self.pv=self.pv_max #pv seront les pv actuelle du perso
            self.score = 0  # le score du joeur
            self.arme = False   #si il posséde une arme ou non
            self.main_secondaire = False    # si il posséde un object dans sa main secondaire
            self.chapeau = False    # si il posséde un chapeau
            self.plastron = False   #si il posséde un plastron
            self.chaussures = False #si il posséde des chaussures
            self.id_perso = 0 # id du personnage
            self.case = [0,0,0]   # la position du personnage
            self.equipement = object.liste_object(5)

        def choix_de_la_class(self,choix):
            self.classe=choix     #input("choisir la class entre 'guerrier', 'voleur', 'mage', 'archer' : ")

            if self.classe=="guerrier": #si le joeur choisit la class guerrier alors on appele la fonction guerrier qui prend les valeur par défaut de la class
                self.vitesse, self.pv_max, self.reg_pv, self.attaque, self.defence, self.equipement_type, self.image1 = guerrier()

            elif self.classe=="mage": # on refarde si c'est un mage si ou on fait comme en haut
                self.vitesse, self.pv_max, self.reg_pv, self.attaque, self.defence, self.equipement_type, self.image1 = mage()

            elif self.classe=="voleur":
                self.vitesse, self.pv_max, self.reg_pv, self.attaque, self.defence, self.equipement_type, self.image1 = voleur()

            elif self.classe=="archer":
                self.vitesse, self.pv_max, self.reg_pv, self.attaque, self.defence, self.equipement_type, self.image1 = archer()

            self.Image2 = pygame.image.load(self.image1)
            self.Image2 = pygame.transform.scale(self.Image2, (25,25))
            self.Image_rect = self.Image2.get_rect()
            self.Image_rect.x = math.ceil(0)
            self.Image_rect.y = math.ceil(0)
            self.Image_p1 = pygame.image.load(self.image1)
            self.Image_p1 = pygame.transform.scale(self.Image_p1, (100, 100))
            self.pv=self.pv_max #pv seront les pv actuelle du perso


            self.equipement=object.liste_object(self.equipement_type)

        def updates(self):
            if self.equipement_type==1:
                if self.equipement.casque_equipe == True and self.equipement.casque_stats == False:
                    self.defence += 5
                    self.equipement.casque_stats = True
                    
                if self.equipement.pastron_equipe == True and self.equipement.pastron_stats == False:
                    self.pv_max += 20
                    self.equipement.pastron_stats = True

                if self.equipement.botte_equipe == True and self.equipement.botte_stats == False:
                    self.vitesse += 5
                    self.equipement.botte_stats = True

                if self.equipement.main1_equipe == True and self.equipement.main1_stats == False:
                    self.attaque += 5
                    self.equipement.main1_stats = True

                if self.equipement.main2_equipe == True and self.equipement.main2_stats == False:
                    self.defence += 5
                    self.equipement.main2_stats = True

            elif self.equipement_type>1:
                if self.equipement.casque_equipe == True and self.equipement.casque_stats == False:
                    self.defence += 5
                    self.equipement.casque_stats = True

                if self.equipement.pastron_equipe == True and self.equipement.pastron_stats == False:
                    self.pv_max += 20
                    self.equipement.pastron_stats = True

                if self.equipement.botte_equipe == True and self.equipement.botte_stats == False:
                    self.vitesse += 5
                    self.equipement.botte_stats = True

                if self.equipement.main1_equipe == True and self.equipement.main1_stats == False:
                    self.attaque += 5
                    self.equipement.main1_stats = True

                if self.equipement.main2_equipe == True and self.equipement.main2_stats == False:
                    self.attaque += 5
                    self.equipement.main2_stats = True
        
        def combat_joeur(self, J2):
            fin = False
            if self.vitesse < J2.vitesse:
                while not fin==True:
                    self.pv=attaque(J2.attaque, self.pv ,self.defence)
                    J2.pv=attaque(self.attaque, J2.pv ,J2.defence)
                    fin=fin_combat_joeur(self, J2, fin)

            elif self.vitesse==J2.vitesse:
                pile_face = random.randint(1,2)

                if pile_face == 1:
                    while not fin==True:
                        self.pv=attaque(J2.attaque, self.pv, self.defence)
                        J2.pv=attaque(self.attaque, J2.pv, J2.defence)
                        fin=fin_combat_joeur(self, J2, fin)

                elif pile_face == 2:
                    while not fin==True:
                        J2.pv=attaque(self.attaque, J2.pv, J2.defence)
                        self.pv=attaque(J2.attaque, self.pv, self.defence)
                        fin=fin_combat_joeur(self, J2, fin)

            else :
                while not fin==True:
                    J2.pv=attaque(self.attaque, J2.pv, J2.defence)
                    self.pv=attaque(J2.attaque, self.pv, self.defence)
                    fin=fin_combat_joeur(self, J2, fin)
            


        def combat_monstre (self, J2 : ennemie.monstre):
            fin = False
            print("test")
            if self.vitesse < J2.vitesse:
                while not fin==True:
                    self.pv=attaque(J2.attaque, self.pv ,self.defence)
                    J2.pv=attaque(self.attaque, J2.pv ,J2.defence)
                    fin=fin_combat_monstre(self, J2, fin)
                return self

            elif self.vitesse==J2.vitesse:
                pile_face = random.randint(1,2)

                if pile_face == 1:
                    while not fin==True:
                        self.pv=attaque(J2.attaque, self.pv, self.defence)
                        J2.pv=attaque(self.attaque, J2.pv, J2.defence)
                        fin=fin_combat_monstre(self, J2, fin)
                    return self

                elif pile_face == 2:
                    while not fin==True:
                        J2.pv=attaque(self.attaque, J2.pv, J2.defence)
                        self.pv=attaque(J2.attaque, self.pv, self.defence)
                        fin=fin_combat_monstre(self, J2, fin)
                    return self

            else :
                while not fin==True:
                    J2.pv=attaque(self.attaque, J2.pv, J2.defence)
                    self.pv=attaque(J2.attaque, self.pv, self.defence)
                    fin=fin_combat_monstre(self, J2, fin)
                return self




def attaque(attaquant_attaque, defenceseur_pv,defenceseur_defense):
    dommage_subi= attaquant_attaque - defenceseur_defense
    if dommage_subi<=0:
        dommage_subi=1
    defenceseur_pv=defenceseur_pv-dommage_subi
    return defenceseur_pv


def fin_combat_joeur (J1 : perso, J2 : perso, fin):
    if J1.pv<=0:
        J2.score = J2.score + (J1.score/2) 
        J1.score = J1.score / 2
        J1.pv = J1.pv_max
        J1.case = [25,25,0]
        fin=True
        return fin
    elif J2.pv<=0:
        J1.score = J1.score + (J2.score/2) 
        J2.score = J2.score / 2
        J2.pv = J2.pv_max
        J2.case = [25,25,0]
        fin=True
        return fin
    else:
        fin=False
        return fin
    
def fin_combat_monstre (J1 : perso, J2 : ennemie.monstre, fin):
    if J1.pv<=0:
        J1.score = J1.score / 2
        J1.pv = J1.pv_max
        J1.case = [25,25,0]
        fin=True
        return fin
    elif J2.pv<=0:
        J1.score = J1.score + (J2.score/2) 
        J1.pv = J1.pv_max
        fin=True
        return fin
    else:
        fin=False
        return fin