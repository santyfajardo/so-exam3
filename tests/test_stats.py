import pytest
import sys
sys.path.append('/home/santiago/so-exam3')

from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'porcentaje_cpu', return_value=50)
  response = client.get('/v1/stats/cpu')
  assert response.data.decode('utf-8') == '{"CPU Porcentaje": 50}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'memoria_disponible', return_value=20)
  response = client.get('/v1/stats/memory')
  assert response.data.decode('utf-8') == '{"Espacio en memoria": 20}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'espacio_disco', return_value=150)
  response = client.get('/v1/stats/disk')
  assert response.data.decode('utf-8') == '{"Espacio en el Disco": 150}'
  assert response.status_code == 200

