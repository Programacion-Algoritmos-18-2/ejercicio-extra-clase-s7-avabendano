#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria


class OrdenamientoInsercion(object):
    """Clase que crea un arreglo lleno de enteros aleatorios.
    Proporciona un metodo para ordenar el arreglo mediante el ordenamiento por insercion."""
    # Constructor de clase

    def __init__(self, valores: list):
        self.datos = valores  # Arreglo de valores

    # Ordena el arreglo usando el ordenamiento por insercion
    def ordenar(self):
        # variable temporal para contener el elemento a insertar
        insercion = int

        # Itera a traves de algunos daos.length - elementos
        for siguiente in range(1, len(self.datos)):

            # Alamacena el valor en el elemento actual
            insercion = self.datos[siguiente]

            # Iniicializa ubicacion para colocar el elemento
            moverElemento = siguiente

            # Busca un lugar para colocar el elemento actual
            while moverElemento > 0 and self.datos[moverElemento - 1] > insercion:
                # Desplaza el elemento una posicion a la derecha
                self.datos[moverElemento] = self.datos[moverElemento - 1]
                moverElemento -= 1

            # Coloca el elemento insertado
            self.datos[moverElemento] = insercion
            # Imprimo el mismo objeto
            print('{}'.format(self))

    # Imprime una pasada del algoritmo
    def imprimirPasada(self, pasada: int, indice: int):
        print('despues de pasada {}: '.format(pasada))

        # Imprime los elementos hasta el elemento intercambio
        for i in range(0, indice):
            print('{} '.format(self.datos[i]))

        print('{}* '.format(self.datos[indice]))

        # Termina de imprimir el arreglo en pantalla
        for i in range(indice + 1, len(self.datos)):
            print('{} '.format(self.datos[i]))

        print('\n               ')  # para alineacion

        # Indica la cantidad del arreglo que este ordenado
        for i in range(0, pasada + 1):
            print('-- ')
        print('\n')  # Arrelga fin de la linea

    # Metodo para mostrar los valores del arreglo en pantalla
    def __str__(self):
        temporal = ''

        # Itera a traves del arreglo
        for elemento in self.datos:
            temporal += '{} '.format(elemento)

        temporal += '\n'
        return temporal
