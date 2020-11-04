#constantes globales
str_buscado = 'ALLIZZWELL'
vecinos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def encontrar_inicio(inicio,matrix):
    #recorro la matriz para buscar la A
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]==inicio):
                #veo si a partir de esa letra surge el string buscado
                if(encontrar_str(matrix,(i,j),0)):
                    return True
    return False


def encontrar_str(matrix, idx_actual, idx_str):
    
    global str_buscado
    global path
    
    #si el indice del string supera la longitud, se ha encontrado la respuesta 
    if(idx_str == len(str_buscado)):
        return True
    
    else:
        #debemos buscar si los vecinos de esta letra siguen la frase
        try:

            if(idx_actual[0]<0 or idx_actual[1]<0):
                raise NameError('Indice negativo')
                
            if(idx_actual in path):
                raise NameError('Indice repetido')
            
            letra_actual = matrix[idx_actual[0]][idx_actual[1]]

            #comparo la letra de la matriz con la letra de la frase
            if(letra_actual == str_buscado[idx_str]):
                path.append(idx_actual)
                global vecinos
                #itero sobre los vecinos para encontrar la respuesta
                for vecino in vecinos:
                    #el índice del vecino

                    nuevo_idx = (idx_actual[0]+vecino[0],idx_actual[1]+vecino[1])

                    #si la respuesta llegó se retorna True
                    if(encontrar_str(matrix, nuevo_idx, idx_str+1)):
                        return True
                        
                    #de lo contrario, sigue el siguiente vecino.
            #si se probaron todos los vecinos y no retorna True
            #esta letra no es parte del path ganador
                path.pop(-1)

        except Exception as e:
            #si no se puede extraer esta letra, se debe retornar falso
            #el índice se ha salido de la matriz

            return False
        
    return False



T = int(input())
for i in range(T):
    filas,columnas = input().split()
    filas = int(filas)
    matrix = []
    path = []
    for j in range(filas):
        matrix.append(list(input()))
        
    if(encontrar_inicio('A',matrix)):
        print('YES')
    else:
        print('NO')
    
    input()