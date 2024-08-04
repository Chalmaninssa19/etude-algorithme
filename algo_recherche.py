# Recherche par dichotomie
def recherche_dichotomie(list, element) :
    n = len(list)
    if n == 0 :
        return None
    mid = n // 2
    if list[mid] == element :
        return element
    elif element < list[mid] :
        return recherche_dichotomie(list[0:mid],element)
    else:
        return recherche_dichotomie(list[mid+1:n],element)


#Existe t-il deux elements dans notre systeme dont la somme des elements est egale a T nombre 
#qu'on a choisi en utilisant la recherche par dichotomie
#existe t-il 2 elements dont leur somme donne T
def find_two_numbers_with_sum_T(system, T, lists):
    for i in system :
        if recherche_dichotomie(system,T-i) != i and recherche_dichotomie(system,T-i) in system:
            lists.append(i)
            lists.append(T-i)
            print("les elements sont :"+str(i)+", "+str(T-i))
            return recherche_dichotomie(system,T-i)
    return None

#existe t-il 3 elements dont leur somme donne T
def three_n_sum(system,T, lists) :
    for i in system :
        if(find_two_numbers_with_sum_T(system,T-i, lists) in system and recherche_dichotomie(lists, i) == None) :
            lists.append(i)
            print(", "+str(i))
            return True
    return False

#existe t-il n elements dont leur somme donne T
def find_n_item(system, n, T) :
    if len(system) < n :
        return False
    
    if n == 1 :
        if recherche_dichotomie(system, T) != None :
            print(str(recherche_dichotomie(system, T))+"+", end="")
        return recherche_dichotomie(system, T)
    i = 0
    for item in system :
        new_system = system[i+1:]
        if(find_n_item(new_system,n-1,T-item)) :
            print(str(item)+"+", end="")
            return True
        i = i + 1
    return False
 
#existe t-il des elements dont leur somme donne T
def find_item_get_sum_target(system, T) :
    for i in range(len(system)) :
        if(find_n_item(system, i, T)) :
            return True
    return False

import algo_tri

arr = [4, 5, 1, 8, 2, 6, 3]
target = 30
listTrie = algo_tri.tri_fusion(arr)
n = 2
lists = []
#print(three_n_sum(listTrie,target, lists))
print(str(target)+" = ", end="")
print(find_item_get_sum_target(listTrie, target))
#print(find_n_elements_with_sum(listTrie,n, target))