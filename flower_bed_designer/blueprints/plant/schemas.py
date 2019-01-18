from voluptuous import Schema, Optional, All, Range

plant_schema = Schema({
    'common_name': str,
    'genus': str,
    'species': str,
    'family': str,
    Optional('rhizomatous'): bool,
    Optional('garden_friendly'): bool
}, required=True)

create_plant_schema = plant_schema.extend({'plant_id': All(int, Range(min=1))})

c_schema = {
    'common_name': {'required': True, 'type': 'string'},
    'genus': {'required': True, 'type': 'string'},
    'species': {'required': True, 'type': 'string'},
    'family': {'required': True, 'type': 'string'},
    'rhizomatous': {'type': 'boolean'},
    'garden_friendly': {'type': 'boolean'}
}
