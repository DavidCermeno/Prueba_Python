# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:01:31 2021

@author: Licht
"""

# Variables
a = 3
print(type(a))
a = "hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

# Operaciones

# Suma
a = 5
b = 2
c = a + b
print(c)

# Resta
a = 5
b = 2
c = a - b
print(c)

# Multiplicación
a = 5
b = 2
c = a * b
print(c)

# División
a = 5
b = 2
c = a / b
print(c)

# Potencia
a = 5
b = 2
c = a ** b
print(c)

# Raíz Cuadrada
a = 16
b = a ** (1/2)
print(b)

# import math
# raiz = math.sqrt(16)
# print(raiz)

# TIPOS DE DATOS

# String str

a = "Hola mundo"
a = 'Hola mundo'
b = "I can't do it"
c = 'Alias "Roberto"'
print(a)
print(b)
print(c)

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones etre tipos de datos

# Convertir de x a entero
a = '3'
y = int(a)
print(y)
print(type(y))

# Convertir de x a decimal
a = '3'
y = float(a)
print(y)
print(type(y))

# Convertir de x a String
a = '3'
y = str(a)
print(y)
print(type(y))

# Concatenaciones

a = 'hola'
b = 'mundo'
c = a + ' ' + b
print(c)

a = 'hola'
b = a * 5
print(b)


# Capturar por pantalla

nombre = input('Digite su nombre: ')
print('Hola,', nombre)


# HUA que sume dos número e imprima su resultado

numero_uno = float(input('Digite el número uno : '))
numero_dos = float(input('Digite el número dos : '))
suma = numero_uno + numero_dos
# print(suma)
# print('La suma es:', suma)
print(f'La suma es {suma}')


# HUA que lea un número y lo eleve al cuadrado
numero = float(input('Digite número a elevar: '))
potencia = float(input('Digite número de potencia: '))
elevar = numero ** potencia
print(f'El resultado es: {elevar} ')

# HUA que tome el valor de un producto, le aplique el 20% de descuento
# imprima el valor del producto inicial, el valorcon descuento
# y el valor ahorrado

val_prod = float(input('Digite el valor del producto: '))
desc = val_prod * 0.20
ahorro = val_prod - desc
print(f'El valor del producto incial es de: ${val_prod:,}')
print(f'El valor de descuento es de: ${desc:,}')
print(f'El valor ahorrado es: ${desc:,}')

# CONDICIONALES

# Tabla de verdad

# Tabla del and
# v and v = v
# v and f = f
# f and f = f
# f and v = f

# Tabla de verdad de or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

# Tabla del and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabla del or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negación
print(not True)
print(not False)

# Jerarquía de operaciones
# 1. Paréntisis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. Sumas y Restas

# Jerarquía para operaciones booleanas
# 1. Paréntesis y llaves
# 2. Tabla de verdad

# Mas de dos codniciones al mismo tiempo
print(True and False and True or False or True or True)
print(True and (False and True) or False or (True or True))

# Estructura IF

if (x > 0):
    print('1')
else:
    print('2')
print('3')

# HUA que dada la edad de una persona indique si es mayor# o menor de edad

edad = int(input('Digite la edad de la persona: '))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')


# HUA que indique si un estudiante aprobó o reprobó una asigantura
# nota

nota = float(input('Ingrese nota del estudiante: '))
if nota < 0 or nota > 5:
    print(f'{nota} No es una nota válida')
elif nota >= 3 and nota <= 5:
    print('Aprobó')
else:
    print('Reprobó')

# HUA que dado un número n diga si es negativo, positivo o cero

num = float(input('Digite númeroo a validar: '))
if num < 0:
    print(f'El número: {num} es negativo')
elif num > 0:
    print(f'El número: {num} es positivo')
else:
    print(f'El número: {num} es cero')


























