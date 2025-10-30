# TP Python : Gestion d’une bibliothèque
# Objectif : Créer une application console en Python qui simule la gestion d'une bibliothèque en utilisant toutes les notions avancé : heritage, abstraction, enum, gestions des exceptions.

# Taches :
# Créer une classe abstraite Document qui représentera l’élément de base de votre bibliothèque. Elle contiendra :

# un attribut de classe nb_document (int)
# la propriété titre (String)
# la propriété anneePublication (Int)
# une méthode abstraite afficherInfos() qui sera redéfinie pour afficher les détails spécifique
# une méthode de classe afficherNbDocument() qui affichera le nombre de document instancié

from abc import ABC, abstractmethod
from enum import Enum 

class Document(ABC) :
    nb_document = 0
    
    def afficherNbDocument(self) :
        return self.nb_document
    
    def __init__(self,titre : str,anneePublication : int) :
        self.titre = titre
        self.anneePublication = anneePublication
    
    @abstractmethod
    def afficherInfos(cls) :
        pass

    

# Créer une classe enum Genre qui permettra de classifier les livres par catégorie.
# Ex: ROMAN, SCIENCE_FICTION, FANTASTIQUE

class Genre(Enum) :
    ROMAN = 1
    SCIENCE_FICTION = 2
    FANTASTIQUE = 3

# Créer une classe abstraite Empruntable que sera hérité par Livre uniquement contenant :
# une propriété estEmprunte: Boolean,
# une méthode abstraite emprunter()
# une méthode abstraite rendre()

class Empruntable(ABC):
    def __init__(self):
        self.estEmprunte = False
    
    @abstractmethod
    def emprunter(self) :
        pass
    
    @abstractmethod
    def rendre(self) :
        pass   

# Créer une classe abstraite Consultable qui sera implémenté par Livre et Magazine contenant :

# une méthode abstraite consulter() qui affiche : "Vous consultez ce document."

class Consultable(ABC) : 
    @abstractmethod
    def consulter(self) :
        pass
           
# Créer 2 exceptions personnalisé : DocumentDejaEmprunteException et DocumentNonEmprunteException

class DocumentDejaEmprunteException(Exception) :
    pass

class DocumentNonEmprunteException(Exception) :
    pass

# À partir de Document, créer deux classes :

# Une classe Livre qui contiendra :
# une propriété auteur: String,
# une propriété nbPages: Int
# une propriété genre: Genre (enum)
# un constructeur secondaire (methode static) qui ne prend que le titre, l'auteur et le genre (nbPages sera à 100 et anneePublication à 0 par défaut)
# une méthode static compteurPages() qui prend une liste de Livre et retourne le total de pages.


class Livre(Document,Empruntable,Consultable) :
    def __init__(self,titre : str,anneePublication : int, auteur : str, nbPages : int, genre : Genre) :
        Document.__init__(self,titre,anneePublication)
        Empruntable.__init__(self)
        self.auteur = auteur
        self.nbPages = nbPages
        self.genre = genre
    
    @staticmethod
    def intialiser_livre(self,titre,auteur,genre) :
        return self.__init_(titre,0,auteur,100,genre)
    
    @staticmethod
    def compteurPages(liste_livres : list) : 
        compteur_livre = 0
        for livre in liste_livres :
            compteur_livre += livre.nbPages
    
    def afficherInfos(self):
        print()
        print(f"======= {self.titre} =========")
        print(f"année de publication : {self.anneePublication}")
        print(f"auteur : {self.auteur}")
        print(f"nombre de pages : {self.nbPages}")
        print(f"genre : {Genre(self.genre)}")
        
        
            
    # Implémenter les méthodes emprunter() et rendre() dans Livre afin quelle consulte le booléen estEmprunte :
    # Si nous pouvons l'emprunter ou le rendre alors afficher un texte de succès.
    # Sinon renvoyé l'exception correspondante.        
    def emprunter(self) :
        try :
            if self.estEmprunte == True :
                raise DocumentDejaEmprunteException("Livre déjà emprunté") 
        except DocumentDejaEmprunteException as ddee :
                print(ddee)    
        else :
            self.estEmprunte = True
            print("emprunt réalisé avec succès")
                     
    def rendre(self) :
        try :
            if self.estEmprunte == False :
                raise DocumentNonEmprunteException("Livre non emprunté") 
        except DocumentNonEmprunteException as ddee :
                print(ddee)    
        else :
            self.estEmprunte = False
            print("restitution réalisée avec succès")
              
        
    def consulter(self) :
        print("vous consulter ce livre : ", self.titre)
    
# Une classe Magazine qui contiendra :
# une propriété numero: Int

class Magazine(Document,Consultable):
    def __init__(self, numero : int,titre : str,anneePublication : int ) :
        super().__init__(titre,anneePublication)
        self.numero = numero
        self.titre = titre
    
    def consulter(self) :
        print("vous consulter ce magazine : ", self.titre)

    def afficherInfos(self):
        print()
        print(f"======= {self.titre} =========")
        print(f"numero : {self.numero}")
        print(f"année de publication : {self.anneePublication}")
        

 
