#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria


class OrdenamientoSeleccion(object):

    # constructor de clase
    def __init__(self, valores):
        self.datos = valores

    # ordena el arreglo usando el ordenamiento por seleccion
    def ordenar(self):
        masPequenio = int  # Indice mas pequenio

        # Itera a traves de len(self.datos) - 1 elementos
        for i in range(0, len(self.datos) - 1):
            masPequenio = i  # primer indice del resto del arreglo

            # Itera para buscar el indice del elemento mas quenio
            for indice in range(i+1, len(self.datos)):
                if self.datos[indice] < self.datos[masPequenio]:
                    masPequenio = indice

            # Intercambia el elemento mas pequenio en la posicion
            self.intercambiar(i, masPequenio)

            # Imprime su porpio objeto
            print(self)

    def intercambiar(self, primero: int, segundo: int):
        temporal = self.datos[primero]  # almacena primero temporal
        # Sustituye primero con segundo
        self.datos[primero] = self.datos[segundo]
        self.datos[segundo] = temporal  # Coloca temporal en segundo

    def __str__(self):
        temporal = ''

        # Itera a tra ves del arreglo
        for elemento in self.datos:
            temporal += ' {}'.format(elemento)

        temporal += '\n'
        return temporal
