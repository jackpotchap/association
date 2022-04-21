class Casier:
    """
    Classe Casier
    """


    def __init__(self, p_numero_casier:str = "", p_taille_casier:str = "", p_localisation_casier:str = "", p_prix_casier:float = 20 ):
        """
        Méthode constructeur
        Définition des attributs de la classe Casier
        """

        self.__numero_casier = p_numero_casier
        self.taille_casier = p_taille_casier
        self.localisation_casier = p_localisation_casier
        self.__prix_casier = p_prix_casier

    """
    Méthode accesseur et mutateur des attributs
    
    """
    def __str__(self):
        return f"{self.__numero_casier} : {self.taille_casier} : {self.localisation_casier}"
    def _get_numero_casier(self) -> str:

        return self.__numero_casier


    def _set_numero_casier(self, p_numero_casier):
        if len(p_numero_casier) == 5:
            if p_numero_casier[0].isalpha() and p_numero_casier[1:].isnumeric():
                self.__numero_casier = p_numero_casier


    #propriétés numero casier

    Numero_casier = property(_get_numero_casier, _set_numero_casier)


    ###############################

    def _get_prix_casier(self) -> str:

        return self.__prix_casier

    def _set_prix_casier(self, p_prix_casier):

        if p_prix_casier > 0:
            if p_prix_casier.isnumeric():
                self.__prix_casier = p_prix_casier

    Prix_casier = property(_get_numero_casier, _set_prix_casier)

