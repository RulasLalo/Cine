from Sala import Sala
from Movie import Movie
import sqlite3 #Library that allow us make a connection between sqlite and python
import random

class Cinema:

    def __init__(self):

        self.connection=sqlite3.connect('/home/lalo/Documentos/Proyectos/Cine/Cines') #Connect to DB
    
    def verCines(self):

        try:
            connect=self.connection
            filas=connect.execute("select * from Cinemas") #Variable to read the rows of the thable
            query=list(filas) #The whole query(tuple) as a list. Every element is a tuple.
            print("Lista de cines")
            count=0
            for i in query:
                row=list(i)
                count=count+1
                print(count, row[0]) 

            print()
            self.selectMovieTheater(query, count)

        except sqlite3.OperationalError:
            print("VERIFIQUE QUE EXISTA LA TABLA O QUE SU CONEXIÓN A LA BD SEA CORRECTA.")

    def selectMovieTheater(self, query, count):
        try:
            opt=0
            opt=int(input("Seleccione el cine de su agrado: "))
    
            while (opt >count or opt<=0 or False): #len(query)

                rand=random.randint(1,4)
                if(rand==1):
                    print("Escoge la opción correcta")
                    print()
                if(rand==2):
                    print("Te equivocaste. Vuelve a intentar, por favor.")
                    print()
                if(rand==3):
                    print("Ups!!!, no tenemos ese cine.")
                    print()
                if(rand==4):
                    print("Parece que ocurrió un error.")
                    print()
                opt=int(input("Seleccione el cine de su agrado: "))
                
        except ValueError:
            print("Ingresa un entero")

        if(opt<=count):
                movieTheater=list(query[opt-1])
                #print(movieTheater)
                print("Bienvenido a: ",movieTheater[0])
                print()

            
       
        movie=Movie()
        movie.showMovies
        sala=Sala()
        sala.verSala(movieTheater[0]) 
       