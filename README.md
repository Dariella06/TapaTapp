# ¡Hola Mundo!

¡HELLOOOOOOOO! ¿Cómo estás?

[Descripció del Projecte TapatApp](archivo.md)

[Requeriments tècnics](tecnics.md)

[Http Response](Respons.md)

[Http Request](Request.md)


## Prototipo 1

## Definició dels EndPoints del Servei Web:
Un endpoint d'un servei web és una URL que proporciona un punt d'accés a una funció o recurs específic del servei web. 

## Què necessitem per cada End-point
Necesitem un minim d'aquest recursos per poder fer el serveis web d'un EndPoint.

- **URL**: L'adreça per accedir-hi al codi.
- **Mètode HTTP**: GET, POST, PUT, DELETE.
- **Paràmetres de consulta o cos**: Dades que es necessiten per completar la sol·licitud del codi que has fet.
- **Resposta**: El resultat que retorna, normalment en format JSON.
- **Codi d'estat**: Indica si la petició ha sigut exitosa o ha fallat (**ex:** 200, 404).

Host: http://192.168.56.1:10050

## Taula de JSON 


| Descripció  | End-point     | Method     |Tipus de petició|Parametres|
| :---        |  :---        |  :---        |  :---         |  :---     |  
| Obtenim dades del usuari  | /Prototip_1/getuser|GET | application/json   |  UserName/Nom-String | 

Primer afegir tot el codi de la resposta posible json de sortida.
Si la petició és GET afegirem URL per provar totes les possibles sortides que tenim.

Resposta JSON per el Usuari ha trobat:  
Code Response Http: 200
<br/> Response Body:

{   "UserName": "Dariella",   "Email": "Dariella.Llosa.2006@gmail.com",
   "Id": 7,   "Password":  "2006" }

[Diagrama](prototipo1/Prototip_1.mermaid)

### BackEdnd
[BackEnd](prototipo1/Backend.mermaid)

### FrontEdnd
[FrontEdnd](prototipo1/FrontEnd.mermaid)

# Prototipo 2

## Wireframe de la App

Puedes ver el wireframe de la app:  
[Wireframe de la App](wireframe.mermaid)

## Descripció dels View:

#### Iniciar Sesión  
Accede ingresando tu nombre y correo.  

#### Lista de Niños  
Consulta los niños registrados con su nombre y apellido.  

#### Recuperar Contraseña  
Si la olvidaste, ingresa tu nombre y correo para recuperarla.  

#### Inicio del Usuario  
Al iniciar sesión, verás tu nombre y correo en tu perfil.  

#### Registro  
Si eres nuevo, crea tu cuenta con nombre, apellidos y correo.  

#### Menú del Niño  
Consulta el menú asignado a cada niño junto con su información básica.  

#### Información del Usuario  
Consulta o edita tu nombre, apellidos y correo cuando quieras.  

#### Código de Verificación  
Recibirás un código en tu correo para recuperar tu contraseña.  

#### Perfil  
Aquí puedes ver y actualizar tus datos personales.  

## Descripción de Implementación del Prototipo 2

En el Prototipo 2, he creado los wireframes para visualizar la estructura de la app, considerando las descripciones de usuarios, niños y sus servicios. 
Este prototipo nos permite analizar el estado del proyecto original y planificar el diseño y el flujo de la aplicación.

## Diagramas de la Arquitectura

### Diagrama FrontEnd  
Aquí está el enlace para ver el FrontEnd:  
[Diagrama de FrontEnd](frontend.mermaid)  

### Diagrama BackEnd  
Aquí está el enlace para ver el BackEnd:  
[Diagrama de BackEnd](backend.mermaid)  
