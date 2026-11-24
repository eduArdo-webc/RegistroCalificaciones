# Registro de calificaciones usando funciones



def registrar_calificaciones():
    calificaciones = []
    respuesta = "s"

    while respuesta == "s":
        calificacion = float(input("Ingrese la calificacion del estudiante (0 a 10): "))

        
        while calificacion < 0 or calificacion > 10:
            print("Calificacion no valida, debe estar entre 0 y 10")
            calificacion = float(input("Ingrese la calificacion otra vez: "))

        calificaciones.append(calificacion)
        respuesta = input("Desea registrar otra calificacion? (s/n): ")

    return calificaciones



def mostrar_calificaciones(calificaciones):
    print("")
    print("CALIFICACIONES REGISTRADAS")
    for i in range(len(calificaciones)):
        print("Estudiante", i + 1, ":", calificaciones[i])



def calcular_promedio(calificaciones):
    suma = 0
    for i in range(len(calificaciones)):
        suma = suma + calificaciones[i]

    promedio = suma / len(calificaciones)
    return promedio



def obtener_calificacion_mayor(calificaciones):
    mayor = calificaciones[0]
    for i in range(len(calificaciones)):
        if calificaciones[i] > mayor:
            mayor = calificaciones[i]
    return mayor



def contar_aprobados(calificaciones):
    aprobados = 0
    for i in range(len(calificaciones)):
        if calificaciones[i] >= 6:
            aprobados = aprobados + 1
    return aprobados



print(" REGISTRO DE CALIFICACIONES ")

lista = registrar_calificaciones()

mostrar_calificaciones(lista)

promedio = calcular_promedio(lista)
mayor = obtener_calificacion_mayor(lista)
aprobados = contar_aprobados(lista)
reprobados = len(lista) - aprobados

print("")
print("----- RESULTADOS -----")
print("Total de estudiantes:", len(lista))
print("Promedio del grupo:", round(promedio, 2))
print("Calificacion mas alta:", mayor)
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
