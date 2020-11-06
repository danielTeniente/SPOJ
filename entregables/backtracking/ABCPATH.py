vecinos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
 
#global
str_buscado = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
 
def encontrar_inicio(inicio,matrix):
    #recorro la matriz para buscar la A
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]==inicio):
                #veo si a partir de esa letra surge el string buscado
                encontrar_str(matrix,(i,j),0,1)
 
def encontrar_str(matrix,idx_actual,idx_str,counter):
    global str_buscado
    global vecinos
    global max_count
    global idx_recorridos
    

    
    x_max = len(matrix[0])
    y_max = len(matrix)
    
    if(max_count!=len(str_buscado) and idx_actual not in idx_recorridos):
        idx_recorridos.append(idx_actual)
        #Llegamos al path más largo
        if(matrix[idx_actual[0]][idx_actual[1]] == str_buscado[-1]):
            max_count = counter
    
        else:

            #bandera de fin de path
            fin_path = True
    
            #el indice debe estar dentro del rango
            for vecino in vecinos:
                new_idx = (idx_actual[0]+vecino[0],idx_actual[1]+vecino[1]) 
                if(new_idx[0]>=0 and new_idx[1]>=0 and
                new_idx[0]<y_max and new_idx[1]<x_max):
                    next_char = matrix[new_idx[0]][new_idx[1]]
                    #si el nuevo char es el que estoy buscando
                    if(next_char == str_buscado[idx_str+1]):
                        fin_path=False
                        encontrar_str(matrix,new_idx,idx_str+1,counter+1)
    
    
            if(fin_path):
                if(counter>max_count):
                    max_count = counter
 
 
 
 
 
 
 
 
 
entrada = input().split()
filas = int(entrada[0])
col = int(entrada[1])
case = 0
 
while(filas !=0 and col !=0):
    case +=1
    matrix = []
    max_count = 0
    idx_recorridos = []


    for _ in range(filas):
        matrix.append(list(input()))
 
    encontrar_inicio('A',matrix)
 
    print('Case {}: {}'.format(case,max_count))
 
 
    entrada = input().split()
    filas = int(entrada[0])
    col = int(entrada[1])   