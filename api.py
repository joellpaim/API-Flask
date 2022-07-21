from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


COUNTRIES = {
    '1': {'name': 'Austria', 'capital': 'Vienna'},
    '2': {'name': 'Bulgaria', 'capital': 'Sofia'},
    '3': {'name': 'Canada', 'capital': 'Ottawa'},
    '4': {'name': 'Denmark', 'capital': 'Copenhagen'},
    '5': {'name': 'Egypt', 'capital': 'Cairo'},
    '6': {'name': 'Fiji', 'capital': 'Suva'},
    '7': {'name': 'Germany', 'capital': 'Berlin'},
    '8': {'name': 'Haiti', 'capital': 'Port-au-Prince'},
    '9': {'name': 'India', 'capital': 'New Delhi'},
    '10':{'name': 'Japan', 'capital': 'Tokyo'},
    '11':{'name': 'Kenya', 'capital': 'Nairobi'},
    '12':{'name': 'Luxemburg', 'capital':'Luxemburg'},
    '13':{'name': 'Maldives', 'capital': 'Male'},
    '14':{'name': 'Netherlands', 'capital': 'Amsterdam'},
    '15':{'name': 'Oman', 'capital': 'Muscat'},
    '16':{'name': 'Panama', 'capital': 'Panama city'},
    '17':{'name': 'Qatar', 'capital': 'Doha'},
    '18':{'name': 'Russia', 'capital': 'Moscow'},
    '19':{'name': 'Saint Lucia', 'capital': 'Castries'},
    '20':{'name': 'Turkey', 'capital': 'Ankara'},
    '21':{'name': 'United States', 'capital': 'Washington D.C'},
    '22':{'name': 'Venezuela', 'capital': 'Caracas'},
    '23':{'name': 'Zambia', 'capital': 'Lusaka'},
    '24':{'name': 'United Kingdom', 'capital': 'London'},

 }

parser = reqparse.RequestParser()

class CountriesList(Resource):
     def get(self):
         return COUNTRIES


     def post(self):
         parser.add_argument("name")
         parser.add_argument("capital")
         args = parser.parse_args()
         country_id = int(max(COUNTRIES.keys())) +1
         country_id = '%i' % country_id
         COUNTRIES[country_id] = {
             "name": args["name"],
            "capital":args["capital"],
         }
         return COUNTRIES[country_id],201
         

class Country(Resource):
      def get(self, country_id):
          if country_id not in COUNTRIES:
            return "Not found", 404
          else:
            return COUNTRIES[country_id]


      def put(self, country_id):
          parser.add_argument("name")
          parser.add_argument("capital")
          args = parser.parse_args()
          if country_id not in COUNTRIES:
              return "Record not found", 404
          else:
             country = COUNTRIES[country_id]
             country["name"] = args["name"] if args["name"] is not None else country["name"]
             country["capital"] = args["capital"] if args["capital"] is not None else country["capital"]
             return country, 200

      def delete(self, country_id):
          if country_id not in COUNTRIES:
           return "Not found", 404
          else:
             del COUNTRIES[country_id]
             return '', 204


api.add_resource(CountriesList, '/countries')
api.add_resource(Country, '/countries/<country_id>')
