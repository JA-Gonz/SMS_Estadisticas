import datetime
import jinja2
import os
import webapp2
import cgi
import re


plantilla_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class PaginaConfigurarEstadisticas:

    def get(self):
        plantilla=plantilla_env.get_template('plantilla/configurar_estadisticas.html')
    	self.response.out.write(plantilla.render())

class PaginaExitoConfigurarEstadisticas:
    def get(self):
        plantilla=plantilla_env.get_template('plantilla/configurar_estadisticas_exito.html')
        self.response.out.write(plantilla.render())
def aplicacion():
    return  webapp2.WSGIApplication([
                                      ('/configurar_estadisticas',PaginaConfigurarEstadisticas),
                                      ('/configurar_estadisticas_exito',PaginaExitoConfigurarEstadisticas)
					], debug=True)
