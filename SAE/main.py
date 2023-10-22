import menu
import jeux
import choix_class

menu1, run3 = menu.game.lancement()


if run3==True:
    J1,J2,J3,J4 = choix_class.choix_perso.choix(menu1)
    jeux.partie.lancement_jeux(menu1,J1,J2,J3,J4)