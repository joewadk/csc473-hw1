from flask import Flask, abort, jsonify, request

from inspector import Inspector

app = Flask(__name__)


@app.route("/search", methods=["GET"])
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
    limit= request.args.get('limit', default = 10, type = int)
    print(restaurant, cuisine, zipcode)
    inspections = [inspection.to_json() for inspection in Inspector.get_inspections()]
    return jsonify(inspections[:limit])


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=8080)
    
