#!/bin/bash

# Comenta que es lo que hace cada uno de los siguientes comandos

mkdir -p respaldo_sistema/configuracion # Crea un directorio con llamado "respaldo_sistema" y un subdirectorio adentro de este llamado "configuracion". La opción "-p" permite crear el directorio padre en caso de no existir, en nuestro caso se asegura de crear "respaldo_sistema"
mkdir -p python/scripts # Crea un directorio llamado "python" y un subdirectorio "scripts" dentro de este. La opción "-p" permite crear el directorio padre en caso de no existir, en nuestro caso se asegura de crear "python"

touch  respaldo_sistema/guia # Crea un archivo llamado "guia" dentro del directorio "respaldo_sistema"
touch  python/scripts/secuencia.data # Crea un archivo "secuencia.data" adentro de python/scripts/

cp -r /bin/* respaldo_sistema/programas/ # Copia todo lo que esté adentro de /bin/* de manera recursiva adentro del subdirectorio programas
cp /etc/X11/ respaldo_sistema/ # Copia lo que esté dentro de la carpeta etc/X11 a respaldo_sistema/

echo $USER # Imprime una línea de texto con el usuario actual
echo $HOME # Imprime una línea de texto mostrando la ruta de HOME

head -37 $HOME/.bashrc > PEGADO.txt # Lee las primeras 37 líneas del archivo .bashrc en el directorio "home" y lo manda al archivo "PEGADO.txt"
echo "#############################" >> PEGADO.txt # Anida ############################# al final del archivo "PEGADO.txt"
tail -37 $HOME/.bash_history >> PEGADO.txt # Lee las últimas 37 líneas del archivo .bash_history en el directorio "home" y lo anida al final del archivo "PEGADO.txt"

touch python/notas # Crea el archivo "notas" adentro del directorio "python"
touch respaldo_sistema/configuracion/guia # Genera el archivo "guia" adentro del subdirectorio "configuracion"

find /usr -perm 777 >> todos.prm # Busca adentro del directorio "/usr" (y adentro de sus subdirectorios) todos los archivos y directorios que tengan todos los permisos tanto para el dueño, el grupo y otros. Esta búsqueda la manda de forma no destructiva a un archivo llamado "todos.prm"
find /var -name *.tar >> all.compress # Busca adentro del directorio "/var" todos aquellos archivos que terminen en ".tar" y la manda de forma no destructiva a un archivo llamado "all.compress"

ls -laR /etc/* | grep daemon # Enlista los contenidos del directorio "/etc" y los directorios adentro de este, dando un formato largo (-l), sin ignorar aquellas entradas que comienzas con un punto (-a) y lo hace de manera recursiva (-R). Este enlistado lo filtra para que devuelva únicamente aquellos elementos que contengan la palabra "daemon"

grep -lri daemon /etc/* > Demonios # Devuelve los archivos que coincidan (-l) con el patrón "daemon" dentro del directorio "/etc/" sin considerar mayúsculas o minísculas (-i) y de manera recursiva (-r). Posteriormente lo manda de forma destructiva a un archivo llamado "Demonio"
find /etc/ -name *.conf >> Demonios # Realiza una busqueda de archivos cuyo nombre termine en ".conf" adentro del directorio "/etc/" y los manda de forma no destructiva al archivo "Demonios"

ps -ea -u $USER > Procesos.txt # Devuelve todos los procesos (-e) del usuario actual (-u) (también aquellos que no esten asociados a la terminal "-a") y los manda de forma destructiva a un archivo llamado "Procesos.txt"

tar -cvf respaldo_sistema # El comando "tar -cvf [nombre_archivo] [directorio de creación] " crea un archivo "tar". Sin embargo, la sintaxis del comando anterior está incompleta, por tanto no hará nada.exit




