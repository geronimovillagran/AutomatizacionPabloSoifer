def promedio(a, b, c):
   return (a + b + c) / 3



nombre = input('Ingrese Nombre del alumno: ')
apellido = input('Ingrese el Apellido del alumno: ')
matematica = int(input('Ingrese la nota de Matematica: '))
literatura = int(input('Ingrese la nota de Literatura: '))
fisica = int(input('Ingrese la nota de Fisica: '))

promedio_total = promedio(matematica, literatura, fisica)

if promedio_total >= 6:
    print(nombre, apellido, 'su promedio es: ', promedio_total)
    print('Aprobado!')
    if promedio_total >= 9:
        print('Alumno Destacado!!')
elif promedio_total < 4:
    print(nombre, apellido, 'su promedio es: ', promedio_total)
    print('Insuficiente!')
else:
    print(nombre, apellido, 'su promedio es: ', promedio_total)
    print('A recuperatorio!')
