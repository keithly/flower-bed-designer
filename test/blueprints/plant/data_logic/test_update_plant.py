import pytest

from flower_bed_designer.helpers import ApiException
from flower_bed_designer.blueprints.plant.data_logic import update_plant


def test_update_plant(test_plants_data, test_cu_plant_data):
    plant = update_plant(test_plants_data, 1, test_cu_plant_data)

    assert plant['plant_id'] == 1
    del plant['plant_id']
    assert plant == test_cu_plant_data


def test_update_plant_not_found(test_plants_data, test_cu_plant_data):
    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 4, test_cu_plant_data)

    assert excinfo.value.message == 'Not Found'
    assert excinfo.value.status == 404


required_msg = 'required key not provided'


def test_update_plant_missing_common_name(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['common_name']

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert required_msg in excinfo.value.message
    assert 'common_name' in excinfo.value.message
    assert excinfo.value.status == 400


def test_update_plant_missing_genus(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['genus']

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert required_msg in excinfo.value.message
    assert 'genus' in excinfo.value.message
    assert excinfo.value.status == 400


def test_update_plant_missing_species(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['species']

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert required_msg in excinfo.value.message
    assert 'species' in excinfo.value.message
    assert excinfo.value.status == 400


def test_update_plant_missing_family(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['family']

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert required_msg in excinfo.value.message
    assert 'family' in excinfo.value.message
    assert excinfo.value.status == 400


invalid_str_values = [1, True, 1.1, None, {}]
invalid_str_msg = 'expected str for dictionary value'


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_update_plant_invalid_common_name(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['common_name'] = test_value

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert invalid_str_msg in excinfo.value.message
    assert 'common_name' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_update_plant_invalid_genus(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['genus'] = test_value

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert invalid_str_msg in excinfo.value.message
    assert 'genus' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_update_plant_invalid_species(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['species'] = test_value

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert invalid_str_msg in excinfo.value.message
    assert 'species' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_update_plant_invalid_family(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['family'] = test_value

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert invalid_str_msg in excinfo.value.message
    assert 'family' in excinfo.value.message
    assert excinfo.value.status == 400


invalid_bool_values = [1, 'blah', 1.1, None, {}]
invalid_bool_msg = 'expected bool for dictionary value'


@pytest.mark.parametrize('test_value', invalid_bool_values)
def test_update_plant_invalid_rhizomatous(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['rhizomatous'] = test_value

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert invalid_bool_msg in excinfo.value.message
    assert 'rhizomatous' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_bool_values)
def test_update_plant_invalid_garden_friendly(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['garden_friendly'] = test_value

    with pytest.raises(ApiException) as excinfo:
        update_plant(test_plants_data, 1, test_cu_plant_data)

    assert invalid_bool_msg in excinfo.value.message
    assert 'garden_friendly' in excinfo.value.message
    assert excinfo.value.status == 400
