#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

from ordInsercion import OrdenamientoInsercion

valores = [34, 56, 4, 10, 77, 50, 93, 30, 5, 52]

# Crea un objeto para realizar el ordenamiento por insercion
arregloOrden = OrdenamientoInsercion(valores)

print('Arreglo desordenado: ')
print(arregloOrden)  # imprime el arreglo desordenado

arregloOrden.ordenar()  # Ordena el arreglo

print('Arreglo ordenado: ')
print(arregloOrden)  # imprime el arreglo ordenado
