from items import items, item

import os
import json
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class itemEncoder(json.JSONEncoder):
    def default(self, itms: items) -> str:
            return itms.toJson()
    
class itemDecoder(json.JSONDecoder):
     def default(self, itms: str) -> items:
          return 

class itemsApi(Resource):

    @app.route('/itemsApi', methods=['GET'])
    def get():

        d = open(os.getcwd() + "/choose_an_adventure/items.json", "r")
        # t = d.read()
        # d.close()
        # return t

    # @app.route('/itemsApi/', methods=['POST'])
    # def post(self):
    #     s = request.get_json(force=True)
    #     d = open("/Users/jim/Repos/jim-roton/Python/api_example/data.json", "w")
    #     d.write(json.dumps(s, cls=itmeEncoder))
    #     d.close()
    #     return "True"

    # def __loadItems__(self) -> items:
    #     jsonItems: str = ""

        #  file = open("/Users/jim/Repos/jim-roton/Python/choose_an_adventure/items.json", "w")

api.add_resource(itemsApi, '/itemsApi')

if (__name__ == "__main__"):
    app.run(port=5001, debug=True, )