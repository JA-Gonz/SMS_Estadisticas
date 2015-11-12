# -*- coding: utf-8 -*-
import unittest
import webapp2
import pasarelatest
from Estadisticas import Estadisticas
from RecolectorDatos import RecolectorDatos


class TestStringMethods(unittest.TestCase):
    #Probar que devuelve alumnos
    def test_getAlumnos(self):
        respuesta = RecolectorDatos.obtenerAlumnos("Sin filtro")
        self.assertTrue(len(respuesta)>0)
    #Probar que devuelve profesores
    def test_getProfesores(self):
        respuesta = RecolectorDatos.obtenerProfes("Sin filtro")
        self.assertTrue(len(respuesta)>0)
    #Probar que devuelve notas
    def test_getNotas(self):
        respuesta = RecolectorDatos.obtenerNotas("Sin filtro")
        self.assertTrue(len(respuesta)>0)
    #Probar que devuelve partes de incidencias
    def test_getPartes(self):
        respuesta = RecolectorDatos.obtenerPartes("Sin filtro")
        self.assertTrue(len(respuesta)>0)
    #Probar que devuelve ranking de profesores por porcentaje de suspensos
    def test_getRankingProfeSuspensos(self):
        respuesta = Estadisticas.obtenerPorcentajeSuspensosProfesores("Sin filtro")
        self.assertTrue(len(respuesta))

    #Probar que devuelve ranking de clases por falta de asistencia
    def test_getRankingClasesFaltas(self):
        respuesta = Estadisticas.obtenerRankingFaltasCurso("Sin filtro")
        self.assertTrue(len(respuesta))
    #Probar que devuelve ranking de clases por partes de incidencias
    def test_getRankigClasesPartes(self):
        respuesta = Estadisticas.obtenerRankingPartesCurso("Sin filtro")
        self.assertTrue(len(respuesta))
    #Probar que devuelve ranking de clases con mas nota media
    def test_getRankingClaseNotaMedia(self):
        respuesta = Estadisticas.obtenerRankingNotaMediaCurso("Sin Filtro")
        self.assertTrue(len(respuesta))
    #Probar que devuelve los alumnos que hay en el día
    def test_getAsistenciaTotal(self):
        respuesta = Estadisticas.obtenerAsistenciaTotalCentro("Sin filtro")
        self.assertTrue(len(respuesta))
    #Probar que devuelve ranking de profesores por partes de incidencias
    def test_getRankingProfePartes(self):
        respuesta = Estadisticas.obtenerRankingPartesProfe("Sin filtro")
        self.assertTrue(len(respuesta))
