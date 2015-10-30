# -*- coding: utf-8 -*-
from RecolectorDatos import RecolectorDatos

# Clase que sirve para hacer estadísticas

class Estadisticas:

    @classmethod
    def obtenerPorcentajeSuspensosProfesores(self, filtro):
        #Primero obtenemos las notas
        notas = RecolectorDatos.obtenerNotas("SinFiltros")
        #Asignamos cada nota al profe que lo ha puesto
        notas_profes=[] #Estructura: [Profesor1{id_profe,nota1,nota2,nota3....}, Profesor2{id_profe,nota1,nota2,nota3,....}]
        if(len(notas) > 0): # Hay algunas notas
            for indice_calificacion in range(len(notas)): #Recorremos todas las tuplas [id_profe,id_alumno,nota]
                insertado=False
                if(len(notas_profes) > 0):   #Si hay profesores registrados de antes...
                    for profesor in range(len(notas_profes)):
                        if notas[indice_calificacion][0] == notas_profes[profesor][0] and insertado==False:#El indice de profe de la nota coincide con n profe ya añadido
                            notas_profes[profesor].append(notas[indice_calificacion][2])
                            insertado=True

                    if insertado==False:    #Si no se ha insertado es por que no ha coincidido con ningun profe, así que el profesor es nuevo
                        notas_profes.append([])
                        indice = len(notas_profes) - 1
                        notas_profes[indice].append(notas[indice_calificacion][0]) #Añadimos el indice del profe
                        notas_profes[indice].append(notas[indice_calificacion][2]) #Añadimos la nota al profesor
                else:               #Si no, lo registramos
                    notas_profes.append([])
                    notas_profes[0].append(notas[indice_calificacion][0]) #Añadimos el indice del profe
                    notas_profes[indice_calificacion].append(notas[indice_calificacion][2]) #Añadimos la nota al profesor

        suspensos=[]    #Matriz de suspensos: [[id_profe, suspensos]]
        #Contamos los suspensos
        for indice in range(len(notas_profes)):     #Recorremos todas las listas de profesores
            suspensos.append([])
            suspensos[indice].append(notas_profes[indice][0])
            suspensos_del_profesor=0
            for indice_columna in range(1,len(notas_profes[indice])):   #recorremos todas las notas de un profe, salando el primer valor de la lista (es el id)
                if notas_profes[indice][indice_columna] <5:
                    suspensos_del_profesor = suspensos_del_profesor+1

            notas_totales = (len(notas_profes[indice]) -1)/1.0  #Entre 1.0 para forzar decimal
            porcentaje = suspensos_del_profesor / notas_totales
            suspensos[indice].append(porcentaje)

        return suspensos

    @classmethod
    def obtenerRankingFaltasCurso(self, filtro):
        return [1,2,3]

    @classmethod
    def obtenerRankingPartesCurso(self, filtro):
        return [1,2,3]
    @classmethod
    def obtenerRankingNotaMediaCurso(self, filtro):
        return [1,2,3]
    @classmethod
    def obtenerAsistenciaTotalCentro(self, filtro):
        return [1,2,3]
    @classmethod
    def obtenerRankingPartesProfe(self, filtro):
        return [1,2,3]
