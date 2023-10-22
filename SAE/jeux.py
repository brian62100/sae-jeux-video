##################################################################################################
# crée par dupuis brian
# se programme sert à la création d'un jeux video
# v2.1
##################################################################################################
# à amélioré :  
#               demande de combat
#               implamenté le combat,
#               gére le score
#               fin du jeu
################################################################################################


#importation des bibliotéque
import pygame, random, math, time

#importation des autres fichier necessaire
import menu, personnage, ennemie

# on crée une class partie contenant la totalité du code pour le jeu
class partie():
        # on crée la fonction lancement_jeux qui permetra de lancer le jeux
        def lancement_jeux(menu1: menu.game, J1: personnage.perso, J2: personnage.perso, J3: personnage.perso, J4: personnage.perso):
                pygame.init()                                   # on initalise  pygame
                screen = pygame.display.set_mode((1500, 800))   # on donne la taille de la fenetre
                pygame.display.set_caption("le vide")           #on lui donne un nom
                background = pygame.image.load('images/backgroud.jpg').convert()        # on donne un backgroud a la fenetre

                ############################################ création des fonction #############################################

                def forge(joeur: personnage.perso):     # la fonction forge permet d'afficher le menu de la forge
                        # on verifie que le jouer n'a pas déjà les 5 équipement 
                        if not joeur.equipement.casque_equipe  == True and joeur.equipement.pastron_equipe == True and joeur.equipement.botte_equipe   == True and joeur.equipement.main1_equipe   == True and joeur.equipement.main2_equipe   == True:
                                pygame.draw.rect(screen, (255,255,255), pygame.Rect(100, 100, 600, 200))

                                screen.blit(J1.equipement.main1,joeur.equipement.Image_main1_rect) 
                                screen.blit(J1.equipement.main2,joeur.equipement.Image_main2_rect) 
                                screen.blit(J1.equipement.casque,joeur.equipement.Image_casque_rect) 
                                screen.blit(J1.equipement.pastron,joeur.equipement.Image_pastron_rect)
                                screen.blit(J1.equipement.botte,joeur.equipement.Image_botte_rect)

                def forge_valide(valide_forge):         # forge valide permet d'enlever le menu forge mais aussi d'empecher de le réactiver
                        pygame.draw.rect(screen, (255,255,255), pygame.Rect(8000, 8000, 1, 1))

                        screen.blit(J1.equipement.main1,(8000,8000,50,50)) 
                        screen.blit(J1.equipement.main2,(8000,8000,50,50)) 
                        screen.blit(J1.equipement.casque,(8000,8000,50,50)) 
                        screen.blit(J1.equipement.pastron,(8000,8000,50,50))
                        screen.blit(J1.equipement.botte,(8000,8000,50,50))
                        valide_forge=False
                        return valide_forge

                def image_equipement(joeur : personnage.perso): # image equipement permet de m'afficher les images de l'equipement dans l'inventaire
                         # si il posséde équipement main1 alors on affichier l'image sinon on afficher le fond d'écran de la page et on fait sa pour les 5 piece d'équipement
                        if joeur.equipement.main1_equipe == True:      
                                Image_main1 = joeur.equipement.main1
                                Image_main1 = pygame.transform.scale(Image_main1, (50,50))
                        elif joeur.equipement.main1_equipe == False:
                                Image_main1 = pygame.image.load('images/backgroud.jpg')
                                Image_main1 = pygame.transform.scale(Image_main1, (50,50))


                        if joeur.equipement.main2_equipe == True:
                                Image_main2 = joeur.equipement.main2
                                Image_main2 = pygame.transform.scale(Image_main2, (50,50))
                        elif joeur.equipement.main2_equipe == False:
                                Image_main2 = pygame.image.load('images/backgroud.jpg')
                                Image_main2 = pygame.transform.scale(Image_main2, (50,50))


                        if joeur.equipement.casque_equipe == True:
                                Image_casque = joeur.equipement.casque
                                Image_casque = pygame.transform.scale(Image_casque, (50,50))
                        elif joeur.equipement.casque_equipe == False:
                                Image_casque = pygame.image.load('images/backgroud.jpg')
                                Image_casque = pygame.transform.scale(Image_casque, (50,50))


                        if joeur.equipement.pastron_equipe == True:
                                Image_pastron = joeur.equipement.pastron
                                Image_pastron = pygame.transform.scale(Image_pastron, (50,50))
                        elif joeur.equipement.pastron_equipe == False:
                                Image_pastron = pygame.image.load('images/backgroud.jpg')
                                Image_pastron = pygame.transform.scale(Image_pastron, (50,50))


                        if joeur.equipement.botte_equipe == True:
                                Image_botte = joeur.equipement.botte
                                Image_botte = pygame.transform.scale(Image_botte, (50,50))
                        elif joeur.equipement.botte_equipe == False:
                                Image_botte = pygame.image.load('images/backgroud.jpg')
                                Image_botte = pygame.transform.scale(Image_botte, (50,50))
                        
                        return  Image_main1, Image_main2, Image_casque, Image_pastron, Image_botte

                def change_information(tour: int): # change_information permet de donnée les information du jouer qui permetront d'afficher ces stats
                        if tour==1:
                                texte_attaque = J1.attaque
                                texte_defence = J1.defence
                                texte_pv = J1.pv
                                texte_pv_max = J1.pv_max
                                texte_regen = J1.reg_pv
                                texte_vitesse = J1.vitesse
                        elif tour==2:
                                texte_attaque = J2.attaque
                                texte_defence = J2.defence
                                texte_pv = J2.pv
                                texte_pv_max = J2.pv_max
                                texte_regen = J2.reg_pv
                                texte_vitesse = J2.vitesse
                        elif tour==3:
                                texte_attaque = J3.attaque
                                texte_defence = J3.defence
                                texte_pv = J3.pv
                                texte_pv_max = J3.pv_max
                                texte_regen = J3.reg_pv
                                texte_vitesse = J3.vitesse
                        elif tour==4:
                                texte_attaque = J4.attaque
                                texte_defence = J4.defence
                                texte_pv = J4.pv
                                texte_pv_max = J4.pv_max
                                texte_regen = J4.reg_pv
                                texte_vitesse = J4.vitesse
                        return texte_pv_max, texte_pv, texte_regen, texte_attaque, texte_defence, texte_vitesse
                
                def random_liste_case(): # random_liste_case permet de choisir des cases parmit les cases vierges pour les transformer en cases spéciale 
                        liste_choix=[(1),(2),(5),(5),(6),(6),(7),(7),(8),(8),(9),(9),(10),(11)]
                        liste_case_random=[]
                        #1 Fontaine = 1
                        #1 Armurerie = 2
                        #2 Cimentier = 5
                        #2 Champ de cadavre = 6
                        #2 Foret = 7
                        #2 Pleine = 8
                        #2 Ville = 9
                        #1 Châteaux = 10
                        #1 Champ de cendre = 11
                        fini=False
                        while fini==False:
                                valide=True
                                case=random.randint(1,37) #on chosit une case viege aléatoire sauf la case de départ
                                if not len(liste_case_random)==0: #on verifie qu'il reste des cases spéciale qui sont pas attribué
                                        for y in range (len(liste_case_random)): # on verifie pour tout les elements de liste_case_random si la case vierge à déjà était attribué
                                                if liste_case_random[y][0]==case:
                                                        valide=False
                                if valide==True: #si la case vierge n'est pas attribué alors on l'attribue
                                        liste_case_random.append((case,liste_choix[0]))
                                        liste_choix.pop(0)        
                                if len(liste_choix)==0: # si il reste plus de case spéciale à attribué alors on met fin au while
                                        fini=True
                        return liste_case_random

                def spawn_monstre(case_random,liste_case):      # spawn_monstre permet de faire apparaitre les monstres sur leurs cases
                        for i in range(len(case_random)):
                                for y in range(len(liste_case)):
                                        if case_random[i][0]==liste_case[y][2]:
                                                x_monstre = (liste_case[y][0])+12.5
                                                y_monstre = (liste_case[y][1])+12.5
                                                if case_random[i][1]==5:
                                                        screen.blit(squelette_1.image_monstre, (x_monstre, y_monstre)) 
                                                if case_random[i][1]==6:
                                                        screen.blit(zombie_1.image_monstre, (x_monstre, y_monstre)) 
                                                if case_random[i][1]==7:
                                                        screen.blit(loup1.image_monstre, (x_monstre, y_monstre)) 
                                                if case_random[i][1]==8:
                                                        screen.blit(Slime1.image_monstre, (x_monstre, y_monstre)) 
                                                if case_random[i][1]==9:
                                                        screen.blit(Chevalier1.image_monstre, (x_monstre, y_monstre))
                                                if case_random[i][1]==10:
                                                        screen.blit(Dragon.image_monstre, (x_monstre, y_monstre)) 
                                                if case_random[i][1]==11:
                                                        screen.blit(Phénix.image_monstre, (x_monstre, y_monstre))

                def verification_joeur(liste_case,case_random, joeur1 : personnage.perso, Joeur2 : personnage.perso, Joeur3 : personnage.perso, Joeur4 : personnage.perso,case_joeur):
                        difference = joeur1.case[2]-case_joeur[2]
                        id_total=[]
                        if difference <= 0:
                                difference=difference*(-1)+1
                        for i in range (difference+1):
                                if(case_joeur[2]+i)>=38:
                                        case_joeur=liste_case[0]
                                if ((case_joeur[2])+i)==Joeur2.case[2]:
                                        id_total.append(Joeur2.id_perso)
                                if ((case_joeur[2])+i)==Joeur3.case[2]:
                                        id_total.append(Joeur3.id_perso)
                                if ((case_joeur[2])+i)==Joeur4.case[2]:
                                        id_total.append(Joeur4.id_perso)

                        for y in range(len(case_random)):
                                if joeur1.case[2]== case_random[y][0]:
                                        if not case_random[y][1]==1 and not case_random[y][1]==2:
                                                id_total.append(case_random[y][1])
                        return id_total

                #permet de crée le plateau et d'afficher les cases spéciales
                def ligne(liste_case,case_random):
                        vérification=False
                        for i in range (len(liste_case)):
                                y=0;bleu=0;vert=0;rouge=0
                                vérification=False
                                while vérification==False and not y==len(case_random):
                                        if liste_case[i][2]==case_random[y][0] and case_random[y][1]==1:
                                                rouge=0; vert=0; bleu=255; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==2:
                                                rouge=128; vert=128; bleu=128; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==5:
                                                rouge=105; vert=105; bleu=105; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==6:
                                                rouge=46; vert=139; bleu=87; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==7:
                                                rouge=0; vert=128; bleu=0; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==8:
                                                rouge=50; vert=205; bleu=50; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==9:
                                                rouge=255; vert=255; bleu=255; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==10:
                                                rouge=112; vert=128; bleu=144; vérification=True
                                        elif liste_case[i][2]==case_random[y][0] and case_random[y][1]==11:
                                                rouge=255; vert=0; bleu=0; vérification=True
                                        elif not liste_case[i][2]==case_random[y][0]:
                                                rouge=255; vert=255; bleu=0; y+=1
                                        if y==len(case_random):
                                                vérification=True

                                pygame.draw.rect(screen, (rouge,vert,bleu), pygame.Rect(liste_case[i][0], liste_case[i][1], 50, 50))

                                pygame.display.flip()

                # permet de choisir aléatoirement le nombre de case de déplacement entre 2 et 12
                def case():
                        case_nombre=random.randint(2,12)
                        return case_nombre


                #permet de déplacer le joeur
                def deplacement(case_nombre, joeur):
                        
                        case=joeur.case
                        test=[0,0,0]
                        for y in range(case_nombre):    
                                i=case[2]

                                if not i==37:
                                        case=liste_case[i+1]
                                elif i==37:
                                        case=liste_case[0]

                        test[0]=case[0]
                        test[1]=case[1]
                        test[2]=case[2]
                        if joeur.id_perso==1: #pour que le joeur 1 reste en haut à gauche
                                test[0]=case[0]
                                test[1]=case[1]
                                test[2]=case[2]
                                joeur.case=test

                        
                        if joeur.id_perso==2: #pour que le joeur 2 reste en haut à droite
                                test[0]=(case[0])+25
                                test[1]=case[1]
                                test[2]=case[2]
                                joeur.case=test

                        if joeur.id_perso==3: #pour que le joeur 3 reste en bas à gauche
                                test[0]=case[0]
                                test[1]=(case[1])+25
                                test[2]=case[2]
                                joeur.case=test

                        if joeur.id_perso==4: #pour que le joeur 4 reste en bas à droite
                                test[0]=(case[0])+25
                                test[1]=(case[1])+25
                                test[2]=case[2]
                                joeur.case=test

                        pygame.display.flip()
                        return joeur.case

                def demande_combat(menu1: menu.game ,joeur: personnage.perso, id, J1: personnage.perso, J2: personnage.perso, J3: personnage.perso, J4: personnage.perso, monstre_total: list[ennemie.monstre]):
                        valide=False
                        image_monstre = pygame.image.load('images/backgroud.jpg')
                        image_monstre = pygame.transform.scale(image_monstre, (50,50))
                        
                        image_demande_combat_J1 = image_monstre.get_rect()
                        image_demande_combat_J1.x = math.ceil(9999)
                        image_demande_combat_J1.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J1) 

                        image_demande_combat_J2 = image_monstre.get_rect()
                        image_demande_combat_J2.x = math.ceil(9999)
                        image_demande_combat_J2.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J2) 

                        image_demande_combat_J3 = image_monstre.get_rect()
                        image_demande_combat_J3.x = math.ceil(9999)
                        image_demande_combat_J3.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J3) 

                        image_demande_combat_J4 = image_monstre.get_rect()
                        image_demande_combat_J4.x = math.ceil(9999)
                        image_demande_combat_J4.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J4)

                        Image_monstre_rect = image_monstre.get_rect()
                        Image_monstre_rect.x = math.ceil(9999)
                        Image_monstre_rect.y = math.ceil(9999)
                        id_monstre=0
                        
                        for i in range(len(id)):
                                if id[i]==1 and menu1.nombre_joeur>=1:
                                        image_demande_combat_J1 = J1.Image2.get_rect()
                                        image_demande_combat_J1.x = math.ceil(150)
                                        image_demande_combat_J1.y = math.ceil(150)
                                        screen.blit(J1.Image2,image_demande_combat_J1) 
                                if id[i]==2 and menu1.nombre_joeur>=2:
                                        image_demande_combat_J2 = J2.Image2.get_rect()
                                        image_demande_combat_J2.x = math.ceil(200)
                                        image_demande_combat_J2.y = math.ceil(200)
                                        screen.blit(J2.Image2,image_demande_combat_J2) 
                                if id[i]==3 and menu1.nombre_joeur>=3:
                                        image_demande_combat_J3 = J3.Image2.get_rect()
                                        image_demande_combat_J3.x = math.ceil(250)
                                        image_demande_combat_J3.y = math.ceil(250)
                                        screen.blit(J3.Image2,image_demande_combat_J3) 
                                if id[i]==4 and menu1.nombre_joeur>=4:
                                        image_demande_combat_J4 = J4.Image2.get_rect()
                                        image_demande_combat_J4.x = math.ceil(300)
                                        image_demande_combat_J4.y = math.ceil(300)
                                        screen.blit(J4.Image2,image_demande_combat_J4)
                        for y in range(len(monstre_total)):
                                for j in range(len(id)):
                                        if monstre_total[y].id_monstre==id[j]:
                                                id_monstre=monstre_total[y]
                                                Image_monstre_rect = ((monstre_total[y]).image_monstre).get_rect()
                                                Image_monstre_rect.x = math.ceil(350)
                                                Image_monstre_rect.y = math.ceil(350)
                                                valide=True
                        pygame.draw.rect(screen, (0,0,0), pygame.Rect(100, 100, 600, 600))
                        if valide==True:
                                screen.blit((monstre_total[y]).image_monstre,Image_monstre_rect) 
                        pygame.display.flip()
                        return id_monstre, Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4


                def fin_demande_combat(menu1: menu.game ,joeur: personnage.perso, id, J1: personnage.perso, J2: personnage.perso, J3: personnage.perso, J4: personnage.perso, monstre_total: list[ennemie.monstre]):
                        image_monstre = pygame.image.load('images/backgroud.jpg')
                        image_monstre = pygame.transform.scale(image_monstre, (0,0))
                        
                        image_demande_combat_J1 = image_monstre.get_rect()
                        image_demande_combat_J1.x = math.ceil(9999)
                        image_demande_combat_J1.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J1) 

                        image_demande_combat_J2 = image_monstre.get_rect()
                        image_demande_combat_J2.x = math.ceil(9999)
                        image_demande_combat_J2.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J2) 

                        image_demande_combat_J3 = image_monstre.get_rect()
                        image_demande_combat_J3.x = math.ceil(9999)
                        image_demande_combat_J3.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J3) 

                        image_demande_combat_J4 = image_monstre.get_rect()
                        image_demande_combat_J4.x = math.ceil(9999)
                        image_demande_combat_J4.y = math.ceil(9999)
                        screen.blit(image_monstre,image_demande_combat_J4)

                        Image_monstre_rect = image_monstre.get_rect()
                        Image_monstre_rect.x = math.ceil(9999)
                        Image_monstre_rect.y = math.ceil(9999)
                        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 9999, 9999))
                        screen.blit(image_monstre,Image_monstre_rect) 
                        pygame.display.flip()
                        return Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4

                ############################## définition des variable ################################

                J1.pv=J1.pv_max # on donne une valeur à pv 
                J2.pv=J2.pv_max
                J3.pv=J3.pv_max
                J4.pv=J4.pv_max

                #liste contenant tout les cases et leurs id
                liste_case =    [(25,25,0),(25,80,1),(25,135,2),(25,190,3),(25,245,4),(25,300,5),(25,355,6),(80,355,7),
                                (135,355,8),(190,355,9),(245,355,10),(300,355,11),(355,355,12),(410,355,13),(465,355,14),
                                (520,355,15),(575,355,16),(630,355,17),(685,355,18),(740,355,19),(740,300,20),(740,245,21),
                                (740,190,22),(685,190,23),(630,190,24),(575,190,25),(520,190,26),(465,190,27),
                                (465,135,28),(465,80,29),(465,25,30),(410,25,31),(355,25,32),(300,25,33),
                                (245,25,34),(190,25,35),(135,25,36),(80,25,37)]

                # on crée les monstres
                zombie_1 = ennemie.monstre(6)
                squelette_1 = ennemie.monstre(5)
                loup1 = ennemie.monstre(7)
                Slime1 = ennemie.monstre(8)
                Chevalier1 = ennemie.monstre(9)
                Dragon = ennemie.monstre(10)
                Phénix = ennemie.monstre(11)

                # on les ajouter dans une liste
                monstre_total=[zombie_1,squelette_1,loup1,Slime1,Chevalier1,Dragon,Phénix]

                plateau=False           # permet d'éviter de réactalisé constament la totalité du tableau
                case_nombre=0           #varaible contenant le nombre de case à ce déplacé
                case_random=random_liste_case() # variable qui contient les cases spéciale

                                # permet d'assigné la bonne image au joeur 1
                if menu1.nombre_joeur>=1:
                        J1.case=liste_case[0]
                        J1.id_perso=1

                # permet d'assigné la bonne image au joeur 2
                if menu1.nombre_joeur>=2:
                        J2.case[0]=(liste_case[0][0])+25
                        J2.case[1]=liste_case[0][1]
                        J2.case[2]=liste_case[0][2]
                        J2.id_perso=2
                
                # permet d'assigné la bonne image au joeur 3
                if menu1.nombre_joeur>=3:
                        J3.case[0]=liste_case[0][0]
                        J3.case[1]=(liste_case[0][1])+25
                        J3.case[2]=liste_case[0][2]
                        J3.id_perso=3
                
                # permet d'assigné la bonne image au joeur 4
                if menu1.nombre_joeur==4:
                        J4.case[0]=(liste_case[0][0])+25
                        J4.case[1]=(liste_case[0][1])+25
                        J4.case[2]=liste_case[0][2]
                        J4.id_perso=4

                # Charger une police
                police = pygame.font.Font(None, 25)
                police2 = pygame.font.Font(None, 17)

                # on ajoute des image pour les pv, l'attaque, la defence, la vitesse et la régeneration de pv
                Image_attaque = pygame.image.load('images/attaque.png')
                Image_attaque = pygame.transform.scale(Image_attaque, (50,50))

                Image_pv = pygame.image.load('images/vie.png')
                Image_pv = pygame.transform.scale(Image_pv, (50,50))

                Image_defence = pygame.image.load('images/defence.png')
                Image_defence = pygame.transform.scale(Image_defence, (50,50))

                Image_vitesse = pygame.image.load('images/vitesse.png')
                Image_vitesse = pygame.transform.scale(Image_vitesse, (50,50))

                Image_regeneration = pygame.image.load('images/régeneration.png')
                Image_regeneration = pygame.transform.scale(Image_regeneration, (50,50))

                joeur=J1
                valide_bouton1=False
                id=[]
                Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 = fin_demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                ############### ###################################### debut de programme principale ###################################
                while menu1.status==True:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        menu1.status = False
                        
                        if J1.score==30000 or J1.score==30000 or J1.score==30000 or J1.score==30000:
                                menu1.status=False

                        #permet d'afficher le plateau avec les cases spéciales et de réactualisé
                        if plateau==False:
                                screen.blit(background,(0,0))
                                ligne(liste_case,case_random)

                                #tableau des dés
                                pygame.draw.rect(screen, (120,60,20), pygame.Rect(1000, 25, 470,170))
                                pygame.draw.rect(screen, (0,128,0), pygame.Rect(1010, 35, 450, 150))


                                #tableau contenant les informations
                                button_des = pygame.image.load('images/lunch.png')
                                button_des = pygame.transform.scale(button_des, (100,100))
                                button_des_rect = button_des.get_rect()
                                button_des_rect.x = math.ceil(200)
                                button_des_rect.y = math.ceil(200)
                                
                                pygame.draw.rect(screen, (120,60,19), pygame.Rect(1000, 200, 470, 300))
                                pygame.draw.rect(screen, (0,128,0), pygame.Rect(1010, 210, 450, 60))

                                screen.blit(Image_pv,(1030, 280, 50, 50)) 
                                screen.blit(Image_regeneration,(1120, 280, 50, 50)) 
                                screen.blit(Image_attaque,(1210, 280, 50, 50)) 
                                screen.blit(Image_defence,(1300, 280, 50, 50)) 
                                screen.blit(Image_vitesse,(1390, 280, 50, 50)) 

                                texte_pv_max, texte_pv, texte_regen, texte_attaque, texte_defence, texte_vitesse = change_information(menu1.tour_joeur)

                                pv = police2.render(str(("PV :" + str(texte_pv) + "/" + str(texte_pv_max))), True, (255,255,255))
                                regen = police2.render(str(("régéneration: " + str (texte_regen))), True, (255,255,255))
                                attaque = police2.render(str(("attaque : " + str (texte_attaque))), True, (255,255,255))
                                defence = police2.render(str(("défence : " + str (texte_defence))), True, (255,255,255))
                                vitesse = police2.render(str(("vitesse : " + str (texte_vitesse))), True, (255,255,255))

                                screen.blit(pv,(1030, 350, 50, 50)) 
                                screen.blit(regen,(1110, 350, 50, 50)) 
                                screen.blit(attaque,(1210, 350, 50, 50)) 
                                screen.blit(defence,(1300, 350, 50, 50)) 
                                screen.blit(vitesse,(1390, 350, 50, 50))

                                if menu1.tour_joeur==1:
                                        Image_main1, Image_main2, Image_casque, Image_pastron, Image_botte = image_equipement(J1)
                                elif menu1.tour_joeur==2:
                                        Image_main1, Image_main2, Image_casque, Image_pastron, Image_botte = image_equipement(J2)
                                elif menu1.tour_joeur==3:
                                        Image_main1, Image_main2, Image_casque, Image_pastron, Image_botte = image_equipement(J3)
                                elif menu1.tour_joeur==4:
                                        Image_main1, Image_main2, Image_casque, Image_pastron, Image_botte = image_equipement(J4)

                                screen.blit(Image_main1,(1030, 370, 50, 50)) 
                                screen.blit(Image_main2,(1110, 370, 50, 50)) 
                                screen.blit(Image_casque,(1210, 370, 50, 50)) 
                                screen.blit(Image_pastron,(1300, 370, 50, 50)) 
                                screen.blit(Image_botte,(1390, 370, 50, 50)) 

                                # permet d'assigné la bonne image au joeur 1
                                if menu1.nombre_joeur>=1:

                                        # Créer un texte pour le nom du personnage sa class et son score
                                        nom_j1_p1 = police.render(str(("nom : " + str (J1.nom))), True, (255,255,255))
                                        class_j1_p1 = police.render(str(("class : " + str (J1.classe))), True, (255,255,255))
                                        score_j1_p1 = police.render(str(("score : " + str (J1.score))), True, (255,255,255))
                                        personnage.perso.updates(J1) # on updates ces stats au cas ou qu'il y aurais eu des changements


                                # permet d'assigné la bonne image au joeur 2
                                if menu1.nombre_joeur>=2:

                                        # Créer un texte pour le nom du personnage sa class et son score
                                        nom_j2_p1 = police.render(str(("nom : " + str (J2.nom))), True, (255,255,255))
                                        class_j2_p1 = police.render(str(("class : " + str (J2.classe))), True, (255,255,255))
                                        score_j2_p1 = police.render(str(("score : " + str (J2.score))), True, (255,255,255))
                                        personnage.perso.updates(J2)# on updates ces stats au cas ou qu'il y aurais eu des changements

                                
                                # permet d'assigné la bonne image au joeur 3
                                if menu1.nombre_joeur>=3:

                                        # Créer un texte pour le nom du personnage sa class et son score
                                        nom_j3_p1 = police.render(str(("nom : " + str (J3.nom))), True, (255,255,255))
                                        class_j3_p1 = police.render(str(("class : " + str (J3.classe))), True, (255,255,255))
                                        score_j3_p1 = police.render(str(("score : " + str (J3.score))), True, (255,255,255))
                                        personnage.perso.updates(J3)# on updates ces stats au cas ou qu'il y aurais eu des changements

                                
                                # permet d'assigné la bonne image au joeur 4
                                if menu1.nombre_joeur==4:

                                        # Créer un texte pour le nom du personnage sa class et son score
                                        nom_j4_p1 = police.render(str(("nom : " + str (J4.nom))), True, (255,255,255))
                                        class_j4_p1 = police.render(str(("class : " + str (J4.classe))), True, (255,255,255))
                                        score_j4_p1 = police.render(str(("score : " + str (J4.score))), True, (255,255,255))
                                        personnage.perso.updates(J4)# on updates ces stats au cas ou qu'il y aurais eu des changements

                                if menu1.nombre_joeur>=1:
                                        pygame.draw.rect(screen, (0,0,255), pygame.Rect(15, 450, 300, 100))
                                        screen.blit(J1.Image_p1, (15, 450)) 
                                        screen.blit(nom_j1_p1, (125, 470))                                  # nom
                                        screen.blit(class_j1_p1, (125, 500))                                # nom class
                                        screen.blit(score_j1_p1, (125, 530)) 

                                if menu1.nombre_joeur>=2:
                                        pygame.draw.rect(screen, (0,0,255), pygame.Rect(400, 450, 300, 100))
                                        screen.blit(J2.Image_p1, (400, 450)) 
                                        screen.blit(nom_j2_p1, (525, 470))                                  # nom
                                        screen.blit(class_j2_p1, (525, 500))                                # nom class
                                        screen.blit(score_j2_p1, (525, 530)) 
                                
                                if menu1.nombre_joeur>=3:
                                        pygame.draw.rect(screen, (0,0,255), pygame.Rect(15, 650, 300, 100))
                                        screen.blit(J3.Image_p1, (15, 650)) 
                                        screen.blit(nom_j3_p1, (125, 670))                                  # nom
                                        screen.blit(class_j3_p1, (125, 700))                                # nom class
                                        screen.blit(score_j3_p1, (125, 730)) 
                                
                                if menu1.nombre_joeur==4:
                                        pygame.draw.rect(screen, (0,0,255), pygame.Rect(415, 650, 300, 100))
                                        screen.blit(J4.Image_p1, (415, 650)) 
                                        screen.blit(nom_j4_p1, (525, 670))                                  # nom
                                        screen.blit(class_j4_p1, (525, 700))                                # nom class
                                        screen.blit(score_j4_p1, (525, 730))

                                
                                spawn_monstre(case_random,liste_case)
                                screen.blit(button_des,button_des_rect)
                                if joeur.case[2]==case_random[1][0] and valide_forge==True:
                                        forge(joeur)
                                        valide_bouton1=True
                                if joeur.case[2]==case_random[0][0] and valide_fontaine==True:
                                        valide_fontaine=False
                                        if not joeur.pv_max==joeur.pv:
                                                joeur.pv+=(joeur.pv_max*0.10)
                                                if joeur.pv_max<joeur.pv: 
                                                        joeur.pv+=joeur.pv_max    
                                valide_demande_combat=False
                                if not len(id)==0:
                                        id_monstre, Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 = demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                                        print(Image_monstre_rect)
                                        valide_demande_combat=True
                                plateau=True


                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if button_des_rect.collidepoint(event.pos):
                                        case_nombre = case()
                                        dep = False
                                        valide_fontaine=False
                                        while dep==False:
                                                if menu1.tour_joeur ==1:
                                                        valide_forge=True
                                                        case_joeur=J1.case
                                                        J1.case=deplacement(case_nombre,J1)
                                                        
                                                        dep = True
                                                        id =verification_joeur(liste_case,case_random,J1, J2, J3, J4, case_joeur)
                                                        time.sleep(0.2)

                                                        if menu1.nombre_joeur>1:
                                                                menu1.tour_joeur = 2
                                                        if not J1.pv_max==J1.pv:
                                                                J1.pv+=J1.reg_pv
                                                                if J1.pv_max<J1.pv: 
                                                                        J1.pv+=J1.pv_max                                   


                                                elif menu1.tour_joeur ==2:
                                                        valide_forge=True
                                                        case_joeur=J2.case
                                                        J2.case=deplacement(case_nombre,J2)

                                                        id =verification_joeur(liste_case,case_random,J2, J1, J3, J4, case_joeur)
                                                        time.sleep(0.2)

                                                        if menu1.nombre_joeur>2:
                                                                menu1.tour_joeur = 3
                                                        else:
                                                                 menu1.tour_joeur = 1
                                                        dep = True
                                                        if not J2.pv_max==J2.pv:
                                                                J2.pv+=J2.reg_pv
                                                                if J2.pv_max<J2.pv: 
                                                                        J2.pv+=J2.pv_max                                   


                                                elif menu1.tour_joeur ==3:
                                                        valide_forge=True
                                                        case_joeur=J3.case
                                                        J3.case=deplacement(case_nombre,J3)

                                                        id =verification_joeur(liste_case,case_random,J3, J1, J2, J4, case_joeur)
                                                        time.sleep(0.2)

                                                        if menu1.nombre_joeur>3:
                                                                menu1.tour_joeur = 4
                                                        else:
                                                                 menu1.tour_joeur = 1
                                                        dep = True
                                                        if not J3.pv_max==J3.pv:
                                                                J3.pv+=J3.reg_pv
                                                                if J3.pv_max<J3.pv: 
                                                                        J3.pv+=J3.pv_max                                   


                                                elif menu1.tour_joeur ==4:
                                                        valide_forge=True
                                                        case_joeur=J4.case
                                                        J4.case=deplacement(case_nombre,J4)

                                                        id =verification_joeur(liste_case,case_random,J4, J1, J2, J3, case_joeur)
                                                        time.sleep(0.2)

                                                        menu1.tour_joeur = 1
                                                        dep = True

                                                else:
                                                        menu1.tour_joeur = 1
                                                        if not J4.pv_max==J4.pv:
                                                                J4.pv+=J4.reg_pv
                                                                if J4.pv_max<J4.pv: 
                                                                        J4.pv+=J4.pv_max                                   




                                if joeur.equipement.Image_main1_rect.collidepoint(event.pos) and valide_bouton1==True:
                                        joeur.equipement.main1_equipe = True
                                        valide_forge=forge_valide(valide_forge)
                                        time.sleep(0.2)
                                        valide_bouton1=False
                                        personnage.perso.updates(joeur)

                                elif joeur.equipement.Image_main2_rect.collidepoint(event.pos) and valide_bouton1==True:
                                        joeur.equipement.main2_equipe = True
                                        valide_forge=forge_valide(valide_forge)
                                        time.sleep(0.2)
                                        valide_bouton1=False
                                        personnage.perso.updates(joeur)

                                elif joeur.equipement.Image_casque_rect.collidepoint(event.pos) and valide_bouton1==True:
                                        joeur.equipement.casque_equipe = True
                                        valide_forge=forge_valide(valide_forge)
                                        time.sleep(0.2)
                                        valide_bouton1=False
                                        personnage.perso.updates(joeur)

                                elif joeur.equipement.Image_botte_rect.collidepoint(event.pos) and valide_bouton1==True:
                                        joeur.equipement.botte_equipe = True
                                        valide_forge=forge_valide(valide_forge)
                                        time.sleep(0.2)
                                        valide_bouton1=False
                                        personnage.perso.updates(joeur)

                                elif joeur.equipement.Image_pastron_rect.collidepoint(event.pos) and valide_bouton1==True:
                                        joeur.equipement.pastron_equipe = True
                                        valide_forge=forge_valide(valide_forge)
                                        time.sleep(0.2)
                                        valide_bouton1=False
                                        personnage.perso.updates(joeur)
                                
                                if button_des_rect.collidepoint(event.pos):
                                        plateau=False
                                        time.sleep(0.2)
                                

                                ################## clique pour la demande de combat ########################
                                if Image_monstre_rect.collidepoint(event.pos) and valide_demande_combat==True:
                                        Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 =fin_demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                                        time.sleep(0.2)
                                        joeur.combat_monstre(id_monstre)
                                        print(joeur.score)
                                        id=[]
                                        plateau=False

                                elif image_demande_combat_J1.collidepoint(event.pos) and valide_demande_combat==True:
                                        Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 =fin_demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                                        time.sleep(0.2)
                                        joeur.combat_joeur(J1)
                                        id=[]
                                        plateau=False

                                elif image_demande_combat_J2.collidepoint(event.pos) and valide_demande_combat==True:
                                        Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 =fin_demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                                        time.sleep(0.2)
                                        joeur.combat_joeur(J2)
                                        id=[]
                                        plateau=False


                                elif image_demande_combat_J3.collidepoint(event.pos) and valide_demande_combat==True:
                                        Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 =fin_demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                                        time.sleep(0.2)
                                        joeur.combat_joeur(J3)
                                        id=[]
                                        plateau=False


                                elif image_demande_combat_J4.collidepoint(event.pos) and valide_demande_combat==True:
                                        Image_monstre_rect, image_demande_combat_J1, image_demande_combat_J2, image_demande_combat_J3, image_demande_combat_J4 =fin_demande_combat(menu1, joeur, id, J1, J2, J3, J4, monstre_total)
                                        time.sleep(0.2)
                                        joeur.combat_joeur(J4)
                                        id=[]
                                        plateau=False


                                if menu1.tour_joeur==1: 
                                        J1=joeur

                                elif menu1.tour_joeur==2:
                                        J2=joeur

                                elif menu1.tour_joeur==3:
                                        J3=joeur

                                elif menu1.tour_joeur==4:
                                        J4=joeur
                                        

                        #affiche le joeur
                        if menu1.nombre_joeur>=1:
                                J1.Image_rect.x = math.ceil(J1.case[0])
                                J1.Image_rect.y = math.ceil(J1.case[1])
                                screen.blit(J1.Image2,J1.Image_rect) 
                        if menu1.nombre_joeur>=2:
                                J2.Image_rect.x = math.ceil(J2.case[0])
                                J2.Image_rect.y = math.ceil(J2.case[1])
                                screen.blit(J2.Image2,J2.Image_rect) 
                        if menu1.nombre_joeur>=3:
                                J3.Image_rect.x = math.ceil(J3.case[0])
                                J3.Image_rect.y = math.ceil(J3.case[1])
                                screen.blit(J3.Image2,J3.Image_rect) 
                        if menu1.nombre_joeur==4:
                                J4.Image_rect.x = math.ceil(J4.case[0])
                                J4.Image_rect.y = math.ceil(J4.case[1])
                                screen.blit(J4.Image2,J2.Image_rect,) 



                        pygame.display.flip()

                pygame.quit()
                quit()
