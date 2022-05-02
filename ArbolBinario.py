""" 
    Script para implematar una busqueda Binaria entre dos nodos 
    dado pos puntos Cualquiera y sacar su eficiencia y costo,

    Nota: integracion no esta completa.
"""


# Estructura de un nodo de árbol binario
class Node:
    def __init__(self, kilometer, gas_price):
        self.kilometer = kilometer
        self.gas_price = gas_price
        self.izquierda = None
        self.derecha = None


class Vehicle:
    def __init__(self, name, number_plate, fuel_efficiency, fuel_tank_size):
        self.name = name
        self.passengers = 4
        self.number_plate = number_plate
        self.vehicle_type = "car"
        self.fuel_efficiency = fuel_efficiency
        self.fuel_tank_size = fuel_tank_size


def getNode(kilometer, gas_price):
    """
    Función auxiliar que asigna un nuevo nodo con el
    datos dados y NULL punteros izquierda y derecha.

    """
    return Node(kilometer, gas_price)


def buscar(nodo, busqueda):

    if nodo is None:
        return None
    if nodo.kilometer == busqueda:
        return nodo
    if busqueda < nodo.kilometer:
        return buscar(nodo.izquierda, busqueda)
    else:
        return buscar(nodo.derecha, busqueda)


def getPath(nodo, rarr, x):
    """
    Función para verificar si hay una ruta desde nodo
    al nodo dado. también puebla
    'arr' con la ruta dada.

    """

    # Si nodo es null no hay camino
    if not nodo:
        return False

    # Agregcar nodo a la ruta
    rarr.append(nodo.kilometer)

    # si es el nodo requerido
    # devuelve verdadero
    if nodo.kilometer == x:
        return True

    # Verifica si el nodo requerido se encuentra
    # en el subárbol izquierdo o en el subárbol derecho de
    # el nodo actual
    if getPath(nodo.izquierda, rarr, x) or getPath(nodo.derecha, rarr, x):
        return True

    # nodo requerido tampoco se encuentra en el
    # subárbol izquierdo o derecho del nodo actual
    # Por lo tanto, elimina el valor del nodo actual de
    # 'arr' y luego devuelve false
    rarr.pop()
    return False


def iprimirRutaEntreDosNodos(nodo, car, a, b):
    """
    Función para imprimir la ruta entre
    dos nodos cualquiera en un árbol binario

    """

    # Crea un arreglo para almacenar la ruta A
    ruta1 = []

    # Crea un arreglo para almacenar la ruta B
    ruta2 = []

    # Obtiene la ruta A
    getPath(nodo, ruta1, a)
    # Obtiene la ruta B
    getPath(nodo, ruta2, b)

    # Obtener punto de intersección
    i, j = 0, 0
    intersection = -1
    while(i != len(ruta1) or j != len(ruta2)):

        # Siga avanzando hasta que no encuentre
        # ninguna intersección.
        if (i == j and ruta1[i] == ruta2[j]):
            i += 1
            j += 1
        else:
            intersection = j - 1
            break
    # Ruta a recorrer
    ruta = []

    for i in range(len(ruta1) - 1, intersection - 1, -1):
        ruta.append(ruta1[i])
        # print("{} ".format(ruta1[i]), end="")
    for j in range(intersection + 1, len(ruta2)):
        ruta.append(ruta2[j])
        # print("{} ".format(ruta2[j]), end="")

    # imprimir ruta
    print("\n Ruta: ", format(ruta))

    # eficiencia del Vehiculo
    eficiencia = car.fuel_efficiency * (car.fuel_tank_size / 100)
    print("\n Eficiencia del Vehiculo: {} km/combustible". format(eficiencia))

    # imprimir Kilometraje
    km = 0
    for n in ruta:
        km += n

    print("\n Kilometraje del Recorrido: {} Km." .format(km))

    # imprimir costo
    costo = 0
    for i in ruta:
        costo += i * buscar(nodo, i).gas_price

    print("\n Costo Total: {} $ ".format(round(costo, 2)))


# Main
if __name__ == '__main__':

    # Vehiculo Prueba
    car = Vehicle("Car", "ABC123", 5, 50)

    # Dado el siguiente árbol binario en KM y precio de combustible
    # Tomado del Test_dev
    nodo = getNode(60, 1.11)
    nodo.izquierda = getNode(45, 1.12)
    nodo.izquierda.izquierda = getNode(21, 1.11)
    nodo.izquierda.izquierda.izquierda = getNode(0, 1.10)
    nodo.derecha = getNode(95, 1.13)
    nodo.derecha.izquierda = getNode(72, 1.12)
    nodo.derecha.izquierda.izquierda = getNode(65, 1.09)
    nodo.derecha.izquierda.derecha = getNode(80, 1.12)
    nodo.derecha.derecha = getNode(120, 1.14)
    # a = 65
    # b = 80
    # Calculamos la ruta entre los nodos A y B
    a = int(input("Ingresa punto A: "))
    b = int(input("Ingresa punto B: "))
    iprimirRutaEntreDosNodos(nodo, car, a, b)
