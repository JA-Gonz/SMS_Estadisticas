![]https://travis-ci.org/JA-Gonz/SMS_Estadisticas.svg?branch=master
#Subproyecto parte de SMS: StudentsManagementSystem

Este README parte de la descripción dada en el [fichero del proyecto SMS](https://github.com/ButterFlyDevs/StudentsManagementSystem/blob/master/README.md), donde se explica la motivación y a lo que se dedicará el rpoyecto en general. 

Como resumen, se repite que este proyecto se ha elegido por petición por parte de algunos profesores de un sistema capaz de dar apoyo en las labores del profesorado, en la etapa de enseñanza primaria, secundaria y bachillerato. Brindará soporte y agilizará las tareas de los docentes en el día a día en las aulas (pudiendose implementar gestiones de partes de incidencias de comportamiento, asistencia a clase, calificaciones, comunicación con los padres e interna entre personal del centro, etc.)

Además, proyecto se presentará al Certamen de proyectos de la UGR organizado por la Oficina de Software Libre.

Probando

Definida en dicho [README](https://github.com/ButterFlyDevs/StudentsManagementSystem/blob/master/README.md) que la arquitectura del proyeto serán algunas máquinas, en este proyecto en concreto se creará toda la infraestructura necesaria para la **máquina estadística**, incluyendo base de datos, triggers, API's de consulta de los datos, y la propia base de datos en sí. También la interfaz web necesaria para configurar estas estadísticas.

## Herramientas utilizadas y estructura en la nube


- Se usará webapp2 para crear la aplicación web que servirá para consultar y configurar las estadísticas. 
- 
- Se usará Ansible para manejar las máquinas en su fase de despliegue. Ansible tendrá un playbook que será ejecutado automáticamente dentro del script de despliegue automático, que levantará las dos máquinas, y les dará las primeras instrucciones (que serán descargar los scripts de aprovisionamiento para poder empezar a funcionar).

- Los scripts de despliegue y de aprovisionamiento se escribirán en un fichero .sh, que podrá ser ejecutado en una máquina Linux

- El testeo y pruebas se realizarán usando unittest, un framework de pruebas para Python

- El alojamiento de la máquina en un principio será en Azure

- 	Para el diseño de la aplicación web, se usará como Framework de CSS **UIKit**

NOTA: La aplicación, originalmente, se desarrollará en GoogleApEngine, pero realizaremos modificaciones oportunas en el código para poder hacer el despliegue en estas máquinas y sin utilizar la infraestructura de Google.

