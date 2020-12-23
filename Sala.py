from Movie import Movie
import sqlite3
import random

class Sala:
    def __init__(self):
        self.connection=sqlite3.connect('/home/lalo/Documentos/Proyectos/Cine/Cines') #Connect to DB

    def verSala(self, movieTheater):
        #print(type(movieTheater))
        connect=self.connection
        movieTheater= '"'+movieTheater+'"'
        query=connect.execute(f'select Sala1, Sala2, Sala3, Sala4, Sala5 from Cinemas where Name={movieTheater}')#Tuple
        
        print("Selecciona la sala que mas sea de tu agrado para ver la disponibilidad de asientos.")
        print()

        for i in list(query): #Las salas están en una tupla, dentro de una lista
            row=list(i) #Guarda en una lista las salas del cine seleccionado. tupla -> lista
        print('{:<10}{}'.format("Sala", "Asientos"))
        count=0
        none=0
        for j in range(len(row)):
            count+=1
            if row[j]==None:
                none+=1
                count=count-none
                continue
            print('{:<10}{}'.format(count,row[j]))
            #row=row.append(row[j])
        self.seleccionarSala(query, count, row)
        """movie=Movie()
        movie.showMovies()"""

    def seleccionarSala(self, query, count, row):
        opt=int(input("Seleccionar sala: "))
        while (opt >count or opt<=0): #len(query)
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

            opt=int(input("Seleccionar sala: "))
        new_row=[]
        for i in range(len(row)):
            if row[i]==None:
                continue
            new_row.append(row[i]) #Se crea una lista sin datos NONE
        print(f"Escogiste la sala {opt}, la cual contiene {new_row[opt-1]} asientos.")
        
        self.seleccionarAsiento(opt, new_row[opt-1])

    def seleccionarAsiento(self, opt, new_row):
        print(f"Sala {opt}, seleccione los asientos (Máximo 8): ")

        valorFila=65
        count=1
        asiento=''
        asientoLista=[]
        for i in range(1,new_row+1):
            asiento=chr(valorFila)+str(count)
            print(asiento,end=" ")
            asientoLista.append(asiento)
            count+=1
            if i%9==0:
                valorFila=valorFila+1
                count=1
                print()
        #print(asientoLista)
        
        contAsiento=1
        print()
        opt=input("Seleccione asiento: ").upper()
        opt_=[]
        #opt_.append(opt)
    
        while contAsiento<9 or opt in asientoLista:
            if opt not in asientoLista:
                print("Selecciona un asiento correcto.")
                opt=input("Seleccione asiento: ").upper()
            else:
                opt_.append(opt)
                compra=input("¿Desea seleccionar otro asiento?, S(si) N(no): ").upper()
                if compra=="S":
                    opt=input("Seleccione asiento: ").upper()
                    opt_.append(opt)
                elif compra=="N":
                    break
                
            #opt=input("Seleccione asiento: ")
            contAsiento+=1
        print()
        print("Tus asientos seleccionados son:")
        for i in range(len(asientoLista)):
            for j in opt_:
                if j==asientoLista[i]:
                    asientoLista[i]="X "
            if i%9==0:
                print()
            print(asientoLista[i],end=" ")
            
        print()