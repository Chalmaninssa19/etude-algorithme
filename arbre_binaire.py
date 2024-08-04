from graphviz import Digraph
from IPython.display import Image

class Node :
    def __init__(self,key) :
        self.key = key
        self.right = None
        self.left = None
    
    # Retourne la valeur de l'arbre
    def getKey(self) :
        return self.key
    
    # Retourne le noeud a gauche
    def getLeft(self) :
        return self.left
    
    # Retourne le noeud a droite
    def getRight(self) :
        return self.right
            
# Afficher l'arbre
def afficher(arbre) :
    if arbre != None :
        return (arbre.getKey(), afficher(arbre.getLeft()), afficher(arbre.getRight()))

# Creer l'arbre
def buildTree(elements) :
    root = Node(elements[0])
    for item in elements :
        insertNode(root, item)
    return root

# Inserer un noeud
def insertNode(node, key) :
    if node == None :
        return Node(key)
    if key < node.key :
        node.left = insertNode(node.left, key)
    if key > node.key : 
        node.right = insertNode(node.right, key)
    return node

# Trouver le minimum par iteration
def findMinimum(arbre) :
    while arbre.getLeft() :
        arbre = arbre.getLeft()
    return arbre

# Trouver minimum par recursivite
def minimum(arbre) : 
    if arbre.getLeft() == None :
        return arbre
    else :
        return minimum(arbre.getLeft())

# Trouver maximum par iteration
def findMaximum(arbre) :
    while arbre.getRight() :
        arbre = arbre.getRight()
    return arbre

# Trouver maximum par recursivite
def maximum(arbre) :
    if arbre.getRight() == None :
        return arbre
    else :
        return maximum(arbre.getRight())

# est ce la valeur key est dans l'arbre
def searchNode(key, tree) :
    if tree == None :
        return False
    elif key == tree.getKey() :
        return True
    elif key < tree.getKey() :
        return search(key, tree.getLeft())
    elif key > tree.getKey() :
        return search(key, tree.getRight())

# Retourne le noeud rechercher si il existe dans l'arbre binaire
def search_node(node, key):
    if node is None or node.getKey() == key:
        return node
    elif node.getKey() < key:
        return search_node(node.getRight(), key)
    else:
        return search_node(node.getLeft(), key)

# Ajouter un element dans l'arbre binaire
def addNode(item, tree) :
    if tree == None :
        return Node(item)
    if item < tree.getKey() :
            tree.left = add(item,tree.getLeft())
    else :
        tree.right = add(item,tree.getRight())

    return tree

# Trier un arbre binaire (Retourner un nouveau tableau trier)
def trierTree(tree) :
    if tree != None :
        return trierTree(tree.getLeft()) + [tree.getKey()] + trierTree(tree.getRight())
    else :
        return []

# Supprimer un element dans l'arbre
def deleteNode(key, tree) :
    if tree == None :
        return tree
    #Rechercher dans l'arbre le noeud a supprimer s'il existe
    if key < tree.getKey() :
        tree.left = deleteNode(key,tree.getLeft())
    elif key > tree.getKey() :
            tree.right = deleteNode(key,tree.getRight())
    else : #Si le noeud est trouve
        #Cas le noeud trouve n'a pas d'enfant
        if not tree.getLeft() and not tree.getRight() :
            tree = None
        #Cas ou le noeud n'a pas d'enfant gauche
        elif not tree.getLeft() :
                tree = tree.getRight()
        #Cas ou le noeud n'a pas d'enfant droit
        elif not tree.getRight() :
                tree = tree.getRight()
        #Cas ou le noeud a deux enfants
        else :
            temp = findMinimum(tree.getRight())
            tree.key = temp.key
            tree.right = deleteNode(key, tree.getRight())
    return tree

#Dessiner un arbre binaire
def draw_tree(root):
    dot = Digraph()
    if not root:
        return dot
    stack = [(root, None)]
    while stack:
        node, parent = stack.pop()
        dot.node(str(node.getKey()))
        if parent:
            dot.edge(str(parent.getKey()), str(node.getKey()))
        if node.getRight():
            stack.append((node.getRight(), node))
        if node.getLeft():
            stack.append((node.getLeft(), node))

    return dot
    
def draw_tree_with_search(root, key):
    dot = Digraph()
    if not root:
        return dot
    stack = [(root, None)]
    while stack:
        node, parent = stack.pop()
        dot.node(str(node.getKey()))
        if parent:
            dot.edge(str(parent.getKey()), str(node.getKey()))
        if node.getRight():
            stack.append((node.getRight(), node))
        if node.getLeft():
            stack.append((node.getLeft(), node))
    
    # Utilisation de la méthode de recherche pour trouver le nœud et le colorier
    node = search_node(root, key)
    if node:
        dot.node(str(node.getKey()), style='filled', fillcolor='red', color='black')

    return dot

elements = [24, 76, 8, 7, 84, 23, 13, 3, 37]
tree = buildTree(elements)
#print(trierTree(tree))
# Dessinez l'arbre binaire
dot = draw_tree(tree)
deleteNode(13, tree)
insertNode(tree, 45)
dot = draw_tree(tree)
#dot = draw_tree_with_search(tree,22)
dot.render('tree', format='png', view=True)

# Affichez l'image de l'arbre binaire
Image(filename='tree.png')