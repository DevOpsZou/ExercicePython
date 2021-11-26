from classGobelet import Goblet

class Joueur:
    def __init__(self, nom, scoreInit = 0):
        self.nom = nom # nom du joueur
        self._score = scoreInit # le score initial du joueur=0
        
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, n):
        self._nom = n
        
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, s):
        self._score = self.score + s
      
    def jouer(self, gobelet: Goblet):
        """
            Cette fonction permet de simuler un tour de jeu d'un joueur
            parametre 
            -------
                Goblet
                    parametre de type Goblet

            return
            -------
                none
        """        
        gobelet.lancer()
        self.score = gobelet.valeur
    
    def afficher_score(self):
        return f"Voici le score du joueur {self.nom} : {self.score}"
        

        