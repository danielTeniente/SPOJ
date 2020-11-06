#global
acciones = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]

def salto_caballo(idx_actual, path_actual):    
    global acciones
    global chess_board
    global mejor_path
    
    
    #agrego el índice actual al path
    path_actual.append(idx_actual)
    
    #bandera que controla que haya una jugada siguiente
    bandera_siguiente = False
    for accion in acciones:
        new_idx = (idx_actual[0]+accion[0],idx_actual[1]+accion[1])
        #el nuevo índice no fue usado con anterioridad
        #el nuevo índice es parte del tablero
        if((new_idx not in path_actual) and 
           chess_board[new_idx[0]][new_idx[1]]!= 0):
            bandera_siguiente = True
            salto_caballo(new_idx, path_actual)
            #si ya ha retornado, entonces se debe deshacer la jugada
            path_actual.pop(-1)
            
    #si no hubo un movimiento siguiente, el path se terminó
    if(not bandera_siguiente):
        if(len(path_actual)>len(mejor_path)):
            mejor_path = path_actual.copy()
            
    


caso_prueba = input().split()
filas = int(caso_prueba[0])
chess_board = []

row = [0]*10

for _ in range(10):
    chess_board.append(row.copy())

case = 0

while(filas !=0 ):
    case+=1
    
    #con esto sabré cuántos cuadros hay disponibles
    cuadros_disponibles = 0
    
    fila_actual = 0
    
    #modifica el chessboard para establecer los cuadros disponibles
    for i in range(1,filas*2,2):

        inicio = int(caso_prueba[i])
        cuadros = int(caso_prueba[i+1])
        cuadros_disponibles += cuadros
        chess_board[fila_actual][inicio:inicio+cuadros] = [1] * len(chess_board[0][inicio:inicio+cuadros])       
        fila_actual+=1
        
    mejor_path = []
    salto_caballo((0,0),[])
    cuadros_faltantes = cuadros_disponibles-len(mejor_path)
    if(cuadros_faltantes==1):
        print('Case {}, {} square can not be reached.'.format(case,cuadros_faltantes))
    else:
        print('Case {}, {} squares can not be reached.'.format(case,cuadros_faltantes))
    for i in range(10):
        chess_board[i][:] = [0]*len(chess_board[0][:])
        
    caso_prueba = input().split()
    filas = int(caso_prueba[0])