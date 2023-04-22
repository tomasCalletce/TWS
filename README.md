# TWS

## i. Introducción
Los servidores son la base de las telecomunicaciones en el mundo. Es importante tener un lugar que almacena y maneja protocolos de comunicación. En la capa de aplicación, hay múltiples protocolos que satisfacen diversas funcionalidades. Hay servidores que manejan protocolos de asignación de IPs dinámicas como DHCP; envio de archivos, FTP, SFTP; entre otras. 


A continuación, se desarrolló un socket para recibir solicitudes de dispositivos finales utilizando el protocolo de capa de aplicación llamado HTTP. Este protocolo es de los más usados en la capa de aplicación y utiliza el protocolo de transporte llamado TCP. En la capa de transporte existen principalmente, 2 protocolos: TCP(Socket_Stream) Transmission Control Protocol y UDP(Datagram) User Datagram Protocol. No entraremos en mas detalle sobre este tipo de protocolos. 


 En este repositorio, se presenta un sencillo servidor web que soporta los tipos de solicitud GET, POST y HEAD. Este servidor está desplegado en Amazon Web Services(AWS) utilizando el servicio EC2 de desplegar un servidor virtual.



## ii. Desarrollo: 
Conforme a las instrucciones del proyecto, este código no utiliza librerías externas aparte de sys, os, time, socket y thread. El código se organiza en tres partes principales: 


main.py: En este archivo, se asigna el puerto al que se va a escuchar y se escribe el código que crea un nuevo thread por cada nueva solicitud. 

Para empezar, se define el socket que se va a utilizar. Se define el tipo de IPs que soportará con el socket.AF_INET y el protocolo de transporte que va a soportar, en este caso, TCP(socket.SOCK_STREAM)

Se define el puerto y el host HOST y el puerto PORT y se empiezan a recibir solicitudes.

Cada vez que se recibe una solicitud, se maneja la solicitud utilizando la librería threading para manejar las solicitudes de manera concurrente utilizando el paralelismo. A continuación se entrará en mas detalle a la estructura del código y cómo se puede interactuar con el servidor desplegado. 

handler.py: Este archivo se encarga de filtrar las peticiones para ser procesadas en los sub manejadores, estos se ocupan de procesar un tipo de solicitud específica como GET o POST. También se encarga de recibir la solicitud procesada y enviar la respuesta. 

GET: 
/page_one -> página con una imagen 

/page_two -> página con múltiples imágenes

 /page_three -> página con una descarga de un archivo grande 

/page_four -> página con una descarga de un archivo grande y múltiples imágenes /image_user_one -> imagen del usuario 1 

/image_user_two -> imagen del usuario 2 

/bigfile -> documento .txt de más de 1 MB 


<-----IP PÚBLICA------>
http://3.19.26.168/


POST:

/createUser -> punto final para crear un usuario. Asegúrese de enviar el cuerpo con la siguiente información:
 { "Nombre": <nombre del usuario> }

 HEAD 
/image_user_one -> verificar la existencia de este archivo en el servidor

/image_user_two -> verificar la existencia de este archivo en el servidor 



<tipo de petición>handler.py: Estos archivos se encargan del procesamiento de cada tipo de solicitud. En el repositorio, existen tres de estos archivos, cada uno responsable de procesar las solicitudes GET, POST y HEAD. 

## iii. Conclusiones 
Despues de hace este proyecto, se pudo entender como realmente funcionan los servidores utilizando el protocolo de comunicación a nivel de Aplicación, HTTP. También entendimos la base de las telecomunicaciones(socket) y se implementó con la librería socket. Entender este nuevo concepto, es muy importante para darse cuenta de cómo funciona no solo para saber las herramientas que uno utiliza en el día a día sino que para poder hacer futuros proyectos en ésta área.

Amazon Web Services es una muy buena herramienta para desplegar servidores de una manera económica. Es importante conocer y saber esta herramienta para poder desplegar las futuras aplicaciones que uno vaya a realizar. 
 También fue super interesante ver cómo realmente funciona un servidor web porque hasta la fecha solo habían usando librerías como flash o express.

## iv. Referencias 
1.https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
2.GPT4 



