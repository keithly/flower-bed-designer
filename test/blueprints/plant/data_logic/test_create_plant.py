import pytest

from flower_bed_designer.helpers import ApiException
from flower_bed_designer.blueprints.plant.data_logic import create_plant


def test_create_plant(test_plants_data, test_cu_plant_data):
    plant = create_plant(test_plants_data, test_cu_plant_data)

    assert len(test_plants_data) == 4
    assert plant['plant_id'] == 4
    del plant['plant_id']
    assert plant == test_cu_plant_data


def test_create_plant_missing_common_name(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['common_name']

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'common_name' in excinfo.value.message
    assert excinfo.value.status == 400


def test_create_plant_missing_genus(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['genus']

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'genus' in excinfo.value.message
    assert excinfo.value.status == 400


def test_create_plant_missing_species(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['species']

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'species' in excinfo.value.message
    assert excinfo.value.status == 400


def test_create_plant_missing_family(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['family']

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'family' in excinfo.value.message
    assert excinfo.value.status == 400


def test_create_plant_missing_multiple(test_plants_data, test_cu_plant_data):
    del test_cu_plant_data['family']
    del test_cu_plant_data['genus']

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'family' in excinfo.value.message
    assert 'genus' in excinfo.value.message
    assert excinfo.value.status == 400


invalid_str_values = [1, True, 1.1, None, {}]


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_create_plant_invalid_common_name(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['common_name'] = test_value

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'common_name' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_create_plant_invalid_genus(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['genus'] = test_value

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'genus' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_create_plant_invalid_species(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['species'] = test_value

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'species' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_str_values)
def test_create_plant_invalid_family(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['family'] = test_value

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'family' in excinfo.value.message
    assert excinfo.value.status == 400


invalid_bool_values = [1, 'blah', 1.1, None, {}]


@pytest.mark.parametrize('test_value', invalid_bool_values)
def test_create_plant_invalid_rhizomatous(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['rhizomatous'] = test_value

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'rhizomatous' in excinfo.value.message
    assert excinfo.value.status == 400


@pytest.mark.parametrize('test_value', invalid_bool_values)
def test_create_plant_invalid_garden_friendly(test_plants_data, test_cu_plant_data, test_value):
    test_cu_plant_data['garden_friendly'] = test_value

    with pytest.raises(ApiException) as excinfo:
        create_plant(test_plants_data, test_cu_plant_data)

    assert 'garden_friendly' in excinfo.value.message
    assert excinfo.value.status == 400