# Dans la fonction principale :

# Créez plusieurs livres (de genres différents) et magazines.   
#self,titre : str, anneePublication : int, auteur : str, nbPages : int, genre : Genre

l1 = Livre("Livre1",1975,"toto1","250",1)
l2 = Livre("Livre2",1976,"toto2","260",2)
l3 = Livre("Livre3",1977,"toto3","240",2)
l4 = Livre("Livre4",1978,"toto4","280",3)

m1 = Magazine(1,"Magazine1",1981)
m2 = Magazine(2,"Magazine2",1982)
m3 = Magazine(3,"Magazine3",1983)
m4 = Magazine(4,"Magazine4",1984)


# Stockez-les dans une liste.

liste_livres_magazines = [l1,l2,l3,l4,m1,m2,m3,m4]

# Affichez la liste complète des documents avec afficherInfos().
for lm in liste_livres_magazines :
    lm.afficherInfos()

# Simulez plusieurs actions :




# consultation d’un livre ou d’un magazine
print()
print("=========== consultation =========")
liste_livres_magazines[3].consulter()

# emprunt d’un livre
print()
print("=========== EMPRUNTER UN LIVRE =========")
liste_livres_magazines[3].emprunter()

# tentative d’emprunt d’un livre déjà emprunté

print()
print("=========== EMPRUNTER UN LIVRE =========")
liste_livres_magazines[3].emprunter()

# retour d’un livre emprunté
print()
print("=========== EMPRUNTER UN LIVRE =========")
liste_livres_magazines[3].rendre()

# tentative de rendre un livre non emprunté
print()
print("=========== EMPRUNTER UN LIVRE =========")
liste_livres_magazines[3].rendre()


def IHM() :
    print("====== GESTION BIBLIOTHEQUE ======")
    print("1. Consulter")
    print("2. Emprunt")
    print("3. Restitution")
    print("4. ajouter un livre")
    print("5. retirer un livre")
    print("0. Quitter")


def ajouter_livre(blibliotheque):
    #titre : str, anneePublication : int, auteur : str, nbPages : int, genre : Genre   
    titre = input("titre du livre à ajouter : ")
    anneePublication = int(input("année de publication du livre à ajouter : "))
    auteur = input("auteur du livre à ajouter : ")
    nbPages = int(input("Nombre de pages du livre à ajouter : "))
    genre=0
    while genre not in Genre : 
        for genre in Genre :
            print(genre.value, " : ", genre.name )
        genre = int(input("Genre du livre à ajouter : "))
    livre = Livre(titre,anneePublication,auteur,nbPages,genre)
    bibliotheque.append(livre)



def retirer_livre(bibliotheque) :
    print("===== RETIRER LIVRE ==========")
    if len(bibliotheque) == 0 :
        print("--------AUCUN LIVRE A RETIRER --------------")
    else :
        afficher_bibliotheque(bibliotheque)
        index_livre = int(input("Numéro du livre à supprimer : "))
        bibliotheque.remove(index_livre-1)

def afficher_bibliotheque(bibiotheque) :
    print()
    print("==== CONSULTATION ========")
    for i,l in enumerate(bibliotheque) :
        print(f"--- Livre n°{i+1} ---")
        l.afficherInfos()
    print()   
    
    
    
    
        
bibliotheque = []
while True :
    IHM()
    choix = input("Que souhaitez-vous faire : ")
    match choix :
        case "1" :
            afficher_bibliotheque(bibliotheque)
        case "2" :
            pass
        case "3" :
            pass
        case "4" :
            ajouter_livre(bibliotheque) 
        case "5" :
            print("toto")
            retirer_livre(bibliotheque)
        case "0" :
            exit()     
  

# Bonus :
# Chacune des classes doivent être dans des scripts à part, puis importer dans le script principal.

# Créer un IHM permettant à l'utilisateur d'effectuer toutes les actions précédentes jusqu'à ce qu'il quitte le programme :

# ====== GESTION BIBLIOTHEQUE ======
# 1. Consulter
# 2. Emprunt
# 3. Restitution
# 0. Quitter
# Nous pourrons également ajouter une option Ajouter Document et Retirer Document
# Exemple :

# --- Liste des documents ---
# Livre: "The Witcher", Andrzej Sapkowski, 1993, 320 pages, Genre: FANTASTIQUE
# Magazine: "Canard PC", n°420, 2023
# Livre: "Harry Potter", J.K. Rowling, 0000, 100 pages, Genre: ROMAN

# Consultation du magazine "Canard PC"...
# Vous consultez ce document.

# Tentative d’emprunt du livre "The Witcher"...
# Emprunt réussi !

# Tentative d’emprunt du livre "The Witcher" à nouveau...
# ERREUR : Ce livre est déjà emprunté !

# Tentative de rendre le livre "Harry Potter" sans l’avoir emprunté...
# ERREUR : Ce document n’a pas été emprunté !

# Retour du livre "The Witcher"...
# Le livre est maintenant disponible.
