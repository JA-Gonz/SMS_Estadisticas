#!/bin/bash

apt-get -y update
apt-get install -y python-pip
apt-get install -y python-software-properties #Necesario para que funciones add-adpt-repository
apt-get install build-essential
make install
