class nodo():
    def __init__(self, dato=None, pos=None):# crea un nodo
        self.izq = None
        self.der = None
        self.dato = dato
        self.alto = 0
        self.pos = pos

def crear_arbolbinario():
    return None
        
def insertar(raiz, dato, pos):# inserta un dato nuevo en el árbol
        if raiz == None:# si no hay nodos en el árbol lo agrega
            raiz = nodo(dato, pos)
        else:# si hay nodos en el árbol lo recorre
            if dato <= raiz.dato: # si el dato ingresado es  menor que el dato guardado va al subárbol izquierdo
                raiz.izq = insertar(raiz.izq, dato, pos)
            else: # si no, procesa el subárbol derecho
                raiz.der = insertar(raiz.der, dato, pos)
        raiz = actualizaraltura(raiz)
        raiz = balancear(raiz)
        return raiz

def reemplazar(raiz):
    aux = nodo()
    if raiz.der!=None:
        raiz.der, aux = reemplazar(raiz.der)
    else:
        aux.dato = raiz.dato
        aux.pos = raiz.pos
        raiz = raiz.izq
    return raiz, aux

def eliminar(raiz, valor, clave):
    dato = None
    if raiz!=None:
        if valor == raiz.dato and clave == raiz.pos:
            dato = raiz.dato
            if raiz.der==None:
                raiz = raiz.izq
            elif raiz.izq==None:
                raiz = raiz.der
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.dato = aux.dato
                raiz.pos = aux.pos
        else:
            if valor<raiz.dato:
                raiz.izq, dato = eliminar(raiz.izq, valor, clave)
            else:
                raiz.der, dato = eliminar(raiz.der, valor, clave)
    raiz = actualizaraltura(raiz)
    raiz = balancear(raiz)
    return raiz, dato
        
def arbolvacio(raiz):
    return raiz == None

def buscarArbol (nodo, dato):
    resultado = None    
    if (nodo != None):
            if dato == (nodo.dato):
                resultado = nodo
            elif dato < (nodo.dato):
                resultado = buscarArbol(nodo.izq, dato)
            else:
                resultado = buscarArbol (nodo.der, dato)
    return resultado

################################## AVL ###########################################
def altura(raiz):
    if raiz==None:
        return -1
    else:
        return raiz.alto
    
def actualizaraltura(raiz):
    if(raiz != None):
        if altura(raiz.izq)>altura(raiz.der):
            raiz.alto = altura(raiz.izq) + 1
        else:
            raiz.alto = altura(raiz.der) + 1
    return raiz

def rotarsimple(raiz, control):
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz # crear_arbolbinario()
    raiz = actualizaraltura(raiz)
    aux = actualizaraltura(aux)
    raiz = aux
    return raiz

def rotardoble(raiz, control):
    if control:
        raiz.izq = rotarsimple(raiz.izq, False)
        raiz = rotarsimple(raiz, True)
    else:
        raiz.der = rotarsimple(raiz.der, True)
        raiz = rotarsimple(raiz, False)
    return raiz

def balancear(raiz):
    if(raiz != None):
        if altura(raiz.izq) - altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotarsimple(raiz, True)
            else:
                raiz = rotardoble(raiz, True)
        elif altura(raiz.der) - altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotarsimple(raiz, False)
            else:
                raiz = rotardoble(raiz, False)
    return raiz

def nivelnodos(raiz,clave):
        cont = 0
        if raiz!=None:
            if raiz.alto == clave:
                cont = 1
            cont += raiz.izq.nivelnodos(clave)
            cont += raiz.der.nivelnodos(clave)
            return cont
        else:
            return 0
############################################################################################
def inorden(raiz):
    if raiz != None:
        inorden(raiz.izq)
        print(raiz.dato)
        inorden(raiz.der)

def preorden(raiz):
    if raiz != None:
        print(raiz.dato, raiz.alto)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(self, raiz):
    if raiz == None:
        return None
    else:
        self.postorden(raiz.left)
        self.postorden(raiz.right)
        print(raiz.dato)

"""
a = crear_arbolbinario()

a = insertar(a, 'a', 1)
a = insertar(a, 'b', 1)
a = insertar(a, 'c', 1)
a = insertar(a, 'd', 1)
a = insertar(a, 'e', 1)
a = insertar(a, 'f', 1)
a = insertar(a, 'g', 1)
a = insertar(a, 'h', 1)
a = insertar(a, 'i', 1)
a = insertar(a, 'j', 1)
a = insertar(a, 'k', 1)
a = insertar(a, 'l', 1)
a = insertar(a, 'm', 1)
a = insertar(a, 'n', 1)
a = insertar(a, 'ñ', 1)

preorden(a)

a, resultado = eliminar(a, 'l', 1) 
a, resultado = eliminar(a, 'j', 1) 
a, resultado = eliminar(a, 'n', 1) 
a, resultado = eliminar(a, 'm', 1) 
a, resultado = eliminar(a, 'i', 1) 
print()
preorden(a)
"""