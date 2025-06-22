import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_motor_category(client):
    response = client.post('/classify', json={'description': 'Mi motor se ha sobrecalentado'})
    assert response.status_code == 200
    assert response.get_json()['category'] == 'Motor'


def test_tire_category(client):
    response = client.post('/classify', json={'description': 'Quiero cambiar las llantas'})
    assert response.status_code == 200
    assert response.get_json()['category'] == 'Neumaticos'


def test_electric_category(client):
    response = client.post('/classify', json={'description': 'Se ha roto el sistema electrico del coche'})
    assert response.status_code == 200
    assert response.get_json()['category'] == 'Electric'
