Ceci est un projet qui presente quelques algorithmes utiles que vous pouvez etudier ou utiliser
dans vos applications.

1. Algorithme de tri (algo_tri.py)
----------------------------------
Les algorithmes de tri sont tres utilises dans plusieurs applications et domaines. Ils permettent 
de trier rapidement un ensemble de donnee dans l'ordre voulue. Je vous presente quelques 
algorithmes de tri que j'ai implemente :

    - Tri par selection : consiste a rechercher l'element ayant la valeur minimal dans une liste
et l'echanger contre l'element indice i pour avoir un nouveau tableau sans compter l'element 
indice i 
    - Tri a bulle : consiste a deplacer les plus grands elements en fin du tableau a chaque 
iteration
    - Tri par fusion : diviser pour regner, diviser la liste en deux parties puis deplacer
a gauche le plus petit et a droite le plus grand, ensuite diviser la sous liste en deux 
parties et ainsi de suite jusqu'a diviser au plus petit element possible et de deplacer a gauche
le plus petit, a droite le plus grand. Au final, on obtient une liste trie.

2. Algorithme de recherche (algo_recherche.py)
----------------------------------------------
Les algorithmes de recherche permet de rechercher un element dans une liste. Ce procedure demande 
beaucoup de comparaison a chaque boucle donc couteux en temps. Raison pour laquelle il faut bien
choisir son algorithme de tri dans ses applications. Voici l'algorithme de recherche que je vois
tres performant en terme de temps et puissant en terme de resultat :
    
    - la recherche par dichotomie : le fameux diviser pour regner, il suffit de diviser la liste
en deux parties et de verifier si l'element se trouve a gauche ou droite ou au milieu. Prendre la 
direction trouve et le diviser encore afin de le recherche, et ainsi de suite jusqu'a trouver 
l'element rechercher.

3. Arbre binaire (arbre_binaire.py)
-----------------------------------
En implementant un arbre binaire dynamique sachant que les plus petits elements se trouvent a 
gauche et a droite les plus grands, les operations basiques sur les listes gagnent en temps de 
calcul tels que les operations de tri, recherche, ajout, suppression, minimum et maximum.
Note : Installer la librairie graphviz pour afficher le binaire en tant que image.

4. Algorithme a glouton (algo_glouton.py)
-----------------------------------------
Cette algorithme permet de rechercher les combinaisons optimales dans une liste en precisant les
valeurs possibles a utiliser. L'algorithme que j'ai concu permet de resoudre le probleme de rendu 
monnaie ou sac a dos.

5. Shunting yard et npi
-----------------------
Algorihme implemente dans les calculatrices en convertissant une expressiona algebrique a une 
expression polonaise et en effectuant des operations arihtmetiques sur l'expression polonaises tout
en respectant les regles de priorite.
