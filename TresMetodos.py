def numPalin():
    
    numero = input("Ingrese numero:")

    X=float(numero)
    Y= X//1 #Redondea el numero
    

    if X-Y == 0: # Si cumple es entero
    
        lista = list(numero)
        listaReverse = []
        i=len(lista)-1

        while i >= 0:
            
            listaReverse.append(lista[i])
            i = i-1
            
        if listaReverse == lista:
            
            print(listaReverse)            
            print(lista)
            return True
        
        else:
        
            print(listaReverse)            
            print(lista)
            return False
    else:
        print("El número no es entero")






def ListaArray():
    vmin=int(input("Digite el mínimo valor: "))
    vmax=int(input("Digite el máximo valor: "))
    lista=[]
    c=0
    x=vmax-vmin
    y=x/99.5
    i=vmin
    if vmax > vmin:
        while i <= vmax:
            lista.append(i)
            i=i+y
            c=c+1
        print(lista)
        print(c)
        return(True)

    else:
        return (False)





    
def LectorTlistaCadenat():
    
    direccion = input("Ingrese la direccion del archivo: ")
    file = open(direccion, 'r')
   
    cadena = input("Ingrese la cadena de caracteres: ")
    listaCadena = cadena.split() #Separa lo ingresado en cada espacio
    
    i = 0
    memoria = []

    
    
    while i <  len(listaCadena): #Compara una posición de listaCadena con todas las demas posiciones
        
        cont = 0
        k = 0
        
        if listaCadena[i] not in memoria: #Si ya se contó una palabra no la vuelve a contar y pasa a la siguiente
            
            while k < len(listaCadena):
                
                if listaCadena[i] == listaCadena[k]: #Guarda en cout la cantidad de veces que aparece una palabra
                    
                    cont = cont + 1
                    
                k = k + 1
                
            memoria.append(listaCadena[i])
            
            print("Palabra: "+ listaCadena[i])
            print("Cantidad: "  + str(cont))
        
        i = i + 1
        
    
    file.close()
