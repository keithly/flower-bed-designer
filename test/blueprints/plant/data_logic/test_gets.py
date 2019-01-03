import pytest

from flower_bed_designer.helpers import ApiException
from flower_bed_designer.blueprints.plant.data_logic import get_plants, get_plant


def test_get_plants(test_plants_data):
    plants = get_plants(test_plants_data)

    assert plants == test_plants_data


def test_get_plant(test_plants_data, test_get_plant_data):
    plant = get_plant(test_plants_data, 1)

    assert plant == test_get_plant_data


def test_get_plant_not_found(test_plants_data):
    with pytest.raises(ApiException) as excinfo:
        get_plant(test_plants_data, 4)

    assert excinfo.value.message == 'Not Found'
    assert excinfo.value.status == 404
