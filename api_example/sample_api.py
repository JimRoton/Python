from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class item:

    def __init__(self, item_name: str, item_damage: int) -> None:
        self.name = item_name
        self.damage = item_damage

    def to_json(self):
        return {"name": self.name, "damage": self.damage}

class itmeEncoder(json.JSONEncoder):
    def default(self, itm: item):
            return itm.to_json()

class sample_api(Resource):
    @app.route('/sample_api', methods=['GET'])
    def get():
        d = open("/Users/jim/Repos/jim-roton/Python/api_example/data.json", "r")
        t = d.read()
        d.close()
        return t

    @app.route('/sample_api/', methods=['POST'])
    def post(self):
        s = request.get_json(force=True)
        d = open("/Users/jim/Repos/jim-roton/Python/api_example/data.json", "w")
        d.write(json.dumps(s, cls=itmeEncoder))
        d.close()
        return "True"

api.add_resource(sample_api, '/sample_api')

if (__name__ == "__main__"):
    app.run(port=5001, debug=True, )