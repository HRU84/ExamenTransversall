import os, time, random, csv

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = [""]
 
    
def sueldos():
    
    sueldos = [random.randint(300000,2500000) for pagos in range(len(trabajadores))]
    
    return(sueldos)


def clasificar_sueldos(sueldos):
    os.system('cls')
    time.sleep(1)
    
    clasificacion = {
        'sueldos menores a $800.000': [],
        'sueldos entre $800.000 y 2.000.000': [],
        'sueldos superiores a $2.0000.000' : []
    }
    
    for pagos in sueldos:
        if pagos < 800000:
            clasificacion['sueldos menores a $800.000'].append(pagos)
        elif 800000 <= pagos <= 2000000:
            clasificacion['sueldos entre $800.000 y 2.000.000'].append(pagos)
        else :
            clasificacion['sueldos superiores a $2.0000.000'].append(pagos)
        return clasificacion
    


def estadisticas(sueldos):
    os.system('cls')
    time.sleep(1)
    
    for pagos in sueldos:
        if pagos == sueldos[0]:
            print()
        
        


def reporte_sueldos(sueldos):
    os.system('cls')
    time.sleep(1)
    
    for pagos in sueldos:
        sueldo_base = sueldos[pagos]
        descuento_salud = int(sueldo_base * 0.07)
        descuento_afp = int(sueldo_base * 0.12)
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        #tabla_reporte = 
        
def guardar_reporte ():
    os.system('cls')
    time.sleep(1)
    
    with open ('Reporte de sueldos.csv', 'w', newline= '' ) as reporte_sueldos:
        writer = csv.writer(reporte_sueldos)
        writer.wirterow([])
        writer.wirterows(reporte_sueldos)
        
def salir():
    os.system('cls')
    time.sleep(1)
    
    print('Finalizando programa...')
    print('Desarrollado por Wilfred Vinet')
    print('Rut 19.902.142-7')
    

def menu(): 
    print('----Menú----')
        
        
    print('1) Asignar sueldos aleatorios')
    print('2) Clasificar sueldos')
    print('3) Ver estadisticas')
    print('4) Reporte sueldos')
    print('5) Salir del programa')


menu()    
while True:
        try:
            print("")
            opcion = int(input('ingrese una opcion\n'))
            
            if opcion == 1:
                print('Creando sueldos aleatorios...')
                sueldos()
                print('sueldos creados satisfactortiamente')
            
            elif opcion == 2:
                print('desea crear sueldos?  (s/n)\n')
                respuesta = input('ingrese s/n')
                if respuesta == "s":
                    sueldos()
                    print('Clasificar sueldos')
                    clasificar_sueldos()
                else :
                    if sueldos != [""]:
                        clasificar_sueldos()
                        
                    else:
                        print('no existen sueldos, intente nuevamente')
                        continue
                
                    
                
            elif opcion == 3:
                print('Ver estadisticas')
                estadisticas()
                
            elif opcion == 4:
                print('Repore de sueldos')
                reporte_sueldos()
            
            elif opcion == 5:
                salir()
                break
            
            else:
                print ('Valor invalido')
                continue
        except ValueError:
            print('opcion invalida, intente nuevamente')