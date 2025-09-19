#---------------------------------------------------------------------------------------------------------------
#    PSA para el problema de las tres jarras
#---------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#---------------------------------------------------------------------------------------------------------------
#   Definición del problema
#---------------------------------------------------------------------------------------------------------------

class ProblemaDeLas3Jarras(SearchProblem):
    """ 
        Clase que es usada para definir el problema de las 3 jarras. Los estados son representados 
        por tuplas (a, b, c), donde cada elemento representa la cantidad de líquido en cada jarra.
    """

    def __init__(self, A, B, C):
        """ Constructor de la clase. Inicializa el problema de acuerdo a las capacidades de cada 
            jarra.
            Las capacidades deben ser valores enteros tales que A > B > C and A es un número par.
       
            A: La capacidad de la primera jarra.
            B: La capacidad de la segunda jarra.
            C: La capacidad de la tercera jarra.
        """
        
        self.capacities = (A, B, C) # Capacidades
        initial_state = (A, 0, 0)   # Estado inicial - La primera jarra llena y las otras vacías.
        
        # Llama al constructor de su superclase SearchProblem (se le especifica el estado inicial).
        SearchProblem.__init__(self, initial_state)

        # Define el estado meta.
        self.goal_state = (A/2, A/2, 0)

    def actions(self, state):
        """ 
            Este método regresa una lista con las acciones posibles que pueden ser ejecutadas de 
            acuerdo con el estado especificado.
            
            state: El estado a ser evaluado.
        """
        actions = []
        # El contenido de la jarra 1 está en la posición 0 del estado y, respectivamente, 
        # el contenido de las jarras 2 y 3 están en las posiciones 1 y 2.
        if state[0] > 0 and state[1] < self.capacities[1]:
            actions.append(('a->b', min([state[0], self.capacities[1] - state[1]])))
        
        if state[0] > 0 and state[2] < self.capacities[2]:
            actions.append(('a->c', min([state[0], self.capacities[2] - state[2]])))

        if state[1] > 0 and state[0] < self.capacities[0]:
            actions.append(('b->a', min([state[1], self.capacities[0] - state[0]])))

        if state[1] > 0 and state[2] < self.capacities[2]:
            actions.append(('b->c', min([state[1], self.capacities[2] - state[2]])))

        if state[2] > 0 and state[0] < self.capacities[0]:
            actions.append(('c->a', min([state[2], self.capacities[0] - state[0]])))

        if state[2] > 0 and state[1] < self.capacities[1]:
            actions.append(('c->b', min([state[2], self.capacities[1] - state[1]])))

        return actions

    def result(self, state, action):
        """ 
            Este método regresa el nuevo estado obtenido despues de ejecutar la acción.

            state: El estado a ser modificado.
            action: La acción a ser ejecutada sobre el estado.
        """
        new_state = (0,0,0)
       
        if action[0] == 'a->b':
            new_state = (state[0]-action[1], state[1]+action[1], state[2])

        elif action[0] == 'a->c':
            new_state = (state[0]-action[1], state[1], state[2]+action[1])
        
        elif action[0] == 'b->a':
            new_state = (state[0]+action[1], state[1]-action[1], state[2])

        elif action[0] == 'b->c':
            new_state = (state[0], state[1]-action[1], state[2]+action[1])

        elif action[0] == 'c->a':
            new_state = (state[0]+action[1], state[1], state[2]-action[1])

        elif action[0] == 'c->b':
            new_state = (state[0], state[1]+action[1], state[2]-action[1])

        return new_state

    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        found_goal = state == self.goal_state

        return found_goal
        
    def cost(self, state, action, state2):
        """ 
            Este método recibe dos estados y una acción, y regresa el costo de 
            aplicar la acción del primer estado al segundo.

            state: El primer estado.
            action: La acción usada para generar el segundo estado.
            state2: El segundo estado obtenido después de aplicar la acción.
        """
        return 1
        
    def heuristic(self, state):
        """ 
            Este método regresa un estimado de la distancia desde el estado a la meta.

            state: El estado a ser evaluado.
        """
        A = self.capacities[0]
        a, b, c = state

        return abs(A/2 - a) + abs(A/2 - b) + c

# Despliega los resultados
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Configuración inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de trasvase', action)
                print('¡Meta lograda con costo =', result.cost,'!')
            else:
                print(i,'- Después de trasvase', action)

            print('  ', state)
    else:
        print('Mala configuración del problema')

#---------------------------------------------------------------------------------------------------------------
#   Programa
#---------------------------------------------------------------------------------------------------------------

my_viewer = None
#my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()        # Abrir en un browser en la liga http://localhost:8000

# Crea un PSA y lo resuelve con la búsqueda primero en anchura
result = breadth_first(ProblemaDeLas3Jarras(8, 5, 3), graph_search=True, viewer=my_viewer)

#print('Stats:')
#print(my_viewer.stats)

print()
print('>> Búsqueda Primero en Anchura <<')
display(result)

result = depth_first(ProblemaDeLas3Jarras(8, 5, 3), graph_search=True)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)

result = astar(ProblemaDeLas3Jarras(8, 5, 3), graph_search=True)
print()
print('>> Búsqueda A* <<')
display(result)


#---------------------------------------------------------------------------------------------------------------
#   Fin del archivo
#---------------------------------------------------------------------------------------------------------------