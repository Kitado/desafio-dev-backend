from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json
import datetime
import calendar

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/db_blue365'

db = SQLAlchemy(app)

#model Usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    profissao = db.Column(db.String(50))
    valorDiario = db.Column(db.Float)
    quantidadeDias = db.Column(db.Integer)

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "profissao": self.profissao, "valorDiario": self.valorDiario, "quantidadeDias": self.quantidadeDias}

db.create_all()

def geraResponse(status, nomeDoConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeDoConteudo] = conteudo

    if(mensagem):
        body['mensagem'] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")

#listar todos usuarios
@app.route("/usuarios", methods=["GET"])
def getAllUsuarios():
    usuarios = Usuario.query.all()
    usuarios_json = [i.to_json() for i in usuarios]
    return geraResponse(200, "Usuarios cadastrados", usuarios_json, "ok")

#pesquisar usuario pelo id
@app.route("/usuarios/id/<id>", methods=["GET"])
def getUsuarioById(id):
    usuarios = Usuario.query.filter_by(id = id).first()
    usuario_json = usuarios.to_json()
    return geraResponse(200, "Usuario", usuario_json, "ok")

#cadastrar usuario
@app.route("/usuarios", methods=["POST"])
def cadastrarUsuario():
    body = request.get_json()
    try:
        usuario = Usuario(nome = body["nome"], email = body["email"], profissao = body["profissao"], valorDiario = body["valorDiario"], quantidadeDias = body["quantidadeDias"])
        db.session.add(usuario)
        db.session.commit()
        return geraResponse(201, "Usuario", usuario.to_json(), "Usuario criado com sucesso!")
    except Exception as e:
        print(e)
        return geraResponse(400, "", {}, "Erro ao cadastrar")

#atualizar cadastro de usuario pelo id
@app.route("/usuarios/id/<id>", methods=["PUT"])
def atualizarUsuario(id):
    usuario = Usuario.query.filter_by(id = id).first()
    body = request.get_json()
    try:
        if('nome' in body):
            usuario.nome = body["nome"]
        if('email' in body):
            usuario.email = body["email"]
        if('profissao' in body):
            usuario.profissao = body["profissao"]
        if('valorDiario' in body):
            usuario.valorDiario = body["valorDiario"]
        if('quantidadeDias' in body):
            usuario.quantidadeDias = body["quantidadeDias"]
        db.session.add(usuario)
        db.session.commit()
        return geraResponse(200, "Usuario", usuario.to_json(), "Usuario atualizado com sucesso!")
    except Exception as e:
        print(e)
        return geraResponse(400, "", {}, "Erro ao atualizar")

#excluir usuario pelo id
@app.route("/usuarios/id/<id>", methods=["DELETE"])
def deletarUsuario(id):
    usuario = Usuario.query.filter_by(id = id).first()
    try:
        db.session.delete(usuario)
        db.session.commit()
        return geraResponse(200, "Usuario", usuario.to_json(), "Usuario excluído com sucesso!")
    except Exception as e:
        print(e)
        return geraResponse(400, "", {}, "Erro ao excluir")

#cálculo de dias e valor retirado da parte 1
@app.route("/usuarios/valor/<id>", methods=["GET"])
def calcularValorTotal(id):
    usuario = Usuario.query.filter_by(id = id).first()
    
    dataAtual = str(datetime.date.today())
    dataAtual = dataAtual.split("-")
    dia = datetime.datetime(int(dataAtual[0]), int(dataAtual[1]), int(dataAtual[2]))

    somaDias = datetime.timedelta(days = 1)

    somaSalario = 0

    for i in range(usuario.quantidadeDias):
        if calendar.day_name[dia.weekday()] != "Saturday" and calendar.day_name[dia.weekday()] != "Sunday":
            somaSalario += usuario.valorDiario
        dia += somaDias

    return "Valor total: R$" + str(somaSalario)

if __name__ == "__main__":
    app.run(debug=True)

