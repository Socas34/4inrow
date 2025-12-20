import json
def menu()->None:
    """
    OBJ: Printea un menu para el usuario elegir que ver
    """
    print("=== Juego de 4 en raya ===\n" \
    "Seleccione una opcion:\n" \
    "1.Iniciar una nueva partida\n" \
    "2.Estadisticas\n" \
    "3.Salir"
    )

def validar_entrada_rango(a:int,b:int,msj:str)->int:
    """
    OBJ: Validar un entero en un rango de intervalo cerrado
    PRE: None
    """
    condicion = True
    while condicion:
        try:
            entero = int(input(msj))
            if a>entero>b:
                raise Exception
            condicion = False
        except:
            print(msj)
    return entero
def crear_tablero()->list:
    """
    OBJ: Almacenar un tablero vacio de 6x7 (Filas x Columnas)
    PRE: None
    """
    tablero = []
    for i in range(6):
        fila = []
        for j in range(7):
            fila.append("[  ]")
        tablero.append(fila)
    return tablero
def insertar_ficha(tablero:list,color:str)->tuple:    
    """
    OBJ: Insertar una ficha de un color determinado en una columna determinada
    PRE: Color ("R","B")
    """
    Rojo = ("[""\033[41m"+"  "+"\033[0m""]")
    Azul = ("[""\033[44m"+"  "+"\033[0m""]")
    Vacio = "[  ]"
    if color == "R":
        i =len(tablero)-1
        x = validar_entrada_rango(1,7,"Jugador Rojo\nEn que columna desea introducir la ficha?: ")
        while i>=0:
            if tablero[i][x-1]==Vacio:
                tablero[i][x-1] = Rojo
                return i,(x-1)
            else:
                i-=1       
    elif color == "B":
        i =len(tablero)-1
        x = validar_entrada_rango(1,7,"Jugador Azul\nEn que columna desea introducir la ficha?: ")
        while i>=0:
            if tablero[i][x-1] == Vacio and i>=0:
                tablero[i][x-1] = Azul
                return i,(x-1)
            else:
                i-=1
        #En el programa principal comparar tableros, si no ha cambiado nada repetir la orden
def imprimir_tablero(tablero:list)->None:
    """
    OBJ: Imprimir el tablero de manera que se represente en forma de matriz
    """
    print(" 1    2   3   4   5   6   7 ")
    print("----------------------------")
    for fila in tablero:
        string = ""
        for elemento in fila:
            string+= elemento
        print(string)
    print("----------------------------")
def combrobar_tablerolleno(tablero:list)->bool:
    Vacio = "[  ]"
    for sublista in tablero:
        if Vacio in sublista:
            return False
    return True
def combrobar_ganador(tablero:list,x:int,y:int)->bool:
    """
    OBJ: Comrpobar si la ultima ficha insertada hace 4 en raya
    PRE: Dados los parametros devueltos de la funcion insertar ficha
    """
    mov = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for movimiento in mov:
        i = 1
        condicion = True
        while condicion:
            x2,y2 = x+ i*movimiento[0],y+ i*movimiento[1]
            if 0<=x2<=5 and 0<=y2<=6:
                if tablero[x][y] != tablero[x2][y2]:
                    condicion = False
                else:
                    i+=1
            else:
                condicion = False
        if i == 4:
            return True,tablero[x][y]
    return False
def crear_estadisticas_jugador(estadisticas:dict,nombre:str):
    estadisticas[nombre] = {"Ganados":0,"Empatados":0,"Perdidos":0,"Puntuacion":0}
def guardar_estadisticas_ganado(estadisticas:dict,rondas:float,nombre:str)->None:
    # Usaremos dump |Python->Json|, load |Json->Python|
    # estadisticas = {nombre:{ganados:0,empatados:0,perdidos:0,puntuacion:0}nombre2:{.....}}
    puntuacion = 3500-500*rondas
    if puntuacion <500: puntuacion = 500
    estadisticas[nombre]["Ganado"]+=1
    estadisticas[nombre]["Puntuacion"] += puntuacion
def guardar_estadisticas_perdido(estadisticas:dict,nombre:str)->None:
    # estadisticas = {nombre:{ganados:0,empatados:0,perdidos:0,puntuacion:0}nombre2:{.....}}
    estadisticas[nombre]["Perdido"]+=1
def guardar_estadisticas_empatado(estadisticas:dict,nombre:str)->None:
    # estadisticas = {nombre:{ganados:0,empatados:0,perdidos:0,puntuacion:0}nombre2:{.....}}
    estadisticas[nombre]["Empatado"]+=1
    estadisticas[nombre]["Puntuacion"] +=250
def almacenar_datos (datos:dict)->None:
    with open("estadisticas.json","w") as archivo:
        json.dump(datos,archivo,indent=4,ensure_ascii=False)
def cargar_datos()->dict:
    with open("estadisticas.json","r") as archivo:
        datos_cargados = json.load(archivo)
    return datos_cargados
#Caracteristicas de algoritmo
def fork_supuesto (tablero:list,x:int,y:int)->bool:
    """
    OBJ: Comrpobar si la ultima ficha insertada hace 2 3 en raya
    PRE: Dados los parametros devueltos de la funcion insertar ficha
    """
    mov = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    contador = 0
    for movimiento in mov:
        i = 1
        condicion = True
        while condicion:
            x2,y2 = x+ i*movimiento[0],y+ i*movimiento[1]
            if 0<=x2<=5 and 0<=y2<=6:
                if tablero[x][y] != tablero[x2][y2]:
                    condicion = False
                else:
                    i+=1
            else:
                condicion = False
        if i == 4:
            contador +=1
    if contador == 2:
        return True, tablero[x][y]
    return False
#La posicion central deberia de ir en la funcion principal del algortimo
def conectar3(tablero:list,x:int,y:int)->bool:
    """
    OBJ: Comrpobar si la ultima ficha insertada hace 3 en raya
    PRE: Dados los parametros devueltos de la funcion insertar ficha
    """
    mov = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for movimiento in mov:
        i = 1
        condicion = True
        while condicion:
            x2,y2 = x+ i*movimiento[0],y+ i*movimiento[1]
            if 0<=x2<=5 and 0<=y2<=6:
                if tablero[x][y] != tablero[x2][y2]:
                    condicion = False
                else:
                    i+=1
            else:
                condicion = False
        if i == 3:
            return True,tablero[x][y]
    return False
def conectar2(tablero:list,x:int,y:int)->bool:
    """
    OBJ: Comrpobar si la ultima ficha insertada hace 2 en raya
    PRE: Dados los parametros devueltos de la funcion insertar ficha
    """
    mov = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for movimiento in mov:
        i = 1
        condicion = True
        while condicion:
            x2,y2 = x+ i*movimiento[0],y+ i*movimiento[1]
            if 0<=x2<=5 and 0<=y2<=6:
                if tablero[x][y] != tablero[x2][y2]:
                    condicion = False
                else:
                    i+=1
            else:
                condicion = False
        if i == 2:
            return True,tablero[x][y]
    return False

def algoritmo_maquina(tablero:list)->tuple:
    mapa_calor= 