

def calcular_imc(peso, altura):
    """Calcula el IMC dividiendo el peso (kg) entre la altura al cuadrado (m)"""
    return peso / (altura ** 2)

def obtener_categoria_imc(imc):
    """Determina la categoría de peso basada en el valor del IMC"""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad grado I"
    elif imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def recomendar_ejercicios(categoria):
    """Proporciona recomendaciones de ejercicios según la categoría de IMC"""
    if categoria == "Bajo peso":
        return """
        Rutina de ejercicios recomendada:
        - Entrenamiento de fuerza 3 veces por semana
        - Ejercicios de resistencia con pesas ligeras
        - Yoga o pilates para mejorar la flexibilidad
        - Evitar ejercicio cardiovascular excesivo
        """
    elif categoria == "Peso normal":
        return """
        Rutina de ejercicios recomendada:
        - Combinación de ejercicios cardiovasculares y de fuerza
        - 150 minutos semanales de actividad moderada
        - Incluir 2-3 días de entrenamiento de fuerza
        - Actividades recreativas como natación, ciclismo o deportes de equipo
        """
    elif categoria == "Sobrepeso":
        return """
        Rutina de ejercicios recomendada:
        - 30 minutos diarios de ejercicio cardiovascular (caminar, nadar, bicicleta)
        - Entrenamiento de fuerza 2 veces por semana
        - Aumentar gradualmente la intensidad
        - Considerar actividades de bajo impacto si hay problemas articulares
        """
    else:  # Cualquier grado de obesidad
        return """
        Rutina de ejercicios recomendada:
        - Comenzar con caminatas diarias de 15-20 minutos
        - Ejercicios acuáticos para reducir impacto en articulaciones
        - Entrenamiento con resistencia supervisado
        - Aumentar gradualmente la duración e intensidad
        - Considerar apoyo de un profesional en educación física
        """

def recomendar_dieta(categoria):
    """Proporciona recomendaciones de dieta según la categoría de IMC"""
    if categoria == "Bajo peso":
        return """
        Dieta recomendada:
        - Aumentar la ingesta calórica con alimentos nutritivos
        - Consumir proteínas de alta calidad en cada comida
        - Incluir grasas saludables como aguacate, frutos secos y aceite de oliva
        - 5-6 comidas pequeñas al día
        - Batidos nutritivos como complemento
        """
    elif categoria == "Peso normal":
        return """
        Dieta recomendada:
        - Mantener una alimentación balanceada
        - Consumir frutas y verduras variadas
        - Proteínas magras y carbohidratos complejos
        - Limitar alimentos procesados y azúcares
        - Mantener una adecuada hidratación
        """
    elif categoria == "Sobrepeso":
        return """
        Dieta recomendada:
        - Reducir moderadamente la ingesta calórica
        - Aumentar el consumo de verduras y frutas
        - Elegir proteínas magras (pollo, pescado, legumbres)
        - Limitar carbohidratos refinados y azúcares
        - Controlar el tamaño de las porciones
        - Evitar bebidas azucaradas
        """
    else:  # Cualquier grado de obesidad
        return """
        Dieta recomendada:
        - Plan de alimentación supervisado por nutricionista
        - Reducción controlada de calorías
        - Eliminar alimentos ultraprocesados
        - Aumentar significativamente el consumo de verduras
        - Consumir proteínas magras en cada comida
        - Beber al menos 2 litros de agua diarios
        - Llevar un registro de alimentación
        """

# Programa principal
print("=" * 50)
print("CENTRO MÉDICO - SISTEMA DE EVALUACIÓN DE IMC")
print("=" * 50)

# Solicitar datos del paciente
nombre = input("Nombre del paciente: ")

# Validar peso
while True:
    try:
        peso = float(input("Peso en kg: "))
        if peso <= 0:
            print("Error: El peso debe ser un valor positivo.")
        else:
            break
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

# Validar altura
while True:
    try:
        altura = float(input("Altura en metros: "))
        if altura <= 0:
            print("Error: La altura debe ser un valor positivo.")
        else:
            break
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

# Calcular IMC y obtener categoría
imc = calcular_imc(peso, altura)
categoria = obtener_categoria_imc(imc)

# Mostrar resultados
print("" + "=" * 50)
print(f"RESULTADOS PARA: {nombre}")
print("=" * 50)
print(f"Su IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")

# Mostrar recomendaciones
print("" + "-" * 50)
print("PLAN DE ACCIÓN RECOMENDADO")
print("-" * 50)
print(recomendar_ejercicios(categoria))
print(recomendar_dieta(categoria))

print("Nota: Estas recomendaciones son generales. Para un plan personalizado,")
print("consulte con profesionales de la salud (médico, nutricionista, entrenador).")
print("=" * 50)