import os
import json
from flask import Flask, request
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
from sparseArray import SparseArray

##########################################
# SWAGGER CONFIGURATION
##########################################
# Set the configuration of Swagger
app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

template = dict(
    swaggerUiPrefix=LazyString(lambda: request.environ.get("HTTP_X_SCRIPT_NAME", ""))
)

app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, config=swagger_config, template=template)


##########################################
# sparseArray INSTANCE
##########################################
# Prepare sparseArray instance
input_file = open(os.environ['INPUT_PATH'], mode='r')
input_data = input_file.read().splitlines()
sparseArray = SparseArray(input_data)
print(sparseArray)


##########################################
# Flask APP METHODS
##########################################
def compute_sparse_array(queries):
    query_result = sparseArray.matching_strings(queries)
    return query_result


@app.route("/")
def index():
    return "Swagger UI - Sparse Array calculation"


@app.route("/compute_sparse_array", methods=["POST"])
@swag_from("swagger_config.yml")
def sparse_array():
    input_json = request.get_json()
    try:
        query = str(input_json["query"])
        query = query.split(',')
        query_result = compute_sparse_array(query)
        res = {k: v for k, v in zip(query, query_result)}
    except:
        res = {"success": False, "message": "Unknown error"}

    return json.dumps(res)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8791)
