# trop contente - mon premier code en Python !

# premiere etape : on importe la boite a outils permettant à l'ordinateur de choisir un nombre au hasard. On importe la fonction random de la bibliotheque / package randint
# pour importer tout random : import random mais attention les perfs !
from random import randint

# deuxieme etape : je demande à l'ordinateur de choisir un nombre au hasard entre 1 et 100 et je stocke cette valeur dans une variable nommée : nombre_ordinateur
nb_ordinateur = randint(1,10)

# affichage de test
print("le nombre magique est :", nb_ordinateur)


# challenge 5 : le jeu s'arrête quand le joueur a trouvé le bon nombre
trouve = 0

# challenge 6 : en combien de coup on a trouvé le nombre magique
nb_coup = 0

games = []

while trouve == 0 :
  # troisieme etape : je demande au joueur de taper (input) un nombre que je stocke dans la variable nombre_joueur
  # input considere que ce qu'il reçoit est une chaîne de caracteres
  nb_joueur = input("Quel est votre nombre entre 1 et 10 ? ")

  # challenge 3 : on vérifie que l'utilisateur indique bien un int
  # le while True : n'est pas utile
  while True :
    try :

      # simplification de code
      nbjint = int(nb_joueur)
      nb_coup = nb_coup + 1

      # challenge 2 : vérifier que le chiffre donné par l'utilisateur est bien compris entre 1 et 10
      if (nbjint > 10 or nbjint < 1) :
        print("Entre 1 et 10 on t'a dit !!! ")

      # comparaison des deux nombres
      elif (nbjint == nb_ordinateur) :
        print("Trop forte ! tu as trouvé en", nb_coup, "coups ! ")
        # challenge 7 : une nouvelle partie
        new_game = input("Veux-tu refaire une partie ? (Y/N) ")
        while (new_game != "Y" and new_game != "N") :
          new_game = input("Oui = Y ou Non = N ? ")
        if new_game == 'Y' :
          print("=====>>> NOUVELLE PARTIE <<<=====")
          nb_coup = 0
        else :
          print("=====>>> BYE BYE ! <<<=====")
          # challenge 8 : on conserve les scores
          games.append(nb_coup)
          trouve = 1
      elif (nbjint > nb_ordinateur) :
        print("Oula ma grande ! c'est beaucoup trop ! ")
        print("Un indice, tu es à ", abs(nbjint-nb_ordinateur) , "près...")
      else :
        print("Bon... faut rêver plus grand ! ")
        print("Un indice, tu es à", abs(nbjint-nb_ordinateur) , "près...")
      
      # challenge 4 : l'ordinateur indique la différence entre son nombre et celui tapé par le joueur

  
      break

    except ValueError :
      nb_joueur = input("Hey cocotte, on veut un int ! Try again ")
      nb_coup = nb_coup + 1



      # cf code combat ou France ioi ou teachers du net
