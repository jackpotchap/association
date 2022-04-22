class Cour:
    """
    Classe Casier
    """

    def __init__(self, sigle_cours: str = "", titre_cours: str = "", nb_heure_de_cours: int = -1):
        """
        Méthode constructeur
        Définition des attributs de la classe Casier
        """
        
        self.__sigle_cours = sigle_cours
        self.__titre_cours = titre_cours
        self.__nb_heure_de_cours = nb_heure_de_cours



    """
    Méthode accesseur et mutateur des attributs

    """

    def __str__(self):
        return f"{self.Sigle_cours} : {self.Titre_cours} : {self.Nb_heure_de_cours}"

    def _get_sigle_cours(self) -> str:

        return self.__sigle_cours

    def _set_sigle_cours(self, p_sigle_cours):
        if len(p_sigle_cours) == 5:
            if p_sigle_cours[0].isalpha() and p_sigle_cours[1:].isnumeric():
                self.__sigle_cours = p_sigle_cours

    # propriétés numero casier

    Sigle_cours = property(_get_sigle_cours, _set_sigle_cours)

    ###############################

    def _get_titre_cours(self) -> str:

        return self.__titre_cours

    def _set_titre_cours(self, p_titre_coursr):

        if len(p_titre_coursr) <= 60:
            self.__titre_cours = p_titre_coursr


    Titre_cours = property(_get_titre_cours, _set_titre_cours)

    def _get_nb_heure_de_cours(self) -> int:

        return self.__nb_heure_de_cours

    def _set_nb_heure_de_cours(self, p_nb_heure_de_cours : int):

        if p_nb_heure_de_cours >= 0:
            self.__nb_heure_de_cours = p_nb_heure_de_cours


    Nb_heure_de_cours = property(_get_nb_heure_de_cours, _set_nb_heure_de_cours)


