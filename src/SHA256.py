class Graph():
    # Propiedades inmutables para la CLI.
    OK = '\033[92m'         # GREEN
    WARNING = '\033[93m'    # YELLOW
    FAIL = '\033[91m'       # RED
    RESET = '\033[0m'       # RESET COLOR

    # Constructor de clase.
    def __init__(self, noVertices):
        self.noVertices = noVertices
        self.incidenceMatrix = [[0 for columna in range(noVertices)]
                                for fila in range(noVertices)]
