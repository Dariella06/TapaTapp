# Què és una Response HTTP

Una **HTTP Response** (Resposta HTTP) és la resposta que el servidor envia al client després d'una petició HTTP (com ara una petició **GET** o **POST**). La resposta inclou informació sobre si la petició va ser processada correctament o si va ocórrer un error.

---

## Headers

Els **headers** són metadades que proporcionen informació addicional sobre la resposta, com el tipus de contingut, la longitud del contingut, etc. Alguns exemples de headers són:

- **Content-Type**: Indica el tipus de contingut de la resposta (per exemple, `text/html`, `application/json`, `image/jpeg`).
- **Content-Length**: Indica la mida del contingut en bytes.
- **Date**: La data i hora en què es va generar la resposta.
- **Server**: Informació sobre el servidor que ha generat la resposta.
- **Set-Cookie**: Si s'han establert cookies al client.

---

## Body

El **body** de la resposta conté les dades que el servidor vol enviar al client. El contingut del body depèn del tipus de petició i la resposta, i pot ser una pàgina web HTML, un document JSON, un fitxer d'imatge, etc.

### Tipus de contingut:
- **HTML**: En el cas de pàgines web, el cos serà el codi HTML.
- **JSON**: Quan s'està treballant amb **API RESTful**, el cos sovint serà un objecte o array **JSON**.
- **Binari**: Quan es carrega un fitxer, el cos contindrà les dades binàries d'aquest fitxer (per exemple, una imatge o un document).

# GET request
GET /index.html HTTP/1.1
Host: www.example.com

# POST request
POST /api/login HTTP/1.1
Host: www.example.com
Content-Type: application/json
Content-Length: 45

{
  "username": "usuari",
  "password": "1234"
}
### HTTP Response (Respuesta HTTP):
- **Código de estado**: Indica el resultado (ej. 200 OK o 404 Not Found).
- **Encabezados**: Información adicional sobre la respuesta.
- **Cuerpo**: Los datos solicitados (como HTML, JSON, etc.).

## Ejemplo_Response:
HTTP/1.1 200 OK
Content-Type: application/json

{"id":123, "nombre":"Producto"}


### Exemple de resposta JSON:
```json
{
  "status": "success",
  "message": "Data received successfully",
  "data": {
    "id": 123,
    "name": "Joan"
  }
}
