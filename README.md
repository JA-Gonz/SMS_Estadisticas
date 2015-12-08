[![](https://travis-ci.org/JA-Gonz/SMS_Estadisticas.svg?branch=master)](https://travis-ci.org/JA-Gonz/SMS_Estadisticas)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://smsestadisticas.herokuapp.com)
#Subproyecto parte de SMS: StudentsManagementSystem

Este README parte de la descripción dada en el [fichero del proyecto SMS](https://github.com/ButterFlyDevs/StudentsManagementSystem/blob/master/README.md), donde se explica la motivación y a lo que se dedicará el rpoyecto en general. 

Como resumen, se repite que este proyecto se ha elegido por petición por parte de algunos profesores de un sistema capaz de dar apoyo en las labores del profesorado, en la etapa de enseñanza primaria, secundaria y bachillerato. Brindará soporte y agilizará las tareas de los docentes en el día a día en las aulas (pudiendose implementar gestiones de partes de incidencias de comportamiento, asistencia a clase, calificaciones, comunicación con los padres e interna entre personal del centro, etc.)

Además, proyecto se presentará al Certamen de proyectos de la UGR organizado por la Oficina de Software Libre.

Probando

Definida en dicho [README](https://github.com/ButterFlyDevs/StudentsManagementSystem/blob/master/README.md) que la arquitectura del proyeto serán algunas máquinas, en este proyecto en concreto se creará toda la infraestructura necesaria para la **máquina estadística**, incluyendo base de datos, triggers, API's de consulta de los datos, y la propia base de datos en sí. También la interfaz web necesaria para configurar estas estadísticas.

## Herramientas utilizadas y estructura en la nube


- Se usará webapp2 para crear la aplicación web que servirá para consultar y configurar las estadísticas. 
- Se usará Ansible para manejar las máquinas en su fase de despliegue. Ansible tendrá un playbook que será ejecutado automáticamente dentro del script de despliegue automático, que levantará las dos máquinas, y les dará las primeras instrucciones (que serán descargar los scripts de aprovisionamiento para poder empezar a funcionar).

- Los scripts de despliegue y de aprovisionamiento se escribirán en un fichero .sh, que podrá ser ejecutado en una máquina Linux

- El testeo y pruebas se realizarán usando unittest, un framework de pruebas para Python

- El alojamiento de la máquina en un principio será en Azure

- 	Para el diseño de la aplicación web, se usará como Framework de CSS **UIKit**

NOTA: La aplicación, originalmente, se desarrollará en GoogleApEngine, pero realizaremos modificaciones oportunas en el código para poder hacer el despliegue en estas máquinas y sin utilizar la infraestructura de Google.


## Segundo hito de la práctica

Como anotación, aunque no tenga que ver con el hito en sí, se ha renombrado tanto el repositorio como el README, además de cambiar el enfoque del proyecto. Ahora el proyecto tratará de crear una base de datos de estadísticas, que cogerá los datos de la base de datos del compañero, para elaborar una serie de funciones que establezcan relaciones entre los datos, y pueda ser usadas en el proyecto principal (quien es el profesor con más porcentaje de suspensos, cuál es la clase con más porcentaje de faltas o partes de incidencias, etc.)

##### Configuración correcta de herramientas de construcción.

Se ha optado por hacer un archivo [Makefile](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/Makefile) que se encarga tanto de testear el proyecto, como de instalarlo. Las órdenes respectivamente son **make test** y **make install**.

Para el testeo de la prueba, se utiliza [sure](https://pypi.python.org/pypi/sure), un paquete destinado al testeo de aplicaciones Python. Se podría haber hecho el desarrollo de la aplicación en otro lenguaje, pero como el proyecto principal y el otro subproyectoestarán hechos con Python, creí conveniente seguir usando el mismo lenguaje (además, en los ejercicios utilicé Python, así que no tenía más que replicar los pasos de los ejercicios, pero en el proyecto). También, tengo pensado crear un apartado web de configuración de las estadísticas (de ahí la carpeta [plantilla](https://github.com/JA-Gonz/SMS_Estadisticas/tree/master/SMS_Estadisticas/plantilla), y que use el archivo [pasarelatest](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/SMS_Estadisticas/pasarelatest.py) para que el test principal pueda usar las funciones de webapp2).

Este paquete es de funcionamiento simple: busca todas las funciones que comiencen por **test_** definidas en la clase del [archivo .py](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/SMS_Estadisticas/test_mediante_sure.py) que se pasa como parámetro, y las ejecuta. Dentro de dichas funciones, hacemos llamdas a otras funciones de la aplicación, y se comprueba si la salida de las mismas son como deberían de ser.

El test se lanza mediante [nose](https://nose.readthedocs.org/en/latest/), otro paquete que complementa a las funciones de [unittest](https://docs.python.org/2/library/unittest.html). En realidad, tan solo con unittest es necesario para poder ejecutar el test, pero sure aporta facilidad al testeo(no necesitamos llamar explícitamente a las funciones de testeo, él lo hace solo), estando un poco a más alto nivel.

Para definir todas las dependencias de instalación, se usa el archivo [requirements.txt](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/requirements.txt), el cuál usará el makefile para intentar resolver.

##### Integración continua funcionando.

Se ha usado Travis para agilizar la integración continua en el proyecto (de hecho, el estado de erróneo o de éxito del proyecto en un momento determinado, aparece en la primera imagen de éste Readme).

Al darme de alta en Travis mediante GitHub, y enlazar este repositorio a Travis, éste se quedará "esperando" nuevos push para ponerse a testear el proyecto, y comprobar si las actualizaciones conducen a un estado exitoso. Para que Travis pueda hacer esto, se necesita configurar en el repositorio el archivo [.travis.yml](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/.travis.yml), donde básicamente se esepcifica que instale las dependencias y ejecute el script de testeo.

##### Tests significativos y/o avance del proyecto en sí más allá de lo básico.

Debido a la naturaleza del proyecto, necesito conectar a la base de datos del compañero para poder realizar funciones realmente útiles. Por ahora, el archivo [RecolectorDatos.py](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/SMS_Estadisticas/RecolectorDatos.py) devuelve listas inventadas, aunque ese mismo archivo será sobreescrito para que pueda conectar a la base de datos del compañero y traer datos reales.

El archivo [Estadisticas.py](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/SMS_Estadisticas/Estadisticas.py) se encarga de la logística de las operaciones de estadística, llamando a RecolectorDatos para servirse de la información necesaria para funcionar. Por ahora, todas las funciones devuelven datos de prueba para que pase los tests, aunque la función que se encarga de calcular el **porcentaje de suspensos de cada profesor** si está implementada y funciona correctamente.

#Despliegue en PaaS

Llegados a este punto de desarrollo del proyecto, hay que remarcar que en realidad, este proyecto al ser parte de un proyecto mayor, no tiene interfaz de usuario como tal. Dicho de otra forma: este proyecto es un **micro-servicio** de otro mayor. Y aunque en el segundo hito se comentara que se iba a hacer un apartado de configuración de las Estadísticas (quizás la única parte con interfaz de usuario), al final se decidió no hacerlo. En su lugar, se dotará a la API de funciones que leerán datos pasados desde la página web, y configurará las estadísticas en función de esos parámetros (aunque las opciones de configuración no serán complicadas, ya que por la naturaleza del proyecto, quizás lo más interesante a configurar sea la frecuencia en tiempo con la que se "refrescan" las estadísticas, y poco más).

Por todo esto, se ha creado una "interfaz de usuario" mínima, donde hay un formulario con 3 elementos: campo de entrada, botón, y área de texto. En el campo de entrada, se pone el nombre de la función estadística que se desea ejecutar, y tras enviarla con el botón, aparecerá a la derecha la salida de la función. Esa salida será la que reciba bien otro micro servicio "parseador" que trate esos datos, o bien la propia interfaz web, y ya se encargará de leer y colocar en la vista de la página para el usuario (aún está por ver).

Definida la interfaz web mínima necesaria para el proyecto, se ha decidido desplegarla en **Heroku**. La razón de por qué se ha escogido este PaaS, es la de poder incluir la configuración necesaria en un fichero [Procfile](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/Procfile), por que es compatible con el lenguaje de desarrollo del proyecto (en este caso, Python), también por que viendo la [documentación de Heroku sobre despliegues de aplicaciones Python](https://devcenter.heroku.com/articles/getting-started-with-python-o), hay bastantes ejemplos y ayuda que nos facilita el proceso, y por último, por que permite la conexión con GitHub para el auto-despliegue de la aplicación después de hacer "push" del código.

Se ha configurado Heroku de la siguiente forma:

1. Se ha creado el pipeline (en este caso, smsestadisticas), por si más adelante se decidiera incorporar mas microservicios dependientes de éste.
2. Se ha creado en GitHub una rama "desarrollo", que es en la que trabajaremos. Cuando queramos pasar cambios a producción, Heroku cogerá los datos automáticamente de la rama master, así que no tendremos más que subir nuestro código a dicha rama (de desarrollo a master),
3. Se han dejado las opciones por defecto de esperar por el CI (Travis en nuestro caso, para asegurarnos que el paso a producción es de una version al menos estable), y de auto-desplegar

Para usar la aplicación, simplemente seguimos el enlace de Heroku del principio del documento, y escribimos algunas de las órdenes que hay como ejemplo debajo del formulario.

Nota: He tenido que usar Gunicorn como servidor WSGI de Python, ya que según la documentación de Heroku, parece que es el único compatible. Buscando información por Internet, nos topamos con que no somos los únicos con este problema, y la solución pasa por Gunicorn (al menos la más fácil), tal y como se comenta [en esta pregunta de StackOverflow](http://stackoverflow.com/questions/17840120/how-to-run-webapp2appengine-in-heroku)

#Docker

En este punto de desarrollo del proyecto, se trabajará con Docker, para crear un contenedor que contendrá la aplicación en sí.

Primero, se han elaborado los correspondientes archivos [Dockerfile](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/Dockerfile) y [docker_run.sh](https://github.com/JA-Gonz/SMS_Estadisticas/blob/master/docker_run.sh) respectivamente.

El primero, incluye todas las órdenes que se ejecutarán dentro del contenedor una vez creado (es una especie de script de "despliegue" en el contenedor).

El segundo script es otro script de despliegue secundario, que también es necesario. En él se han introducido las instalaciones de todas las dependencias (requirements de pip para Python, aparte de la instalación de éste).

Antes de todo esto, hemos tenido que tocar el archivo de servidor (main.py) para que sirva en la dirección 0.0.0.0, el puerto lo seguimos manteniendo (8080).

Una vez tenemos todo creado en local, con docker:

	sudo docker build -t  jagonz/sms_estadisticas .
La direción DockerHub del repo con docker es [esta](https://hub.docker.com/r/jagonz/sms_estadisticas/), y para llegar a tenerla ahí, hemos hecho lo siguiente:

Primero, asignar el tag. Una vez tenemos el contenedor con docker puesto,asignamos su ID con el tag que nos da DockerHub una vez creado el repositorio. En nuestro caso:

	sudo docker tag c1aa0c0c874d /jagonz/sms_estadisticas
    
Después, configuramos docker login:

	sudo docker login --name=JAGonz --email=XXXX@XXXX.com
    
Una vez docker "sabe quienes somos", podemos hacer el push:

	sudo docker push jagonz/sms_estadisticas
    
Se subirá al repo la imagen creada, y tardará bastante.

Una vez acabe, podemos descargarla en nuestra máquina de Azure:

	$ sudo apt-get update
	$ sudo apt-get install -y docker.io
	$ sudo docker pull jagonz/sms_estadisticas
	$ sudo docker run -t -i jagonz/sms_estadisticas

Como tenemos el dockerfile y el docker_run configurado, todo se lanza automáticamente.

Podemos ver el resultado en la máquina Azure [en este enlace](smsestadisticas.cloudapp.net:8080)
    