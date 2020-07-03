##Se consiguen todos los números primos hasta el límite máximo de 32000, raíz cuadrada de 1 000 000 000
#Aprobado
from math import sqrt

primos = [2]
for i in range(3,32000,2):
    limite = int(sqrt(i)+1)
    es_primo = True
    for primo in primos:
        if(primo>limite):
            break
        if(i % primo == 0):
            es_primo = False
            break
    if(es_primo):
        primos.append(i)

#Se realiza la prueba con los números del rango
t = int(input())

for i in range(t):
    #criba = []
    m , n = map(int , input().split())
    matriz_primos = [True]*(n-m+1)
    if(m==1):
        matriz_primos[0]=False
    limite = int(sqrt(n)+1)
    
    for primo in primos:
        if(primo>limite):
            break
        #encuentro un múltiplo del número primo para empezar a recorrer el arreglo
        inicio = m - (m%primo)
        
        if(inicio==0):
            inicio+= primo
        
        #si el inicio no se encuentra en el rango
        if(inicio < m or inicio == primo):
            inicio += primo
            
        bloque_falso = [False]*len(matriz_primos[inicio-m:n+1:primo])
        matriz_primos[inicio-m:n+1:primo] = bloque_falso
    for i in range(len(matriz_primos)):
        if(matriz_primos[i]):
            print(i+m)
    print()
    
    