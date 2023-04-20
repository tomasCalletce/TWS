# TWS

## i. Introducción
 En este repositorio, se presenta un sencillo servidor web que soporta los tipos de solicitud GET, POST y HEAD. 

GET: 
/page_one -> página con una imagen 
/page_two -> página con múltiples imágenes
 /page_three -> página con una descarga de un archivo grande 
/page_four -> página con una descarga de un archivo grande y múltiples imágenes /image_user_one -> imagen del usuario 1 
/image_user_two -> imagen del usuario 2 
/bigfile -> documento .txt de más de 1 MB 

POST:
/createUser -> punto final para crear un usuario. Asegúrese de enviar el cuerpo con la siguiente información:
 { "Nombre": <nombre del usuario> }

 HEAD 
/image_user_one -> verificar la existencia de este archivo en el servidor 
/image_user_two -> verificar la existencia de este archivo en el servidor 

## ii. Desarrollo: 
Conforme a las instrucciones del proyecto, este código no utiliza librerías externas aparte de sys, os, time, socket y thread. El código se organiza en tres partes principales: 

main.py: En este archivo, se asigna el puerto al que se va a escuchar y se escribe el código que crea un nuevo thread por cada nueva solicitud. 

handler.py: Este archivo se encarga de filtrar las peticiones para ser procesadas en los sub manejadores, estos se ocupan de procesar un tipo de solicitud específica como GET o POST. También se encarga de recibir la solicitud procesada y enviar la respuesta. 

<tipo de petición>handler.py: Estos archivos se encargan del procesamiento de cada tipo de solicitud. En el repositorio, existen tres de estos archivos, cada uno responsable de procesar las solicitudes GET, POST y HEAD. 

## iii. Conclusiones 
Estamos muy felices con los resultados del proyecto. logramos escribir código organizado y legible. También fue super interesante ver cómo realmente funciona un servidor web porque hasta la fecha solo habían usando librerías como flash o express.

## iv. Referencias 
1.https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
2.GPT4 
