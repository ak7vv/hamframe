from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from ..api import api

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { 'message': 'https://github.com/ak7vv/hamframe' }

# def test_create_item():
#     response = client.post("/items/", json={"name": "Item1", "price": 10.0})
#     assert response.status_code == 201
#     assert response.json() == {"name": "Item1", "price": 10.0}
