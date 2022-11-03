import json
from unittest.mock import patch

from flower_bed_designer.helpers import ApiException

data_logic_path = 'flower_bed_designer.blueprints.plant.api.data_logic'


@patch(data_logic_path)
def test_get_plants(m_data_logic, client):
    fake_plants = [1, 2]
    m_data_logic.get_plants.return_value = fake_plants

    response = client.get('/plant/')
    plants = json.loads(response.data)

    assert response.status_code == 200
    assert plants == fake_plants


@patch(data_logic_path)
def test_get_plant(m_data_logic, client):
    fake_plant = {'key': 'value'}
    m_data_logic.get_plant.return_value = fake_plant

    response = client.get('/plant/1')
    plant = json.loads(response.data)

    assert response.status_code == 200
    assert plant == fake_plant


@patch(data_logic_path)
def test_get_plant_fails(m_data_logic, client):
    fake_body = {'message': 'error'}
    m_data_logic.get_plant.side_effect = ApiException('error')

    response = client.get('/plant/1')
    body = json.loads(response.data)

    assert response.status_code == 400
    assert body == fake_body


@patch(data_logic_path)
def test_post(m_data_logic, client):
    fake_plant = {'key': 'value'}
    m_data_logic.create_plant.return_value = fake_plant

    response = client.post('/plant/', content_type='application/json', data=json.dumps(fake_plant))
    plant = json.loads(response.data)

    assert response.status_code == 201
    assert plant == fake_plant


@patch(data_logic_path)
def test_put(m_data_logic, client):
    fake_plant = {'key': 'value'}
    m_data_logic.update_plant.return_value = fake_plant

    response = client.put('/plant/1', content_type='application/json', data=json.dumps(fake_plant))
    plant = json.loads(response.data)

    assert response.status_code == 200
    assert plant == fake_plant


@patch(data_logic_path)
def test_delete(m_data_logic, client):
    m_data_logic.delete_plant.return_value = {'key': 'value'}

    response = client.delete('/plant/1')

    assert response.status_code == 204
    assert response.data == b''
