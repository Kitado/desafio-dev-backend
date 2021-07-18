from .utils import *
from .database import Database
from flask_restful import Resource
from flask import request


class Advanced(Resource):
    
    @staticmethod
    def get():
        args = request.args.to_dict()
        
        if "total_days" not in args or "profissao" not in args:
            return "É preciso especificar total_days e profissao!", 400
        
        db = Database()
        result = db.read(args["profissao"].title())
        
        if not result:
            return "Não foi achada nenhum registro de profissão com esse nome!", 400        
        
        try:
            total_days = int(args["total_days"])
        except:
            return "É preciso passar valores numéricos em total_days!", 400
        
        busday_gain = calculate_gain(total_days, result["valor_diario"])
        return f"Como {args['profissao']} você ganhará um total de R${busday_gain}, caso comece a trabalhar amanhã", 200
    
    @staticmethod
    def post():
        args = request.get_json()
        
        if "valor_diario" not in args or "profissao" not in args:
            return "É preciso especificar valor_diario e profissao!", 400
        
        try:
            valor_diario = float(args["valor_diario"])
        except:
            return "É preciso passar valores numéricos em valor_diario!", 400
        
        db = Database()
        response = db.register(args["profissao"].title(), valor_diario)
        
        return response
    