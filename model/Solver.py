import sys

# Les quatre fonctions arithmetiques de base

add = lambda x, y: x + y

sub = lambda x, y: x - y

mul = lambda x, y: x * y

div = lambda x, y: x // y


class Operation:
    """
     Classe associant une operation a sa description textuelle, pour pouvoir
     afficher le detail des calculs effectues lorsqu'on a trouve le resultat.
     """
    def __init__(self, func, desc):
        """
         Constructeur : initialise les deux champs
         func : pointeur vers la function qui fait le calcul
         desc : chaine de caractere, descriptif
         """
        self.func = func
        self.desc = desc

# Les quatre operations
#
# ALL_OPERATIONS = (Operation(add, "+"), Operation(sub, "-"),
#
#                   Operation(mul, "x"), Operation(div, ":"))
#
# # Les operations qui ne peuvent pas donner 0 comme resultat
# OPERATIONS = (Operation(add, "+"), Operation(mul, "x"),
#               Operation(div, ":"))



    # ----------------------------------------------------------------------------


class PairIterator:


    """
     Classe donnant une suite de paire de nombres a partir d'une liste de
     nombres.

     """
    def __init__(self, nums):
        assert len(nums) >= 2, "La liste doit contenir au moins 2 elements"
        self.nums = nums
        self.index1 = 0
        self.index2 = 1
    def __iter__(self):
        """ La classe est son propre iterateur. """
        return self
    def __next__(self):
        """ Renvoie la prochaine paire d'entiers """
        # Si on est arrive au bout de la liste de paires
        if self.index2 == len(self.nums):
            raise StopIteration

            # Cree une paire

        p = (self.nums[self.index1], self.nums[self.index2])
        # Avance la position pour la prochaine fois

        if self.index2 < len(self.nums) - 1:
            self.index2 += 1
        else:
            self.index1 += 1
            self.index2 = self.index1 + 1
        return p
    def next(self):
        """
         Meme fonction que la precedente, par souci de compatibilite
         avec python 2.x
         """
        return self.__next__()

def algo(entiers, aTrouver,stop, log=[] ):
    """
     Fonction de recherche de solutions.
     Parametres:
         entiers: liste de donnees utilisables (entiers)
         aTrouver: resultat auquel aboutir (entier)
         log: liste des operations deja effectuees (liste de chaines)
     """
    # Pour chaque paire d'entiers
    paires = PairIterator(entiers)
    for paire in paires:
        if not stop[0] :
            # On evite de faire des calculs qui donnent 0 comme resultat
            ops = list()
            ops.append(Operation(add, "+"))
            if paire[0] > paire[1] :
                ops.append(Operation(sub, "-"))
            if paire[0] > paire[1] > 1 and paire[0] % paire[1] == 0:
                ops.append( Operation(div, ":"))
            if paire[0] != 1 and paire[1] != 1 :
                ops.append(Operation(mul, "x"))

            for op in ops:
                # On fait le calcul
                resultat = op.func(paire[0], paire[1])
                # Note l'operation dans le journal
                log.append("%d %s %d = %d" % (paire[0], op.desc, paire[1],resultat))
                # Si on a trouve la solution
                if resultat == aTrouver:
                    # On affiche les operations effectuees et on quitte
                    # for ligne in log:
                    #     print(ligne)
                    stop[0]=True
                    break
                else:
                    # On prend les autres nombres et le resultat de l'operation
                    entiers2 = [n for n in entiers if n not in paire]
                    entiers2.append(resultat)
                    # et on recommence
                    entiers2.sort(reverse=True)
                    if len(entiers2) >= 2:
                        algo(entiers2, aTrouver,stop, log)
                        # L'operation n'a pas donne de resultat, on l'enleve du journal
                        if stop[0] :
                            break
                log.pop()
        else :
            break

# ----------------------------------------------------------------------------

# VALIDES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100)
#
# if len(sys.argv) != 8:
#
#     print("Pas assez d'arguments.")
#
#     print("usage : compte nb1 nb2 nb3 nb4 nb5 nb6 aTrouver")
#
#     sys.exit(1)
# else:
#
#     try:
#         entiers = [int(i) for i in sys.argv[1:7]]
#         aTrouver = int(sys.argv[-1])
#     except:
#         print("Les arguments de ce programmes doivent etre des entiers")
#         sys.exit(2)
#
#         # Verifie que le nombre a trouver est valide
#
#     if aTrouver <= 100 or aTrouver >= 1000:
#         print("Argument invalide")
#         print("Le nombre a trouver doit etre compris entre 101 et 999")
#         sys.exit(3)
#
#     # Verifie que tous les nombres sont dans la liste des valides
#
#     if any(e not in VALIDES for e in entiers):
#         print("Argument(s) invalide(s)")
#         print(("Les nombres doivent etre dans la liste %s" % (str(VALIDES))))
#         sys.exit(3)
#
# entiers.sort(reverse=True)
# stop = list()
# stop.append(False)
# log=list()
# algo(entiers, aTrouver,stop,log=log)
# if len(log) == 0 :
#     print("Aucun resultat.")
# else :
#     print(log)
