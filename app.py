from api.basic import Basic
from api.advanced import Advanced
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Basic, "/api/basic")
api.add_resource(Advanced, "/api/advanced")

app.run(debug=True)
