

def determinar_signo(dia, mes):
    """Determina el signo zodiacal basado en el día y mes de nacimiento"""
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    else:
        return "Piscis"

def obtener_prediccion_salud(signo):
    """Retorna la predicción de salud para 2026 según el signo"""
    predicciones = {
        "Aries": "En 2026, tu energía estará en su punto máximo. Es un buen año para iniciar una rutina de ejercicios. Cuida especialmente tus músculos y cabeza.",
        "Tauro": "El 2026 te invita a cuidar tu garganta y sistema digestivo. La alimentación consciente será clave para mantener tu característico vigor.",
        "Géminis": "Tu sistema respiratorio necesitará atención en 2026. Ejercicios de respiración y actividades al aire libre serán fundamentales para tu bienestar.",
        "Cáncer": "En 2026, el equilibrio emocional será esencial para tu salud física. Cuida tu sistema digestivo y considera terapias que integren mente y cuerpo.",
        "Leo": "Tu corazón y espalda requerirán atención especial en 2026. El ejercicio moderado pero constante será tu mejor aliado para mantener la vitalidad.",
        "Virgo": "2026 será un año para prestar atención a tu sistema digestivo. La alimentación equilibrada y técnicas de reducción del estrés mejorarán tu salud.",
        "Libra": "En 2026, tus riñones y sistema endocrino necesitarán cuidados. Mantén un equilibrio entre actividad y descanso para optimizar tu bienestar.",
        "Escorpio": "El 2026 te invita a cuidar tu sistema reproductivo y circulatorio. Las prácticas de desintoxicación serán especialmente beneficiosas.",
        "Sagitario": "Tu sistema nervioso y caderas requerirán atención en 2026. Actividades al aire libre y ejercicios de estiramiento serán fundamentales.",
        "Capricornio": "En 2026, tus huesos, articulaciones y piel necesitarán cuidados especiales. Una rutina de ejercicios de bajo impacto será ideal.",
        "Acuario": "2026 será un año para cuidar tu sistema circulatorio y tobillos. Técnicas de relajación y ejercicios de respiración mejorarán tu salud.",
        "Piscis": "En 2026, tu sistema linfático e inmunológico estarán en foco. El descanso adecuado y la hidratación serán esenciales para tu bienestar."
    }
    return predicciones[signo]

def obtener_prediccion_dinero(signo):
    """Retorna la predicción financiera para 2026 según el signo"""
    predicciones = {
        "Aries": "2026 traerá oportunidades financieras inesperadas. Tu audacia será recompensada, pero evita decisiones impulsivas con grandes inversiones.",
        "Tauro": "En 2026, tu estabilidad financiera se fortalecerá. Es un buen año para inversiones a largo plazo, especialmente en bienes raíces.",
        "Géminis": "El 2026 favorecerá los ingresos por proyectos creativos y comunicación. Diversifica tus fuentes de ingreso para maximizar beneficios.",
        "Cáncer": "2026 será un año de consolidación económica. Tus habilidades para el ahorro te permitirán crear un fondo de seguridad importante.",
        "Leo": "En 2026, brillarás en lo financiero si apuestas por proyectos que te apasionen. Posibles ingresos por actividades creativas o de liderazgo.",
        "Virgo": "El 2026 premiará tu meticulosidad en las finanzas. Es un excelente año para reorganizar tu economía y eliminar gastos innecesarios.",
        "Libra": "2026 traerá equilibrio a tus finanzas. Posibles ingresos a través de asociaciones o actividades relacionadas con el arte y la belleza.",
        "Escorpio": "En 2026, tu intuición para los negocios estará en su punto máximo. Posibilidades de recibir herencias o beneficios de recursos compartidos.",
        "Sagitario": "El 2026 favorecerá la expansión financiera a través de estudios o contactos internacionales. Buen momento para inversiones educativas.",
        "Capricornio": "2026 será un año de reconocimiento profesional que se traducirá en mejoras económicas. Tu disciplina con el dinero dará frutos.",
        "Acuario": "En 2026, los ingresos pueden llegar de formas innovadoras o tecnológicas. Buen momento para emprendimientos grupales o comunitarios.",
        "Piscis": "El 2026 mejorará tu relación con el dinero. Tu creatividad e intuición te guiarán hacia oportunidades financieras inesperadas."
    }
    return predicciones[signo]

