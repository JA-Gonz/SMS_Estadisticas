import sys

sys.path.insert(0, 'lib') #http://stackoverflow.com/questions/14638262/python-2-7-how-to-use-beautifulsoup-in-google-app-engine/14648038#14648038
import jinja2
import os
import webapp2
import cgi
import re
from Estadisticas import Estadisticas
from Estructuras import BD_PorcentajeSuspensosProfes
from google.appengine.ext import ndb
plantilla_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class PaginaGetEstadisticas(webapp2.RequestHandler):
    def get(self):
        plantilla = plantilla_env.get_template('plantilla/index.html')
        self.response.out.write(plantilla.render())
    def post(self):

        if (self.request.get('guardar')):
            #NDB
            porcentaje = BD_PorcentajeSuspensosProfes(parent = ndb.Key("Estadisticas_almacenadas","PorcentajeSuspensosProfe"),id_profe=1,porcentaje=0.5)
            porcentaje_key = porcentaje.put()
            #porcentaje = BD_PorcentajeSuspensosProfes(parent = ndb.Key("Estadisticas_almacenadas","PorcentajeSuspensosProfe"),1,0.5)
            #porcentaje.put()
            self.redirect('/configurar_estadisticas')
        if (self.request.get('ver_estadisticas')):
            ancestor_key = ndb.Key("Estadisticas_almacenadas","PorcentajeSuspensosProfe")
            estadisticas_suspensos_profes = BD_PorcentajeSuspensosProfes.estadisticas_guardadas(ancestor_key).fetch(20)
            for estadistica in estadisticas_suspensos_profes:
                #self.response.out.write('<blockquote>%s</blockquote>' %
                #                        cgi.escape(estadistica.id_profe))
                print estadistica.id_profe

            #self.redirect('/configurar_estadisticas')
        if not(self.request.get('orden')):
            plantilla = plantilla_env.get_template('plantilla/index.html')
            self.response.out.write(plantilla.render())

        else:
            string = "Orden no encontrada"
            if(self.request.get('orden')) =="obtenerPorcentajeSuspensosProfesores":
                string = str(Estadisticas.obtenerPorcentajeSuspensosProfesores("SinFiltros"))

            string = string +'<input type="submit" id="guardar" name="guardar" value="Guardar Estadisticas"></input> <input type="submit" name="ver_estadisticas" id="ver_estadisticas" value="Ver Estadisticas anteriores"></input>'
            templateVars = {"texto" : string}
            plantilla = plantilla_env.get_template('plantilla/index.html')
            self.response.out.write(plantilla.render(templateVars))


class PaginaConfigurarEstadisticas(webapp2.RequestHandler):

    def get(self):
        plantilla=plantilla_env.get_template('plantilla/configurar_estadisticas.html')
    	self.response.out.write(plantilla.render())

class PaginaExitoConfigurarEstadisticas(webapp2.RequestHandler):
    def get(self):
        plantilla=plantilla_env.get_template('plantilla/configurar_estadisticas_exito.html')
        self.response.out.write(plantilla.render())


aplicacion = webapp2.WSGIApplication([
                                      ('/configurar_estadisticas',PaginaConfigurarEstadisticas),
                                      ('/configurar_estadisticas_exito',PaginaExitoConfigurarEstadisticas),
                                      ('/',PaginaGetEstadisticas),
					], debug=True)




def main():
    #import fix_path
    #import lib
    #from lib import paste
    #from paste import httpserver
    #httpserver.serve(aplicacion, host='127.0.0.1', port='8080')
    aplicacion.run()
if __name__ == '__main__':
    main()
