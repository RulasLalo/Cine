from Cinema import Cinema
from datetime import datetime 

class Viewer:

    def __init__(self):
        fecha=datetime.now()
        if(fecha.month==1):
            print("Estamos a: ",fecha.day," de Enero del ",fecha.year)
        if(fecha.month==2):
            print("Estamos a: ",fecha.day," de Febrero del ",fecha.year)
        if(fecha.month==3):
            print("Estamos a: ",fecha.day," de Marzo del ",fecha.year)
        if(fecha.month==4):
            print("Estamos a: ",fecha.day," de Abril del ",fecha.year)
        if(fecha.month==5):
            print("Estamos a: ",fecha.day," de Mayo del ",fecha.year)
        if(fecha.month==6):
            print("Estamos a: ",fecha.day," de Junio del ",fecha.year)
        if(fecha.month==7):
            print("Estamos a: ",fecha.day," de Julio del ",fecha.year)
        if(fecha.month==8):
            print("Estamos a: ",fecha.day," de Agosto del ",fecha.year)
        if(fecha.month==9):
            print("Estamos a: ",fecha.day," de Septiembre del ",fecha.year)
        if(fecha.month==10):
            print("Estamos a: ",fecha.day," de Octubre del ",fecha.year)
        if(fecha.month==11):
            print("Estamos a: ",fecha.day," de Noviembre del ",fecha.year)
        if(fecha.month==12):
            print("Estamos a: ",fecha.day," de Diciembre del ",fecha.year)

        
    def seleccionarCine(self):
        cine=Cinema()
        cine.verCines()
        

    