def obtener_prediccion_amor(signo):
    """Retorna la predicción amorosa para 2026 según el signo"""
    predicciones = {
        "Aries": "En 2026, tu vida amorosa será apasionada y dinámica. Si estás en pareja, renovarás la chispa; si estás soltero/a, posibles encuentros intensos.",
        "Tauro": "2026 traerá estabilidad a tu vida sentimental. Las relaciones basadas en valores compartidos y comodidad serán especialmente favorecidas.",
        "Géminis": "El 2026 será un año de comunicación profunda en el amor. Expresar tus sentimientos con claridad fortalecerá tus relaciones existentes.",
        "Cáncer": "En 2026, la intimidad emocional será tu prioridad. Posible consolidación de relaciones existentes o encuentros con gran conexión emocional.",
        "Leo": "2026 iluminará tu vida romántica. Si tienes pareja, vivirán momentos memorables; si estás soltero/a, atraerás admiradores con facilidad.",
        "Virgo": "El 2026 te invita a equilibrar razón y emoción en el amor. Posibles conexiones con personas que valoren tu inteligencia y atención al detalle.",
        "Libra": "En 2026, la armonía reinará en tus relaciones. Buen momento para compromisos o para encontrar una pareja que comparta tus ideales de equilibrio.",
        "Escorpio": "2026 será un año de transformación en el amor. Las relaciones superficiales darán paso a conexiones profundas y significativas.",
        "Sagitario": "El 2026 traerá aventuras románticas y expansión emocional. Posibles conexiones con personas de diferentes culturas o filosofías de vida.",
        "Capricornio": "En 2026, el compromiso y la responsabilidad en el amor serán temas centrales. Las relaciones maduras y estables serán favorecidas.",
        "Acuario": "2026 renovará tu visión del amor. Relaciones basadas en la amistad, libertad y respeto mutuo serán especialmente favorecidas.",
        "Piscis": "El 2026 será mágico para tu vida sentimental. Tu sensibilidad atraerá personas que aprecien tu mundo interior y capacidad de entrega."
    }
    return predicciones[signo]

def validar_fecha(dia, mes):
    """Valida que la fecha ingresada sea correcta"""
    dias_por_mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2026 no es bisiesto
    
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_por_mes[mes]:
        return False
    return True

# Programa principal
print("=" * 60)
print("HORÓSCOPO 2026 - PERIÓDICO NACIONAL".center(60))
print("=" * 60)
print("\nDescubre qué te depara el año 2026 en salud, dinero y amor")
print("-" * 60)

# Solicitar fecha de nacimiento
while True:
    try:
        dia = int(input("\nIngresa tu día de nacimiento (1-31): "))
        mes = int(input("Ingresa tu mes de nacimiento (1-12): "))
        
        if validar_fecha(dia, mes):
            break
        else:
            print("\n¡Error! Fecha no válida. Por favor, intenta nuevamente.")
    except ValueError:
        print("\n¡Error! Debes ingresar números enteros. Por favor, intenta nuevamente.")

# Determinar signo zodiacal
signo = determinar_signo(dia, mes)

# Mostrar resultados
print("\n" + "=" * 60)
print(f"TU HORÓSCOPO 2026: {signo.upper()}".center(60))
print("=" * 60)

print("\n✨ DESCRIPCIÓN:")
if signo == "Aries":
    print("Aries es el primer signo del zodíaco. Caracterizado por su energía, iniciativa y valentía.")
elif signo == "Tauro":
    print("Tauro es el segundo signo del zodíaco. Destaca por su determinación, practicidad y aprecio por la belleza.")
elif signo == "Géminis":
    print("Géminis es el tercer signo del zodíaco. Conocido por su curiosidad, adaptabilidad y comunicación.")
elif signo == "Cáncer":
    print("Cáncer es el cuarto signo del zodíaco. Caracterizado por su sensibilidad, intuición y protección.")
elif signo == "Leo":
    print("Leo es el quinto signo del zodíaco. Destaca por su creatividad, generosidad y liderazgo natural.")
elif signo == "Virgo":
    print("Virgo es el sexto signo del zodíaco. Conocido por su meticulosidad, inteligencia y servicio.")
elif signo == "Libra":
    print("Libra es el séptimo signo del zodíaco. Caracterizado por su diplomacia, sentido de justicia y aprecio por la armonía.")
elif signo == "Escorpio":
    print("Escorpio es el octavo signo del zodíaco. Destaca por su intensidad, pasión y capacidad de transformación.")
elif signo == "Sagitario":
    print("Sagitario es el noveno signo del zodíaco. Conocido por su optimismo, sinceridad y amor por la libertad.")
elif signo == "Capricornio":
    print("Capricornio es el décimo signo del zodíaco. Caracterizado por su ambición, disciplina y sentido de responsabilidad.")
elif signo == "Acuario":
    print("Acuario es el undécimo signo del zodíaco. Destaca por su originalidad, humanitarismo e independencia.")
elif signo == "Piscis":
    print("Piscis es el duodécimo signo del zodíaco. Conocido por su compasión, intuición y sensibilidad artística.")

print("\n❤️ PREDICCIÓN AMOR 2026:")
print(obtener_prediccion_amor(signo))

print("\n💰 PREDICCIÓN DINERO 2026:")
print(obtener_prediccion_dinero(signo))

print("\n🌿 PREDICCIÓN SALUD 2026:")
print(obtener_prediccion_salud(signo))

print("\n" + "=" * 60)
print("PERIÓDICO NACIONAL - Horóscopo Especial 2026".center(60))
print("=" * 60)