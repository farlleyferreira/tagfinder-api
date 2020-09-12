import os
import json

from flask import Flask, abort, request, send_from_directory, jsonify
from flask_expects_json import expects_json
from flask_swagger import swagger
from blueprint import Schema
from main import Process


app = Flask(__name__)

swagger_url = ''
app_base_url = '/docs/swagger.json'

swaggerui_blueprint = Schema().get_blueprint(swagger_url, app_base_url)

corpus = {
    'type': 'object',
    'properties': {
        'corpus': {'type': 'string'}
    },
    'required': ['corpus']
}

tag_list = {
    'type': 'object',
    'properties': {
        'tag_list': {
            'type': 'array',
        }
    },
    'required': ['tag_list']
}


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'ping'}), 200


@app.route("/docs/swagger.json")
def specs():
    return send_from_directory(os.getcwd(), "docs/swagger.json")


@app.route('/create', methods=['POST'])
@expects_json(corpus)
def create():
    try:
        
        data_request = request.data
        data_object = json.loads(data_request)
        corpus = data_object["corpus"]
        
        
        if corpus:

            output_process = Process().get_hashtags(corpus)
            output = Process().get_hashtag_rates(output_process)

            if len(output) > 0:
                return jsonify({'response': output}), 200

            else:
                return jsonify({'response': 'no content'}), 204                

        else:
            return jsonify({'response': 'bad request'}), 400            

    except:
        abort(500, description="unhandled exception")


@app.route('/validate', methods=['POST'])
@expects_json(tag_list)
def validate():
    try:
        
        data_request = request.data
        data_object = json.loads(data_request)
        tag_list = data_object["tag_list"]
        
        
        if len(tag_list) > 0:

            output = Process().get_hashtag_rates(tag_list)

            if len(output) > 0:
                return jsonify({'response': output}), 200

            else:
                return jsonify({'response': 'no content'}), 204                

        else:
            return jsonify({'response': 'bad request'}), 400            

    except:
        abort(500, description="unhandled exception")


app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

if __name__ == '__main__':
    app.run(debug=True)
