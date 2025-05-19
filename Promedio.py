# Inicializar variables
suma_notas = 0
cantidad_materias = 7

# Definir los nombres de las materias
materias = [
    "Programación",
    "Bases de Datos",
    "Sistemas Operativos",
    "Redes",
    "Matemáticas Discretas",
    "Algoritmos",
    "Ingeniería de Software"
]

# Solicitar las notas de las 7 materias
print("Bienvenido al sistema de cálculo de promedio semestral")
print("Por favor ingrese las notas de las 7 materias (de 0 a 6):")

for i in range(cantidad_materias):
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {materias[i]}: "))
            # Validar que la nota esté en el rango correcto (0-6)
            if 0 <= nota <= 6:
                suma_notas += nota
                break
            else:
                print("Error: La nota debe estar entre 0 y 6. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

# Calcular el promedio
promedio = suma_notas / cantidad_materias

# Mostrar el promedio con dos decimales
print(f"\nEl promedio del estudiante es: {promedio:.2f}")

# Determinar si el estudiante aprobó o reprobó
if promedio < 3:
    print("El estudiante ha REPROBADO el semestre.")
elif 3 <= promedio <= 6:
    print("El estudiante ha APROBADO el semestre.")

# Mostrar mensaje adicional según el rendimiento
if promedio >= 5:
    print("¡Felicitaciones por el excelente rendimiento!")
elif promedio >= 4:
    print("Buen trabajo, sigue así.")
elif promedio >= 3:
    print("Has aprobado, pero puedes mejorar.")