#-------------------------------------------------------------------------------
#    Esqueleto de PSA para el problema de ...
#-------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#-------------------------------------------------------------------------------
#   Definición del problema
#-------------------------------------------------------------------------------

class Problem(SearchProblem):
    """
        Clase que es usada para crear el objeto problema. Los estados son representados con
        una estructura en Python que guarde la información descrita en la formulación del PSA.
    """

    def __init__(self, args):
        """ Constructor de la clase. Inicializa el problema de acuerdo un conjunto de 
            argumentos. 

            arg1: ...
            arg2: ...
        """

        # Construye el estado inicial a partir de los argumentos especificados de acuerdo
        # a lo definido en la formulación del PSA.

        # Llama al constructor de su superclase SearchProblem (start = estado inicial).
        SearchProblem.__init__(self, start)

        # Define el estado meta (opcional).
        self.goal_state = ...

    def actions(self, state):
        """
            Regresa una lista con las acciones legales del agente.

            state: ...
        """

        # Determina las acciones legales según el estado recibido y las precondiciones
        # de cada acción posible, para luego colocarlas en una lista de python

        return ...

    def result(self, state, action):
        """
            Regresa el nuevo estado al ejecutar una acción.

            state: ...
            action: ...
        """

        # Implementa el modelo de transición para determinar el nuevo estado a partir
        # de aplicar la acción al estado especificado

        return ...

    def is_goal(self, state):
        """
            Determina si se ha llegado a un estado meta.

            state: Estado a ser evaluado.
        """

        # efectúa la prueba de meta para determinar si se ha llegado a un 
        # estado deseado

        return ...

    def cost(self, state, action, state2):
        """
            Regresa el costo de ejecutar una acción.

            state: ...
            action: ...
            state2: ...
        """

        # regresa un número que representa el costo de ejecutar action sobre
        # el estado state para producir el estado state2

        return ...

    def heuristic(self, state):
        """
            Regresa valor de la heurística para algoritmos de búsqueda con información.

            state: ...
        """

        # Estima y regresa la distancia desde el estado dado a su meta más cercana.

        return ...

# Despliega la secuencia de estados y acciones obtenidas como resultado
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Estado inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de la accion', action)
                print('¡Meta lograda con costo =', result.cost,'!')
            else:
                print(i,'- Después de la accion', action)

            print('  ', state)
    else:
        print('Falla: No se pudo resolver el problema')

#-------------------------------------------------------------------------------
#   Solución del problema con diferentes métodos
#-------------------------------------------------------------------------------

# posibles expectadores para las búsquedas
my_viewer = None
#my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()        # Abrir en un browser en la liga http://localhost:8000

# Crea PSAs y los resuelve usando una estrategia de búsqueda mediante
# un algoritmo seleccionado.

# resuelve el problema utilizando búsqueda de árbol con el algoritmo de
# primero en anchura
result = breadth_first(Problem(args...), graph_search=False, viewer=my_viewer)
print()
print('>> Búsqueda Primero en Anchura <<')
display(result)

# despliega las estadísticas de búsqueda si no se seleccionó un espectador
if my_viewer != None:
    print('Estadisticas:')
    print(my_viewer.stats)

# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# primero en profundidad
result = depth_first(Problem(args...), graph_search=True, viewer=my_viewer)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)

# despliega las estadísticas de búsqueda si no se seleccionó un espectador
if my_viewer != None:
    print('Estadisticas:')
    print(my_viewer.stats)

# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# A*. Ojo: equiere tener difinida la heurística
result = astar(Problem(args...), graph_search=True, viewer=my_viewer)
print()
print('>> Búsqueda A* <<')
display(result)

# despliega las estadísticas de búsqueda si no se seleccionó un espectador
if my_viewer != None:
    print('Estadisticas:')
    print(my_viewer.stats)

#-------------------------------------------------------------------------------
#   Fin del archivo
#-------------------------------------------------------------------------------