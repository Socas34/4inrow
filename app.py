import funciones_basicas as f
estadisticas = f.cargar_datos()
f.menu()
opcion = f.validar_entrada_rango(1,3,"Introduzca una opción dado el siguiente menu: ")
while opcion != 3:
    if opcion == 1:
        print("Seleccione un modo de juego: \n1.Jugador vs jugador\n2.Jugador vs maquina")
        opcion2 = f.validar_entrada_rango(1,2,"Introduzca un modo de juego: ")
        if opcion2 == 1:
            condicion = True
            i = 0
            tablero = f.crear_tablero()
            f.imprimir_tablero(tablero)
            while condicion:
                tablero_ant = f.copia_tablero(tablero)
                if i%2 == 0: color = "R"
                else: color = "B"
                ult_ficha = f.insertar_ficha(tablero,color)
                if tablero_ant == tablero:
                    print("Introduccion invalida, intentelo de nuevo: ")
                    continue
                ganadorc = f.combrobar_ganador(tablero,ult_ficha[0],ult_ficha[1])
                if ganadorc[0]:
                    break
                if f.combrobar_tablerolleno(tablero):
                    break
                f.imprimir_tablero(tablero)
                i+=1
            if ganadorc[1] == ("[""\033[41m"+"  "+"\033[0m""]"): colorg = "Rojo"
            elif ganadorc[1] == ("[""\033[44m"+"  "+"\033[0m""]"): colorg = "Azul"
            if i <42:
                print(f"El ganador ha sido el jugador {colorg}")
                nombreg = input("Introduzca el nombre del ganador: ")
                if nombreg not in estadisticas:
                    f.crear_estadisticas_jugador(estadisticas,nombreg)
                f.guardar_estadisticas_ganado(estadisticas,(i//2+i%2),nombreg)
                nombrep = input("Introduzca el nombre del perdedor: ")
                if nombrep not in estadisticas:
                    f.crear_estadisticas_jugador(estadisticas,nombrep)
                f.guardar_estadisticas_perdido(estadisticas,nombrep)                
            else:
                print("Empate!")
                nombre1,nombre2 = input("Introduzca el nombre del jugador: "), input("Introduzca el nombre del otro jugador: ")
                if nombre1 not in estadisticas:
                    f.crear_estadisticas_jugador(estadisticas,nombre1)
                f.guardar_estadisticas_empatado(estadisticas,nombre1)
                if nombre2 not in estadisticas:
                    f.crear_estadisticas_jugador(estadisticas,nombre2)
                f.guardar_estadisticas_empatado(estadisticas,nombre2)
        elif opcion2 == 2:
            condicion = True
            i = 0
            tablero = f.crear_tablero()
            f.imprimir_tablero(tablero)
            while condicion:
                tablero_ant = f.copia_tablero(tablero)
                ult_ficha = f.insertar_ficha(tablero,"R")
                if tablero == tablero_ant:
                    print("Introduccion invalida, repita la entrada")
                    continue
                i +=1
                ganadorc = f.combrobar_ganador(tablero,ult_ficha[0],ult_ficha[1])
                if ganadorc[0]:
                    break
                ult_ficha = f.algoritmo_maquina(tablero)
                f.imprimir_tablero(tablero)
                i+=1
                ganadorc = f.combrobar_ganador(tablero,ult_ficha[0],ult_ficha[1])
                if ganadorc[0]:
                    break
                if f.combrobar_tablerolleno(tablero):
                    condicion = False
            if i%2 != 0: colorg = "Rojo"
            elif i%2 == 0: colorg = "Azul"
            if i <42:
                if colorg == "Rojo":
                    print(f"El ganador ha sido el jugador {colorg}")
                    nombreg = input("Introduzca el nombre del ganador: ")
                    if nombreg not in estadisticas:
                        f.crear_estadisticas_jugador(estadisticas,nombreg)
                    f.guardar_estadisticas_ganado(estadisticas,(i//2+i%2),nombreg)
                    f.guardar_estadisticas_perdido(estadisticas,"Maquina")
                elif colorg == "Azul":
                    print(f"El ganador ha sido {colorg}")
                    f.guardar_estadisticas_ganado(estadisticas,(i//2+i%2),"Maquina")
                    nombrep= input("Introduzca el nombre del perdedor: ")
                    if nombrep not in estadisticas:
                        f.crear_estadisticas_jugador(estadisticas,nombreg)
                    f.guardar_estadisticas_perdido(estadisticas,nombrep)
            else:
                print("Empatado!")
                nombre = input("Introduzca su nombre: ")
                if nombre not in estadisticas:
                    f.crear_estadisticas_jugador(estadisticas,nombre)
                f.guardar_estadisticas_empatado(estadisticas,nombre)
                f.guardar_estadisticas_empatado(estadisticas,"Maquina")
print("Finalizando...")
print("Mostrando estadisticas:\n")
print(estadisticas)

