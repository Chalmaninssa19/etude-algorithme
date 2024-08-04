# Combinaisons de t elements possibles dont la somme de ces elements soit egale a un nombre n
def liste_elements(n, t, element_min=1):
    # Si la taille est 1, la seule liste valide est la liste avec un seul élément de valeur n
    if t == 1:
        if n >= element_min:
            return [[n]]
        else:
            return []
    # Sinon, on doit générer toutes les listes possibles
    # en utilisant chaque élément minimum possible et en réduisant le nombre et la taille
    result = []
    for i in range(element_min, n // t + 1):
        sub_lists = liste_elements(n - i, t - 1, i)
        for sub_list in sub_lists:
            result.append([i] + sub_list)
    return result
print(liste_elements(6,5))

# Est ce que tous les elements de la liste list est egale au liste system 
def exist(listes, system) :
    for liste in listes :
        if liste not in system :
            return False
    return True

# L'algorithme a glouton
def algoGlouton(nombre,system) :
    tab = []
    maxi = max(system)
    while(nombre-maxi != 0) :
        if (nombre-maxi) >= 0 :
            nombre = nombre-maxi
            tab.append(maxi)
            if(nombre-maxi == 0) :
                tab.append(maxi)
        else :
            system.remove(maxi)
            maxi = max(system)
            if(nombre-maxi == 0) :
                tab.append(maxi)
    return tab
print(algoGlouton(6, [1,3,4]))

# L'algorithme optimise de l'algorithme a glouton 
# (Cherche des pieces minimal pour un rendu de pieces)
def algoOptimise(nombre, system) :
    for division in range(nombre+1) :
        # Toutes les combinaisons possibles de division elements dont la somme soit egale au nombre
        combinaisonSumPossible = liste_elements(nombre, division+1) 
        for item in combinaisonSumPossible :
            if exist(item,system) == True :
                return item
    return "Y a pas de solution optimise pour votre piece disponible"
print(algoOptimise(6, [1,3,4]))
