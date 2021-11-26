from classJoueur import Joueur
from classDes import Des
from classGobelet import Goblet
from bcolor import Bcolors
class Partie:
    def __init__(self, b_tours, nb_des, nbrJoueur):
        self.bTours=b_tours # nombre de tour
        self.nbDes= nb_des # nombre de des
        self._nbrJoueur=nbrJoueur # nombre de joueur
        self._joueurs=[] # tableau de joueur
     
    @property
    def nbrJoueur(self):
       return self._nbrJoueur
    
    @nbrJoueur.setter
    def nbrJoueur(self, nbrJoueur):
        self._nbrJoueur=nbrJoueur
        
    @property
    def bTours(self):
       return self._bTours
    
    @bTours.setter
    def bTours(self, bTours):
        self._bTours=bTours
        
    @property
    def nbDes(self):
       return self._nbDes
   
    @nbDes.setter
    def nbDes(self, nbd):
        self._nbDes=nbd
    
    @property
    def joueurs(self):
       return self._joueurs
   
    def initialiser(self):
        """
            Cette fonction permet d'initialiser le tableau des joueurs
            en fonction du nombre de joueur renseigné à l'instantiation de 
            l'objet Partie
            parametres
            -------
                none
            return
            -------
                none
        """     
        for i in range(0, self.nbrJoueur):
            nom = input("veuillez saisir votre nom :") 
            joueur=Joueur(nom,0)                       # instantiation d'un objet joueur
            self._joueurs.append(joueur)               # Maj du tableau des joueurs
           
        
    def initDesEtGoblet(self):
        """
            Cette fonction initialise le tableau des des et le goblet avec les des
            parametres
            -------
                none
            return
            -------
                Goblet
                    
        """   
        tabDes=[]
        tabDes.clear
        for i in range (0, self.nbDes):                  # boucle pour l'instatiation des des 
            des=Des()
            tabDes.append(des)
        goblet = Goblet(self.nbDes, tabDes, valeur=0)     # créer le goblet et lui injecté le tableau de des
        return goblet
    
    def lancer(self):
        """
            Fonction principale permettant de Lancer le jeu 
            lance la fonction initialiser
            execute la fonction initDesEtGoblet pour chaque tour de jeu 
            (ce qui permet d'avoir un goblet avec  valeur à zero en début de chaque tour de jeu)
            Affiche le gagnant à al afin du jeu : fonction afficher_gagnant() 
            parametres
            -------
                none
            return
            -------
                none
        """   
        self.initialiser()
        nbTours=0
        print("---------------Debut du jeu---------------------------")
        while nbTours <= self.bTours:
            print("nbre tour ",self.bTours)
            for joueur in self.joueurs:
                goblet=self.initDesEtGoblet()
                print(f"{joueur.nom} c'est à votre tour de joeur :")
                joueur.jouer(goblet)
                print(joueur. afficher_score())
                print("-----------------------------------------")
            nbTours+=1
                
        self.afficher_gagnant()      
                
    def afficher_gagnant(self):
        name=" "
        tabScore=[i.score for i in self.joueurs] # cherche le max des scores
        name = [joueur.nom for joueur in self.joueurs if joueur.score==max(tabScore)] # trouve le nom du gagnant
        print(f"Voici le gagnant {name[0]} avec un score de {max(tabScore)}")
       
                
        
        
        