from fabric.api import *

def info_servidor():
    run ('uname -s')

def descargar():
    run ('rm -rf SMS_Estadisticas')
    run ('rm -rf google_appengine')
    run ('git clone https://github.com/JA-Gonz/SMS_Estadisticas.git')
    run ('wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.32.zip')
    run ('unzip google_appengine_1.9.32.zip')
    run ('rm -rf unzip google_appengine_1.9.32.zip')

def actualizar():
    run ('cd SMS_Estadisticas')
    run ('sudo git pull')

def iniciar():
    run ('sudo python google_appengine/dev_appserver.py --port=80 --host=0.0.0.0 SMS_Estadisticas/SMS_Estadisticas &')

def detener():
    run ('kill -9 $(pidof python)')

def borrar():
    run ('rm -rf SMS_Estadisticas')

def testear():
    run ('cd SMS_Estadisticas && make test')

def instalar():
    run ('cd SMS_Estadisticas && make install')
