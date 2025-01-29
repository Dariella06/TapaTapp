# ¡Hola Mundo!

¡HELLOOOOOOOO! ¿Cómo estás?

[Descripció del Projecte TapatApp](archivo.md)

[Requeriments tècnics](tecnics.md)

[Http Response](Respons.md)

[Http Request](Request.md)

## Definició dels EndPoints del Servei Web:
Un endpoint d'un servei web és una URL que proporciona un punt d'accés a una funció o recurs específic del servei web. 

## Què necessitem per cada End-point
- **URL/Path**: http://IP:PORT/la ruta d'accés
- **Mètode HTTP**: Existix 4 métodes: GET, POST, PUT, DELETE.
- **Paràmetres**: Es a dir les rutes dels comands ej: /api/aplicacions.
- **Codi d'estat HTTP**: l'estat de la sol·licitud: 200
- **Respostes**: Depén del codi la resposta et por donar Ex:
  self.id=id
        self.username=username
        self.password=password
        self.email=email

Host: http://192.168.56.1:10050

## Taula de JSON 


| Descripció  | End-point     | Method     |Tipus de petició|Parametres|
| :---        |  :---        |  :---        |  :---         |  :---     |  
| Obtenim dades del usuari  | /Prototip_1/getuser|GET | application/json   |  UserName/Nom-String | 

Primer afegir tot el codi de la resposta posible json de sortida.
Si la petició és GET afegirem URL per provar totes les possibles sortides que tenim.

Resposta JSON per el Usuari ha trobat:  
Code Response Http: 200
<br/> Response Body: ```{   "UserName": "Dariella",   "Email": "Dariella.Llosa.2006@gmail.com",   "Id": 7,   "Password":  "2006" }      |