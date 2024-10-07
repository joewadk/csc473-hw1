from flask import Flask, abort, jsonify, request

from inspector import Inspector

app = Flask(__name__)


@app.route("/search", methods=["GET"]) #search route, using get to get an output
def search():
    
    '''
    Below you will find several examples of requests that clients might make:
  - `curl --location --request GET 'http://127.0.0.1:8080/search?restaurant_name=pizza'`
    - [Example response](golden_files/search_by_restaurant_name.json)
  - `curl --location --request GET 'http://127.0.0.1:8080/search?zipcode=10031'`
    - [Example response](golden_files/search_by_zipcode.json)
  - `curl --location --request GET 'http://127.0.0.1:8080/search?cuisine=italian&limit=5'`
    - [Example response](golden_files/search_by_cuisine_with_limit.json)
  - `curl --location --request GET 'http://127.0.0.1:8080/search?cuisine=mexican&zipcode=10003'`
    - [Example response](golden_files/search_by_cuisine_and_zipcode.json)
  - `curl --location --request GET 'http://127.0.0.1:8080/search?restaurant_name=taco&cuisine=mexican&zipcode=10003'`
    - [Example response](golden_files/search_by_restaurant_name_cuisine_and_zipcode.json)
    ''' #adding here for self-reference



    #create inspector object
    #load json
    #search for any args



    restaurant=request.args.get('restaurant_name')
    cuisine=request.args.get('cuisine')
    zipcode=request.args.get('zipcode')
    limit= request.args.get('limit', default = 10, type = int) #default limit is 10, but can be changed by user
    print(restaurant, cuisine, zipcode) #debug to see if i get the right params
    inspections = [inspection.to_json() for inspection in Inspector.get_inspections()] #load the json


    #conditional statements to filter the inspections
    if restaurant: 
        inspections = [insp for insp in inspections if restaurant.lower() in insp['restaurant_name'].lower() ] #case insensitive, and also checks if param inside restaurant_name
    if cuisine:
        inspections = [insp for insp in inspections if insp['cuisine'].lower() == cuisine.lower()]#case insensitive, and also checks if param == cuisine
    if zipcode:
        inspections = [insp for insp in inspections if insp['zipcode'] == zipcode] #strictly checks if param == zipcode
    inspections.sort(key=lambda x: x['restaurant_id']) #lambda to sort by restaurant_id
    return jsonify(inspections[:limit]) #return the jsonified inspections with the limit


if __name__ == "__main__": #boiler plate, no touch!!!!
    app.run(host="localhost", debug=True, port=8080)
    
