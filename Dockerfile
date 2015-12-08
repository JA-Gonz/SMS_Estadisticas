FROM ubuntu
RUN apt-get install -y git  #Primero de todo instalamos git
RUN cd /home && git clone https://github.com/JA-Gonz/SMS_Estadisticas
RUN cd /home/SMS_Estadisticas && chmod a+x docker_run.sh
RUN cd /home/SMS_Estadisticas/ && ./docker_run.sh
CMD cd /home/SMS_Estadisticas/SMS_Estadisticas/ &&  python main.py

