# Evaluacion #3 Metodos Cuantitativos: Simulador de Filas de Supermercado

# Procedemos a importar las siguientes librerias para poder utilizarlas en el programa:
import random
import matplotlib.pyplot as plt

# Definimos la clase Cliente:
class Cliente:
    def __init__(self):
        self.llegada = random.randint(2, 6)
        self.atencion = random.randint(2, 4)

# Definimos la clase Supermercado: 
class Supermercado:
    # Definimos la funcion de inicializacion del programa
    def __init__(self, clientes):

        self.clientes = clientes
        self.tiempos_de_espera = []

    # Definimos la funcion de simulacion:
    def simular(self):
        tiempo_actual = 0
        otro_tiempo = 0

        for cliente in clientes:
            if otro_tiempo + cliente.llegada >= tiempo_actual:
                self.tiempos_de_espera.append(0)
                tiempo_actual += otro_tiempo + cliente.llegada + cliente.atencion - tiempo_actual
            else:
                tiempo_de_espera = tiempo_actual - (otro_tiempo + cliente.llegada)
                self.tiempos_de_espera.append(tiempo_de_espera)
                tiempo_actual += otro_tiempo + cliente.llegada + tiempo_de_espera + cliente.atencion - tiempo_actual
            otro_tiempo += cliente.llegada
        return self.tiempos_de_espera

clientes = []
for x in range(200):
    clientes.append(Cliente())

# Definimos los parametros, y luego el programa a traves de MatPlotLib se encargara de hacer las graficas demostrando el tiempo de espera:
y = Supermercado(clientes).simular()
x = list(range(1, len(y) + 1))
plt.bar(x, y)
plt.show()
