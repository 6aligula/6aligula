import json
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class FakeClassifier:
    def __call__(self, text, labels):
        mapping = {
            "Mi motor se ha sobrecalentado": {"labels": ["Motor"]},
            "Quiero cambiar las llantas": {"labels": ["Neumaticos"]},
            "Se ha roto el sistema electrico del coche": {"labels": ["Electric"]},
        }
        return mapping.get(text, {"labels": ["Otros"]})

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr('transformers.pipelines.pipeline', lambda *a, **k: FakeClassifier())
    import app
    with app.app.test_client() as client:
        yield client

def test_motor_category(client):
    response = client.post('/classify', json={'description': 'Mi motor se ha sobrecalentado'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['category'] == 'Motor'

def test_tire_category(client):
    response = client.post('/classify', json={'description': 'Quiero cambiar las llantas'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['category'] == 'Neumaticos'

def test_electric_category(client):
    response = client.post('/classify', json={'description': 'Se ha roto el sistema electrico del coche'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['category'] == 'Electric'
