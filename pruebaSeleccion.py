#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

from ordSeleccion import OrdenamientoSeleccion

valores = [100, 12, 3, 20, 28, 15]

# Crea un objeto para realizar el ordenamiento por insercion
arregloOrden = OrdenamientoSeleccion(valores)

print('Arreglo desordenado: ')
print(arregloOrden)  # imprime el arreglo desordenado

arregloOrden.ordenar()  # Ordena el arreglo

print('Arreglo ordenado: ')
print(arregloOrden)  # imprime el arreglo ordenado
