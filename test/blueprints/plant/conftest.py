import pytest


@pytest.fixture
def test_plants_data():
    return [
        {
            'plant_id': 1,
            'common_name': 'common milkweed',
            'genus': 'asclepias',
            'species': 'syriaca',
            'family': 'asclepiadaceae',
            'rhizomatous': True,
            'garden_friendly': False
        },
        {
            'plant_id': 2,
            'common_name': 'purple milkweed',
            'genus': 'asclepias',
            'species': 'purpurascens',
            'family': 'asclepiadaceae',
            'rhizomatous': True,
            'garden_friendly': True
        },
        {
            'plant_id': 3,
            'common_name': 'heart-leaved aster',
            'genus': 'symphyotrichum',
            'species': 'cordifolium',
            'family': 'asteraceae',
            'rhizomatous': False,
            'garden_friendly': True
        }
    ]


@pytest.fixture
def test_cu_plant_data():
    return {
        'common_name': 'common milkweed',
        'genus': 'asclepias',
        'species': 'syriaca',
        'family': 'asclepiadaceae',
        'rhizomatous': True,
        'garden_friendly': False
    }


@pytest.fixture
def test_get_plant_data(test_cu_plant_data):
    test_cu_plant_data['plant_id'] = 1
    return test_cu_plant_data
