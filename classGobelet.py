from classDes import Des
from random import randint
class Goblet:
    def __init__(self, nb_des, tabDes:Des, valeur=0):
        self.valeur = valeur # la somme des valeurs des "des" d'un goblet
        self.nbDes = nb_des  # nombre de des
        self._tab = [nb_des] # tableau de des
        self.tab = tabDes
    
    @property    
    def valeur(self):
        return self._valeur
    
    def valeur(self, s):
        self._valeur=s
    
    @property
    def nbDes(self):
        return self._nbDes
    
    @nbDes.setter
    def nbDes(self, nb_des):
        self._nbDes= nb_des

    @property
    def tab(self):
        return self._tab
    
    @tab.setter
    def tab(self, tabDes:Des):
        self._tab = tabDes
   
    def lancer(self):
        """
            Cette fonction sert a lancer les d'un d'un goblet
            parametre 
            -------
                none
            return
            -------
                none
        """
        for des in self.tab:
           self.valeur+= des.lancer() 
        
    def afficher_score(self):
        print(f"Voici le score du dernier lancer ", {self.valeur}) 
    


# des= Des()
# des2= Des()
# tab=[]
# tab.append(des)
# tab.append(des2)
# goblet = Goblet(2,tab)
# goblet.afficher_score()
