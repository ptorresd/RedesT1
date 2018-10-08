La tarea se realizó en python 3.6
Supuestos:
-El formato del json es como el que se adjunta con la entrega (ojo que dirección va con tilde)

-Al correr el cliente, si se le da un sólo argumento, entonces debe ser la ruta a un json

-Si hay mas de uno, se asume que se le entregarán todos los servidores en la misma línea, con el formato
que se muestra en el enunciado.

-Al establecer la conexión a un servidor, el servidor siempre enviará un mensaje de vuelta.

-La conexión a un servidor siempre será exitosa

-Si se usa el comando exit, se dejarán de enviar mensajes al servidor al que se le envió


Instrucciones para correr la tarea:

Para correr la tarea:
python3 Cliente.py data.json

python3 Cliente.py nombre_1 ip_1 puerto_1 ... nombre_n ip_n puerto_n

donde nombre_i es un string, ip_i es una dirección ip, puerto_n es un entero representando un puerto

Para ejecutar los comandos:
Se ingresan dos líneas.
La primera línea contiene el comando que se desea enviar
La segunda línea contiene los destinatarios, que puede ser all o una lista con todos
los nombres de los servidores a los que se le envía

Ejemplos:

ls
all

echo hola server
server1 nombre_servidor_cualquiera server5

exit
server3 server4
