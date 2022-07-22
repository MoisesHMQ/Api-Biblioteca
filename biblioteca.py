from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask (__name__)

Leitor = []

@app.route("/cadastrar/leitores", methods=['POST'])
def leitores_cadastrar():
    registro = request.json 
    for user in Leitor:
        if user["rg"] == registro["rg"]:  
            return {"Errado.":"Rg ja existe."}
    registro = {
        "Nºcadastro": str(uuid.uuid4()),
        "rg": registro["rg"],
        "senha": registro["senha"]
        }
    Leitor.append(registro)
    return jsonify(registro)



