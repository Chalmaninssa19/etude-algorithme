# Tri par selection
def triSelection(tab) :
    for i in range(len(tab)) :
        for j in range(i+1, len(tab)) :
            if (tab[j] < tab[i]) :
                p = tab[i]
                tab[i] = tab[j]
                tab[j] = p
    return  tab
ls = [7, 4, 3, 2, 0, 9, 8, 23, 21, 45, 12, 15, 43]
print(triSelection(ls))

# Tri a bulles  
def triBulle(tab) :
    for i in range(len(tab)-1, 0, -1) :
        trier = True
        for j in range (0, i) :
            if (tab[j] > tab[j+1]) :
                p = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = p
                trier = False
        if(trier) :
            return tab
    return tab
list = [ 45, 23, 22, 14, 32, 48, 34]
print(triBulle(list))

# Tri par fusion
def tri_fusion(list) :
    if(len(list) <= 1) :
        return list
    
    # Diviser la liste en deux parties égales
    milieu = len(list) // 2
    left = list[:milieu]
    right = list[milieu:]
    
    # Trier récursivement chaque moitié
    left_trier = tri_fusion(left)
    right_trier = tri_fusion(right)
    
    # Fusionner les deux moitiés triées en une seule liste triée
    return fusion(left_trier, right_trier)

# Fusionner les listes de gauches aux listes de droites
def fusion(left,right) :
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

list = [ 55, 6, 4, 14, 32]
print(tri_fusion(list))