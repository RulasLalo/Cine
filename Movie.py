import sqlite3
import random

class Movie:
    def __init__(self):
        self.connection=sqlite3.connect("Cines")
    
    def showMovies(self):
        
        try:
            moviesTable=self.connection
            filas=moviesTable.execute("select * from peliculas")
            
            query=list(filas)
            count=0
            print("Películas disponibles en este cine: ")
            for i in query:
                row=list(i)
                count+=1
                print(count,end=". ")
                for j in range(len(row)):
                    print(row[j],end="    ")
                print()
                print()
            self.selectMovies(count, query)
            
        except sqlite3.OperationalError:
            print("VERIFIQUE QUE EXISTA LA TABLA O QUE SU CONEXIÓN A LA BD SEA CORRECTA.")

    def selectMovies(self, count, query):
        opt=int(input("Seleccione la película de su agrado: "))

        while (opt >count or opt<=0):
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
            print()
            opt=int(input("Seleccione la película de su agrado: "))
            

        movie=query[opt-1] #Se guarda la fila correspondiente a la película seleccionada
        print(f"Seleccionaste la película: {movie[0]}")
        print()
        
        if movie[2]=='C' or movie[2]=='D':
            print("ADVERTENCIA, esta película es solamente apta para mayores de 18 años. Se "
                    "pedirá identidicación al momento del ingreso.")
        