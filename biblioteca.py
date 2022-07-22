from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask (__name__)

livros = []
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

@app.route("/acesso", methods=['POST'])
def acesso():
    entrar = request.json
    for entrar in Leitor:
        if entrar["rg"] == entrar["rg"] and entrar["senha"] == entrar["senha"]:
            return{"Acesso":"Liberado."}
        else:
            return{"Erro.":"Usuario ou Senha Incorretos."}

@app.route("/cadastrar/livros", methods=['POST'])
def livro():
    livros_registro = request.json 
    for user in livros:
        if user["nome_livro"] == livros_registro["nome_livro"]:  
            return {"Algo deu errado.":"Esse nome_livro ja existe."}
    livros_registro = {
        "id": str(uuid.uuid4()),
        "nome_livro": livros_registro["nome_livro"]
        }
    livros.append(livros_registro)
    return jsonify(livros_registro) 

@app.route("/leitores")
def todos_leitores():
    return jsonify(Leitor)

@app.route("/livros")
def todos_livros():
    return jsonify(livros)

@app.route("/livros/leitores")
def livros_e_leitores():
    return jsonify(livros,Leitor)
