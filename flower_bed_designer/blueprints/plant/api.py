from flask.views import MethodView
from flask import request, jsonify

from flower_bed_designer.helpers import validate_body, api_result
from flower_bed_designer.blueprints.plant import data_logic
from flower_bed_designer.persistence import plants_data


class PlantAPI(MethodView):
    decorators = [api_result]

    def get(self, plant_id):
        if plant_id:
            return data_logic.get_plant(plants_data, plant_id)
        else:
            return data_logic.get_plants(plants_data)

    def post(self):
        validate_body(request.json)

        return data_logic.create_plant(plants_data, request.json), 201

    def put(self, plant_id):
        validate_body(request.json)

        return data_logic.update_plant(plants_data, plant_id, request.json)

    def delete(self, plant_id):
        return data_logic.delete_plant(plants_data, plant_id), 204
