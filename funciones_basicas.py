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
def insertar_ficha_segunx(tablero:list,color:str,x:int)->tuple:    
    """
    OBJ: Insertar una ficha de un color determinado en una columna determinada
    PRE: Color ("R","B")
    """
    Rojo = ("[""\033[41m"+"  "+"\033[0m""]")
    Azul = ("[""\033[44m"+"  "+"\033[0m""]")
    Vacio = "[  ]"
    if color == "R":
        i =len(tablero)-1
        while i>=0:
            if tablero[i][x-1]==Vacio:
                tablero[i][x-1] = Rojo
                return i,(x-1)
            else:
                i-=1     
    elif color == "B":
        i =len(tablero)-1
        while i>=0:
            if tablero[i][x-1] == Vacio and i>=0:
                tablero[i][x-1] = Azul
                return i,(x-1)
            else:
                i-=1
    return None
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
    ejes= [
        [(1,0),(-1,0)],
        [(0,1),(0,-1)],
        [(1,1),(-1,-1)],
        [(1,-1),(-1,1)]
        ]
    for eje in ejes:
        contador = 1
        for (dirx,diry) in eje:
            i = 1
            condicion = True
            while condicion:
                x2,y2 = x+ i*dirx,y+ i*diry
                if 0<=x2<=5 and 0<=y2<=6:
                    if tablero[x][y] != tablero[x2][y2]:
                        condicion= False
                    else:
                        i+=1
                        contador+=1
                else:
                    condicion = False
            if contador >= 4:
                return True,tablero[x][y]
    return False,"Vacio"
def crear_estadisticas_jugador(estadisticas:dict,nombre:str):
    estadisticas[nombre] = {"Ganado":0,"Empatado":0,"Perdido":0,"Puntuacion":0}
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
    ejes= [
        [(1,0),(-1,0)],
        [(0,1),(0,-1)],
        [(1,1),(-1,-1)],
        [(1,-1),(-1,1)]
        ]
    sub_contador=0
    for eje in ejes:
        contador = 1
        for (dirx,diry) in eje:
            i = 1
            condicion = True
            while condicion:
                x2,y2 = x+ i*dirx,y+ i*diry
                if 0<=x2<=5 and 0<=y2<=6:
                    if tablero[x][y] != tablero[x2][y2]:
                        condicion= False
                    else:
                        i+=1
                        contador+=1
                else:
                    condicion = False
            if contador == 3:
                sub_contador+=1
            if sub_contador >=2:
                return True,tablero[x][y]
    return False,"Vacio"
#La posicion central deberia de ir en la funcion principal del algortimo
def conectar3(tablero:list,x:int,y:int)->bool:
    """
    OBJ: Comrpobar si la ultima ficha insertada hace 3 en raya
    PRE: Dados los parametros devueltos de la funcion insertar ficha
    """
    ejes= [
        [(1,0),(-1,0)],
        [(0,1),(0,-1)],
        [(1,1),(-1,-1)],
        [(1,-1),(-1,1)]
        ]
    for eje in ejes:
        contador = 1
        for (dirx,diry) in eje:
            i = 1
            condicion = True
            while condicion:
                x2,y2 = x+ i*dirx,y+ i*diry
                if 0<=x2<=5 and 0<=y2<=6:
                    if tablero[x][y] != tablero[x2][y2]:
                        condicion= False
                    else:
                        i+=1
                        contador+=1
                else:
                    condicion = False
            if contador == 3:
                return True,tablero[x][y]
    return False,"Vacio"
def conectar2(tablero:list,x:int,y:int)->bool:
    """
    OBJ: Comrpobar si la ultima ficha insertada hace 2 en raya
    PRE: Dados los parametros devueltos de la funcion insertar ficha
    """
    ejes= [
        [(1,0),(-1,0)],
        [(0,1),(0,-1)],
        [(1,1),(-1,-1)],
        [(1,-1),(-1,1)]
        ]
    for eje in ejes:
        contador = 1
        for (dirx,diry) in eje:
            i = 1
            condicion = True
            while condicion:
                x2,y2 = x+ i*dirx,y+ i*diry
                if 0<=x2<=5 and 0<=y2<=6:
                    if tablero[x][y] != tablero[x2][y2]:
                        condicion= False
                    else:
                        i+=1
                        contador+=1
                else:
                    condicion = False
            if contador == 2:
                return True,tablero[x][y]
    return False,"Vacio"

