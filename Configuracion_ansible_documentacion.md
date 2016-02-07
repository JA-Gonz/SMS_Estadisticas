#Configuración de Ansible

En este punto de la ejecución del archivo Vagrantfile, hay variables que ya ha tomado, como la configuración de conexión SSH. Quedan algunas pinceladas más:

* hosts: default ==> Servidor en el que se harán las órdenes. Se pone por defecto
* sudo:Yes ==>ÓRdenes como sudo
* remote_user ==> Usuario remoto con el que se ejecutarán las órdenes
* tasks: ==> Tareas a ejecutar
* name:NOmbre de la tarea a ejecutar
* apt / shell ==> Ejecuta con apt para descargar dependencias / Ejecuta la órden