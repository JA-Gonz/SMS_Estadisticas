install:
	sudo apt-get update
	#mysql -u root < CrearBD_Estadisticas.sql # Más adelante, cuando las API's estén listas, se hará por BD. En esta primera entrega, los datos se devolverán mediante listas.
	sudo pip install -r requirements.txt
	#Algunos paquetes no son utilizados ahora, pero si que serán utilizados a posteriori
	sudo pip install ansible
	sudo pip --upgrade ansible
	wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
	sudo dpkg -i vagrant_1.8.1_x86_64.deb
	sudo vagrant plugin install vagrant-azure
	sudo apt-get install fabric
test:
	nosetests SMS_Estadisticas/test_mediante_sure.py

desplegar:
	vagrant up --provider=azure
