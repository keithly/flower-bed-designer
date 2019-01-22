plant_schema = {
    'common_name': {'required': True, 'type': 'string'},
    'genus': {'required': True, 'type': 'string'},
    'species': {'required': True, 'type': 'string'},
    'family': {'required': True, 'type': 'string'},
    'rhizomatous': {'type': 'boolean'},
    'garden_friendly': {'type': 'boolean'}
}

bed_schema = {
    'area': {'required': True, 'type': 'float'},
    'plants': {'required': True, 'type': 'list', 'schema': {'type': 'integer'}}
}

user_schema = {
    'username': {'required': True, 'type': 'string'},
    'beds': {'required': True, 'type': 'list', 'schema': {'type': 'integer'}}
}
