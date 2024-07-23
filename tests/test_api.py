# test REST API using FastAPI
# https://fastapi.tiangolo.com/tutorial/bigger-applications/
# https://fastapi.tiangolo.com/tutorial/testing/

API_VERSION = 'v1'

from fastapi.testclient import TestClient
from api import api

# Define API testclient for 'api'

client = TestClient(api)

def test_tea_pot():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'You\'re a tea pot?'}
