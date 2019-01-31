from flask import request, jsonify, make_response
from flask.views import MethodView

from flower_bed_designer.blueprints.plant import data_logic
from flower_bed_designer.helpers import validate_body, ApiResult
from flower_bed_designer.persistence import plants_data


class PlantAPI(MethodView):

    def get(self, plant_id):
        if plant_id:
            return ApiResult(data_logic.get_plant(plants_data, plant_id))
        else:
            return ApiResult(data_logic.get_plants(plants_data))

    def post(self):
        validate_body(request.json)

        return ApiResult(data_logic.create_plant(plants_data, request.json), 201)

    def put(self, plant_id):
        validate_body(request.json)

        return ApiResult(data_logic.update_plant(plants_data, plant_id, request.json))

    def delete(self, plant_id):
        return ApiResult(data_logic.delete_plant(plants_data, plant_id), 204)

    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response
