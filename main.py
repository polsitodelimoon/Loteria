#Hacemos las importaciones necesarias
import random as rd
import sqlite3

listanum=[]
listabolts=[]

def boleto():
    #Conectamos con la base de datos
    con=sqlite3.connect('numeroSQL.db')
    #Creamos el cursor
    cursor=con.cursor()
    #Creamos la tabla, en caso de que no exista
    cursor.execute("""CREATE TABLE IF NOT EXISTS numeros (
        num int
        )  
        """)

    jugar='si'

    while jugar=='si':
        #Preguntamos si desea jugar, si es que no saldrá del while y se acabará el programa
        jugar=input('¿Desea sacar un décimo aleatorio?: ')  
        #Añadimos todos los números hasta el 50 para que más tarde elija un número de los que hay en la lista
        for num in range(50):
            listanum.append(num)

        listanum.remove(0)

        if jugar=='si':
   
            print('Seleccionando números...')
            numTot=''

            for num in range(6):        #Hacemos que elija uno de esos 50 números que hay
                num=rd.choice(listanum)
                listanum.remove(num)    #El número que ha salido lo quitamos de la lista para que no vuelva a salir en esa ronda
            
                if num<=9:
                    print('-- Ha salido el','0'+str(num),'--')  #Mostramos en pantalla el número que ha salido
                    num='0'+str(num)    #En caso de ser menor a 9 le añadimos un 0 delante para que sea un número de 2 cifras
            
                else:
                    print('-- Ha salido el',num,'--')   #Para cualquier número mayor que 9 simplemente lo imprimimos en pantalla
            
                num=str(num)
                numTot=numTot+num+' '   #Creamos el número total, que estará compuesto por la elección 6 veces de números del 1 al 50. EJ: (23 45 29 11 50 32)

            instruccion1=f"INSERT INTO numeros VALUES ('{numTot}')"     #Damos la instrucción de que el número que ha salido se escriba en la tabla NUMEROS creada previamente

            cursor.execute(instruccion1)    #Ejecutamos la instrucción

            if numTot in cursor or numTot in listabolts:    #Para hacer que el número no sé repita nunca, hacemos que en caso de que vuelva a salir repita todo hasta que salga diferente
                 boleto()

            else:
                print(numTot)   #Mostramos el número que ha salido en pantalla
                listabolts.append(numTot)   #Añadimos el número a una lista para que el usuario pueda consultar todos los números que han salido por sí quiere ver alguno anterior
            print('\n### Las combinaciones que han salido ya son:',listabolts,'\n')   #Imprimimos todos los números que han salido en esa ronda   


        elif jugar=='no':       #En el caso de que el jugador desee para de jugar, le despedimos y cerramos el archivo
            print('¡Hasta la próxima!')

        else:
            jugar=input('Por favor, ingrese una respuesta válida: ')    #Si el jugador escribe algo erroneo le pedimos que lo vuelva a escribir

    con.commit()
    con.close()



if __name__ == '__main__':  #LLamamos a la función cuando se ejecute el script
    boleto()
