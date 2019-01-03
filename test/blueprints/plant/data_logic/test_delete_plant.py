import pytest

from flower_bed_designer.helpers import ApiException
from flower_bed_designer.blueprints.plant.data_logic import delete_plant


def test_delete_plant(test_plants_data):
    result = delete_plant(test_plants_data, 1)

    assert result == {}


def test_delete_plant_not_found(test_plants_data):
    with pytest.raises(ApiException) as excinfo:
        delete_plant(test_plants_data, 4)

    assert excinfo.value.message == 'Not Found'
    assert excinfo.value.status == 404
