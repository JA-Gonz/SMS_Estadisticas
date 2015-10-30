install:
	sudo apt-get update
	#mysql -u root < CrearBD_Estadisticas.sql # Más adelante, cuando las API's estén listas, se hará por BD. En esta primera entrega, los datos se devolverán mediante listas.
	pip install -r requirements.txt
	#Algunos paquetes no son utilizados ahora, pero si que serán utilizados a posteriori
test:

	cd SMS_Estadisticas
	nosetests test_mediante_sure.py