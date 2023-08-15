# agent-spam-detector
  Este proyecto se trata de un agente detector de correos electrónicos clasificados como spam o no deseados en tiempo real en el servicio
  de correo electrónico Zimbra, en dónde se aplica aprendizaje automático(machine learning) para la detección, en compañía con un conjunto
  de datos etiquetados como ham y spam, contando con alrededor de 45k de correos electrónicos de ejemplo.

  Para poder ejecutar este proyecto, deberás usar la versión 3 de python e instalar las siguientes librerías:
```bash
pip3 install setuptools_rust
pip3 install cryptography==40.0.2
pip3 install mail-parser==3.15.0
pip3 install pandas==1.1.5
pip3 install PyJWT==1.4.2
pip3 install pymongo==4.1.1
pip3 install secure-smtplib==0.1.1
pip3 install scikit-learn==0.24.2
pip3 install watchdog==2.2.1
```

Cabe recalcar que las versiones instaladas pueden variar dependiendo el sistema operativo, en este caso, el backend desarrollado estaba en el SO Centos 7, por lo que las últimas versiones disponibles son las mencionadas previamente.

Para poder ejecutar el proyecto, deberás modificar el archivo [`config.py`](config.py), asegurandote de seguir las instrucciones dentro del archivo para poder crear las claves correctamente.

Antes de ejecutar el proyecto, es necesario entrenar el algoritmo Random Frest, que se encuentra en el archivo  [`trainning.py`](modules/machine/trainning/trainning.py), puede
entrenar el algoritmo entrando a la ruta modules/machine/trainning/ y ejecutar el comando ```bash trainning.py ```.
Cabe recalcar que este proyecto deberá estar en el servidor de correo electrónico Zimbra, independientemente ser SO que se esté usando,
pero durante la fase de desarrollo se hizo la prueba en el SO Centos 7.
Esl proceso de entrenamiento puede variar dependiendo de los recursos de su servidor, por ejemplo con 2GB de Ram en un SO virtualizado, el aproximado
es de 8 minutos, mientras que con 16 puede tardar 3 minutos aproximadamente.
Para ello deberá de modificar bien las rutas que se encuentra en el archivo [`trainning.py`](modules/machine/trainning/trainning.py) y [`prediction.py`](modules/machine/prediction/prediction.py)

Posteriormente, ejecutar el comando python3 main.py para la ejecución del proyecto.
