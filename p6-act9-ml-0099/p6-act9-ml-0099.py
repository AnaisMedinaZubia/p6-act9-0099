# Medica Anais NC 0099
# ==========================================
# EJEMPLOS DE PYTHON
# Variables, tipos de datos y operadores
# ==========================================


# ==========================================
# 1. VARIABLES
# ==========================================

print("===== EJEMPLO 1: VARIABLES =====")

nombre = "Anais"
edad = 17

print("Nombre:", nombre)
print("Edad:", edad)


print("\n===== EJEMPLO 2: VARIABLES =====")

producto = "Cuaderno"
precio = 35

print("Producto:", producto)
print("Precio:", precio)


print("\n===== EJEMPLO 3: VARIABLES =====")

ciudad = "Ciudad Juarez"
temperatura = 28

print("Ciudad:", ciudad)
print("Temperatura:", temperatura)


# ==========================================
# 2. VARIABLES MULTIPLES
# ==========================================

print("\n===== EJEMPLO 1: VARIABLES MULTIPLES =====")

nombre, edad, grado = "Anais", 17, 5

print("Nombre:", nombre)
print("Edad:", edad)
print("Grado:", grado)


print("\n===== EJEMPLO 2: VARIABLES MULTIPLES =====")

producto, precio, cantidad = "Pluma", 10, 5

print("Producto:", producto)
print("Precio:", precio)
print("Cantidad:", cantidad)


print("\n===== EJEMPLO 3: VARIABLES MULTIPLES =====")

x, y, z = 10, 20, 30

print("Valor de x:", x)
print("Valor de y:", y)
print("Valor de z:", z)


# ==========================================
# 3. TIPOS DE DATOS
# ==========================================

print("\n===== EJEMPLO 1: STRING =====")

nombre = "Anais"

print("Nombre:", nombre)
print("Tipo de dato:", type(nombre))


print("\n===== EJEMPLO 2: INTEGER =====")

edad = 17

print("Edad:", edad)
print("Tipo de dato:", type(edad))


print("\n===== EJEMPLO 3: FLOAT =====")

precio = 25.50

print("Precio:", precio)
print("Tipo de dato:", type(precio))


# ==========================================
# 4. OPERADORES ARITMETICOS
# ==========================================

print("\n===== EJEMPLO 1: SUMA =====")

numero1 = 10
numero2 = 5

resultado = numero1 + numero2

print("Numero 1:", numero1)
print("Numero 2:", numero2)
print("Resultado de la suma:", resultado)


print("\n===== EJEMPLO 2: RESTA =====")

numero1 = 20
numero2 = 8

resultado = numero1 - numero2

print("Numero 1:", numero1)
print("Numero 2:", numero2)
print("Resultado de la resta:", resultado)


print("\n===== EJEMPLO 3: MULTIPLICACION =====")

precio = 50
cantidad = 4

resultado = precio * cantidad

print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", resultado)


# ==========================================
# 5. OPERADORES DE COMPARACION
# ==========================================

print("\n===== EJEMPLO 1: IGUAL QUE =====")

numero1 = 10
numero2 = 10

resultado = numero1 == numero2

print("Numero 1:", numero1)
print("Numero 2:", numero2)
print("¿Son iguales?", resultado)


print("\n===== EJEMPLO 2: MAYOR QUE =====")

edad = 18

resultado = edad > 17

print("Edad:", edad)
print("¿Es mayor que 17?", resultado)


print("\n===== EJEMPLO 3: MENOR QUE =====")

calificacion = 7

resultado = calificacion < 10

print("Calificacion:", calificacion)
print("¿Es menor que 10?", resultado)


# ==========================================
# 6. OPERADORES LOGICOS
# ==========================================

print("\n===== EJEMPLO 1: AND =====")

edad = 18
tiene_identificacion = True

resultado = edad >= 18 and tiene_identificacion == True

print("Edad:", edad)
print("Tiene identificacion:", tiene_identificacion)
print("¿Puede realizar el tramite?", resultado)


print("\n===== EJEMPLO 2: OR =====")

dia = "sabado"

resultado = dia == "sabado" or dia == "domingo"

print("Dia:", dia)
print("¿Es fin de semana?", resultado)


print("\n===== EJEMPLO 3: NOT =====")

lluvia = False

resultado = not lluvia

print("¿Esta lloviendo?", lluvia)
print("¿No esta lloviendo?", resultado)


# ==========================================
# FIN DEL PROGRAMA
# ==========================================

print("\n===== Medica Anais NC 0099 =====")