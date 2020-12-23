from Viewer import Viewer

class Main:
    def __init__(self):
        print("Bienvenido")
        cliente=Viewer() #Objeto de la clase Viewer
        cliente.seleccionarCine() #Mandamos a llamar a la clase seleccionarCine

obj=Main() #Objeto de la clase Main que manda a llamar al método Init
