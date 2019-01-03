from voluptuous import MultipleInvalid

from flower_bed_designer.blueprints.plant import schemas
from flower_bed_designer.helpers import ApiException


def get_plants(plants_data):
    return plants_data


def get_plant(plants_data, plant_id):
    try:
        plant = [p for p in plants_data if p['plant_id'] == plant_id][0]
        return plant

    except IndexError:
        raise ApiException('Not Found', 404)


def create_plant(plants_data, request_json):
    try:
        schemas.plant_schema(request_json)

        new_plant = {
            'plant_id': 4,
            'common_name': request_json['common_name'],
            'genus': request_json['genus'],
            'species': request_json['species'],
            'family': request_json['family'],
            'rhizomatous': request_json['rhizomatous'],
            'garden_friendly': request_json['garden_friendly']
        }
        plants_data.append(new_plant)

        return new_plant

    except MultipleInvalid as e:
        raise ApiException(str(e), 400)


def update_plant(plants_data, plant_id, request_json):
    try:
        schemas.plant_schema(request_json)

        plant = [p for p in plants_data if p['plant_id'] == plant_id][0]
        plant['common_name'] = request_json['common_name']
        plant['genus'] = request_json['genus']
        plant['species'] = request_json['species']
        plant['family'] = request_json['family']
        plant['rhizomatous'] = request_json['rhizomatous']
        plant['garden_friendly'] = request_json['garden_friendly']

        return plant

    except MultipleInvalid as e:
        raise ApiException(str(e), 400)

    except IndexError:
        raise ApiException('Not Found', 404)


def delete_plant(plants_data, plant_id):
    if [p for p in plants_data if p['plant_id'] == plant_id]:
        plants_data[:] = [p for p in plants_data if p.get('plant_id') != plant_id]
        return {}
    else:
        raise ApiException('Not Found', 404)
