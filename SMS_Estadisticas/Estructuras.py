# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

class BD_PorcentajeSuspensosProfes(ndb.Model):

    id_profe = ndb.IntegerProperty()
    porcentaje = ndb.FloatProperty()
    fecha = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def estadisticas_guardadas(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.fecha)
