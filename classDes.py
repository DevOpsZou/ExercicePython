from random import randint
class Des:
    
    def __init__(self, valeur=0):
        self.valeur=valeur
        
    
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self, v):
        self._valeur = v
    
    
    def lancer(self):
        """
            Cette fonction sert a lancer un des en lui attribuant un random entre 1 et 6
            parametre 
            -------
                none
            return
            -------
                int
                    la valeur du des lancé
        """
        self.valeur=randint(1,6)
        print(f"voici le des lancé : {self.valeur}")
        return self.valeur
        
    
   