def algoritmo_maquina(tablero:list)->tuple:
    mapa_calor= [
        [30,40,50,70,50,40,30],
        [40,60,80,100,80,60,40],
        [50,80,110,130,110,80,50],
        [50,80,110,130,110,80,50],
        [40,60,80,100,80,60,40],
        [30,40,50,70,50,40,30]
    ]
    Vacio = "[  ]"
    puntuacion_mayor = 0
    posicion  = -9999999999999999999
    for i in range(7):
        tablero_aux = copia_tablero(tablero)
        ficha_ins = insertar_ficha_segunx(tablero_aux,"B",i+1) #El mas 1 porque la funcion utiliza x-1 para que cuando el usuario meta un 7 vaya a la ultima al ser las columnas (0,6)
        puntuacion_actual = 0
        if ficha_ins is None:
            continue
        #Si una fila ya esta llena no la comprobamos
        if combrobar_ganador(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
            puntuacion_actual = 10000
        else:
            tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
            ficha_ins = insertar_ficha_segunx(tablero_aux,"R",i+1)
            if combrobar_ganador(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
                puntuacion_actual= 9000
            else:
                tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
                ficha_ins = insertar_ficha_segunx(tablero_aux,"B",i+1)
                if fork_supuesto(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
                    puntuacion_actual = 8000
                else:
                    tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
                    ficha_ins = insertar_ficha_segunx(tablero_aux,"R",i+1)
                    if fork_supuesto(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
                        puntuacion_actual= 7000
                    else:
                        tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
                        ficha_ins = insertar_ficha_segunx(tablero_aux,"R",i+1)
                        if conectar3(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
                            puntuacion_actual= 6500
                        else:
                            tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
                            ficha_ins = insertar_ficha_segunx(tablero_aux,"B",i+1)
                            if conectar3(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
                                puntuacion_actual = 150
                            else:
                                tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
                                ficha_ins = insertar_ficha_segunx(tablero_aux,"B",i+1)
                                if conectar2(tablero_aux,ficha_ins[0],ficha_ins[1])[0]:
                                    puntuacion_actual = 100
                                else:
                                    tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
                                    ficha_ins = insertar_ficha_segunx(tablero_aux,"B",i+1)
                                    if puntuacion_actual<mapa_calor[ficha_ins[0]][ficha_ins[1]]:
                                        puntuacion_actual = mapa_calor[ficha_ins[0]][ficha_ins[1]]
        tablero_aux[ficha_ins[0]][ficha_ins[1]] = Vacio
        ficha_ins = insertar_ficha_segunx(tablero_aux,"B",i+1)
        if comprobar_columna_llena1(tablero_aux,i) and puntuacion_actual<5000:
                puntuacion_actual += consecuencias_rival(tablero_aux,i+1)
        if puntuacion_actual > puntuacion_mayor: puntuacion_mayor,posicion = puntuacion_actual,i
    ficha_final = insertar_ficha_segunx(tablero,"B",posicion+1)
    return ficha_final

def consecuencias_rival(tablero:list,x:int)->int:
    """
    En tablero siempre pondre el auxiliar, y comprobaremos que pasa si el jugador inserta una ficha en dicha posicion
    Nos devuelve la puntuacion
    """
    tablero_prueba = copia_tablero(tablero)
    ficha = insertar_ficha_segunx(tablero_prueba,"R",x)
    if conectar3(tablero_prueba,ficha[0],ficha[1])[0] or conectar2(tablero_prueba,ficha[0],ficha[1])[0] or combrobar_ganador(tablero_prueba,ficha[0],ficha[1])[0] or fork_supuesto(tablero_prueba,ficha[0],ficha[1])[0]:
        puntuacion = -1000000
    else:
        puntuacion= 0
    return puntuacion
     
def copia_tablero(tablero:list)->list:
    """
    Copiamos el tablero y lo asignamos a una variable nueva
    """
    tablero_nuevo = []
    for i in tablero:
        fila = []
        for j in range(len(i)):
            fila.append( i[j])
        tablero_nuevo.append(fila)
    return tablero_nuevo
def comprobar_columna_llena1(tablero:list,x:int)->bool:
    """
    OBJ: Devuelve True si todavia se pueden poner fichas
    """
    Vacio = "[  ]"
    contador = 0
    for i in range(6):
        if tablero[i][x] == Vacio:
            contador+=1
    if contador >=1: #Esto es 2 porque queremos ver que pasaria con la ficha que el jugador pone despues de la nuestra
        return True
    else:
        return False