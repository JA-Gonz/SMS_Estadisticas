
#Subproyecto parte de SMS: StudentsManagementSystem

Este README parte de la descripción dada en el [fichero del proyecto SMS](https://github.com/ButterFlyDevs/StudentsManagementSystem/blob/master/README.md), donde se explica la motivación y a lo que se dedicará el rpoyecto en general. 

Como resumen, se repite que este proyecto se ha elegido por petición por parte de algunos profesores de un sistema capaz de dar apoyo en las labores del profesorado, en la etapa de enseñanza primaria, secundaria y bachillerato. Brindará soporte y agilizará las tareas de los docentes en el día a día en las aulas (pudiendose implementar gestiones de partes de incidencias de comportamiento, asistencia a clase, calificaciones, comunicación con los padres e interna entre personal del centro, etc.)

Además, proyecto se presentará al Certamen de proyectos de la UGR organizado por la Oficina de Software Libre.

Probando

Definida en dicho [README](https://github.com/ButterFlyDevs/StudentsManagementSystem/blob/master/README.md) que la arquitectura del proyeto serán 4 (o 5) máquinas totales (balanceador, servidor 1 y 2, base de datos y réplica de la base de datos), en este subproyecto se trabajará con el **balanceador y las máquinas servidoras**

## Herramientas utilizadas y estructura en la nube

- Para el balanceador, se usará **Nginx** como software balanceador de carga (en un principio). 

- Se usará webapp2 para crear la aplicación web que tendrán los servidores.
- 
- Se usará Ansible para manejar las máquinas en su fase de despliegue. Ansible tendrá un playbook que será ejecutado automáticamente dentro del script de despliegue automático, que levantará las dos máquinas, y les dará las primeras instrucciones (que serán descargar los scripts de aprovisionamiento para poder empezar a funcionar).

- Los scripts de despliegue y de aprovisionamiento se escribirán en un fichero .sh, que podrá ser ejecutado en una máquina Linux

- El testeo y pruebas se realizará mediante Docker, y las pruebas se prepararán en uno o varios Dockerfile.

- Todas las máquinas serán alojadas en un principio en Azure.

- 	Para el diseño de la aplicación web, se usará como Framework de CSS **UIKit**

NOTA: La aplicación, originalmente, se desarrollará en GoogleApEngine, pero realizaremos modificaciones oportunas en el código para poder hacer el despliegue en estas máquinas y sin utilizar la infraestructura de Google.

