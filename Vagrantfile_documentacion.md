#Configuración de Vagrant

En éste despliegue, se ha usado [Azure](https://azure.microsoft.com/es-es/), un IaaS hecho por Microsoft.

Para poder usarlo, es necesario tener una suscripción. Es importante asegurarse de tener una. PAra ésta asignatura, se ha usado una de las suscripciones proporcionadas por el profesor para la misma, pero se pueden conseguir mediante pago, ofertas en la DreamSpark, pases de invitado o de prueba, etc.

Una vez tenemos la suscripción, crearemos los certificados.Lo haremos con las 3 órdenes que hay en el tutorial del [siguiente enlace](https://jujucharms.com/docs/stable/config-azure), apartado "Config Values". Concretamente:
```
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout azure.pem -out azure.pem
openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
chmod 600 azure.pem
```

Dentro de azure, nos logueamos en nuestra cuenta (en el [portal antiguo es más comodo](https://manage.windowsazure.com/)) -> Configuración -> Certificados de administración -> Cargar, y cargamos el archivo **.cer**

Hecho todo esto, ya podemos hacer el fichero de configuración. Escribimos la órden:

	Vagrant init

Aparecerá un fichero que retocaremos con las siguientes órdenes:

* config.vm.box = "azure" ==> Indicamos que la box de la máquina virtual es la de azure
* config.vm.network "public_network" ==> INdicamos que la máquina virtual tendrá una conexión pública
* azure.mgmt_certificate = File.expand_path("azure.pem") ==> Indicamos el nombre y ubicación del fichero donde se encuentra el certificado
* azure.mgmt_endpoint    = "https://management.core.windows.net" ==> Ubicación del portal de administración de la máquina
* azure.subscription_id = "3252f376-df66-4dae-b865-76048fcb3c63" ==> ID de la suscripción
* azure.vm_name     = "smsestadisticas" ==> NOmbre de la máquina virtual
* azure.cloud_service_name = 'smsestadisticas' ==> Nombre del servicio web en la nube
* azure.vm_image    = "b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB" ==> Imagen de SO que instalamos
* azure.vm_size     = "Small" ==> Tamaño de la máquina virtual
* config.vm.box_url = "https://github.com/msopentech/vagrant-azure/raw/master/dummy.box" ==> Configuración de la box utilizada
* azure.vm_user = "ja"  ==> Nombre de usuario de la máquina
* azure.vm_password = "12345678!Ab" ==> Contraseña de acceso para el usuario creado
* azure.vm_location = "Central US" ==> Ubicación de la máquina virtual
* azure.tcp_endpoints = '8080:80' ==> Redireccionamiento del puerto 80 al 8080 (donde en nuestro caso está escuchando el servidor)
* azure.ssh_port = "22" ==> Puerto para conexiones SSH

Hecho todo esto, configuramos por último:
	
* config.vm.synced_folder ".", "/vagrant",disabled: true ==> Evitamos que se sincronice el contenido local con el de la máquina que se acaba de crear
* config.ssh.username = 'ja'  ==> Usuario para la conexión SSH
* config.ssh.password = '12345678!Ab' ==> Clave para la conexión SSH

