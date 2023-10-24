class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

def floyd_tortoise(cabeza):
    if cabeza is None:
        return False

    tortuga = cabeza
    liebre = cabeza

    while liebre is not None and liebre.siguiente is not None:
        tortuga = tortuga.siguiente
        liebre = liebre.siguiente.siguiente

        if tortuga == liebre:
            return True

    return False

def principal():
    # Lista con un ciclo
    cabeza = Nodo(1)
    cabeza.siguiente = Nodo(2)
    cabeza.siguiente.siguiente = Nodo(3)
    cabeza.siguiente.siguiente.siguiente = Nodo(4)
    cabeza.siguiente.siguiente.siguiente.siguiente = cabeza

    # Ejecutamos el algoritmo
    tiene_ciclo = floyd_tortoise(cabeza)

    # Imprimimos el resultado
    print(tiene_ciclo)

if __name__ == "__main__":
    principal()