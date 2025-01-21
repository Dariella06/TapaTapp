from flask import Flask, request, jsonify

app = Flask(__name__)

# Dades d'exemple per diferents categories
categories_data = {
    "animals": ["gat", "gos", "elefant"],
    "fruites": ["poma", "plàtan", "maduixa"],
    "colors": ["vermell", "blau", "groc"]
}

@app.route('/dam1', methods=['GET'])
def dam1():
    nom = request.args.get('nom', default=None, type=str)
    return jsonify(nom)


@app.route('/llista', methods=['GET'])
def obtenir_llista():
    # Obtenir el paràmetre 'categoria' de la URL
    categoria = request.args.get('categoria', default=None, type=str)
   
    if not categoria:
        return jsonify({"error": "El paràmetre 'categoria' és obligatori."}), 400
   
    # Obtenir les dades per a la categoria proporcionada
    result = categories_data.get(categoria.lower())
   
    if not result:
        return jsonify({"error": f"No hi ha dades per a la categoria '{categoria}'."}), 404
   
    # Retornar el resultat com a JSON
    return jsonify({"categoria": categoria, "elements": result})

@app.route('/api/dades', methods=['POST'])
def rebre_dades():
    # Obtenir les dades enviades en format JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "No s'han enviat dades"}), 400

    # Accedir a les dades específiques del JSON
    nom = data.get("nom", "Desconegut")
    edat = data.get("edat", "No especificada")
    ciutat = data.get("ciutat", "No especificada")

    # Processar les dades i retornar una resposta
    resposta = {
        "status": "success",
        "message": f"Dades rebudes per {nom}",
        "dades_rebudes": {
            "nom": nom,
            "edat": edat,
            "ciutat": ciutat
        }
    }
    return jsonify(resposta), 201  # Codi HTTP 201: Recurs creat

@app.route('/', methods=['GET'])
def servei_actiu():                                                                                                                                                        
    return jsonify({"status": f"Servei Actiu"}),

if __name__ == '__main__':
    app.run(debug=True)
