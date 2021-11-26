  
from classPartie import Partie
import time

def main(nbTours, nbDes, nbrJoueur):
    """
        Cette fonction sert à lancer la partie
        parametres
            -------
            
                nombre de tour
                nombre de des
                nombre de joueurs
        return
            -------
                Goblet
                    
    """   
    partie=Partie(nbTours, nbDes, nbrJoueur)
    partie.lancer()

if __name__ == "__main__":
    try :
        nbTours=int(input("Veuillez saisir le nombre de tour :"))
        while(nbTours<2): 
            print("Veuillez saisir un nombre de joueurs d'au moins deux ")
            nbTours=int(input("Veuillez saisir le nombre de tour :"))
        nbDes=int(input("Veuillez saisir le nombre de Des :"))
        nbrJoueur=int(input("Veuillez saisir le nombre de joueur :"))
 
        main(nbTours, nbDes, nbrJoueur)
    except ValueError :
        print("veuillez saisir un nombre ")
