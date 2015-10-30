# -*- coding: utf-8 -*-

#Clase que devuelve los datos que necesita las funciones de estadísticas para funcionar
#(Alumnos, profes, faltas, etc.).
# En una primera arpoximación, se hará con listas, pero más adelante

class RecolectorDatos:

    #Función que devolverá a los alumnos
    @classmethod
    def obtenerAlumnos(self, filtro):   # Poh ahora no se usa el filtro
        alumnos = []
        for i in range (1,5):
            alumno = [i,"Pepe" + str(i), "Granada"]
            alumnos.append(alumno)
        print alumnos
        return alumnos

    #Funcion que devuelve los profesores
    @classmethod
    def obtenerProfes(self, filtro):    # Por ahora no se usa el filtro
        profesores= [[1,"El bonachon", 27, "Granada"],[2,"El Galletas", 35, "Almeria"],[3,"Don Cabron", 56, "Valencia"]]
        print profesores
        return profesores
    @classmethod
    def obtenerNotas(self, filtro): #Estructura: {id profesor, id alumno, nota}
        notas = [ [1,1,9], [1,2,8], [1,3,7],[1,4,9],[1,5,5],[2,1,6],[2,2,7],[2,3,5],
                [2,4,8],[2,5,3],[3,1,2],[3,2,3],[3,3,5],[3,4,4],[3,5,1]]
        return notas

    @classmethod
    def obtenerPartes(self, filtro):    #Estructura: {id profesor, id alumno}
        partes = [{2,3}, {2,3}, {2,1}, {3,1}, {3,2}]
        #return partes

        return partes
