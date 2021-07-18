from .utils import *
from flask_restful import Resource
from flask import request

class Basic(Resource):
    
    @staticmethod
    def get():
        args = request.args.to_dict()
        if "total_days" not in args or "gain_per_day" not in args:
            return "É preciso especificar total_days e gain_per_day!", 400
        
        try:
            total_days = int(args["total_days"])
            gain_per_day = float(args["gain_per_day"])
        except:
            return "É preciso passar valores numéricos em total_days e gain_per_day!", 400
        
        busday_gain = calculate_gain(total_days, gain_per_day)
        return f"Você ganhará um total de R${busday_gain}, caso comece a trabalhar amanhã", 200