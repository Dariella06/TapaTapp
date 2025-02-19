# ¡Hola Mundo!

¡HELLOOOOOOOO! ¿Cómo estás?

[Descripció del Projecte TapatApp](archivo.md)

[Requeriments tècnics](tecnics.md)

[Http Response](Respons.md)

[Http Request](Request.md)

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


## Prototipo 1
[Diagrama](prototipo1/Prototip_1.mermaid)

### BackEdnd
[BackEnd](prototipo1/Backend.mermaid)

### FrontEdnd
[FrontEdnd](prototipo1/FrontEnd.mermaid)



## Prototipo 2
[Prototipo2](prototipo2/prototipo.md)

