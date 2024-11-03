import pytest
from conftest import Client, goods_data

def test_post_goods(client: Client, goods_data):
    goods_data['name'] = 'Test Product'
    goods_data['nodeId'] = 1
    goods_data['externalId'] = None
    response = client.post("/partner/v2/goods", json=goods_data)
    assert response.status_code == 200

@pytest.mark.parametrize("max_results", [10, 25])
def test_get_goods(client: Client, max_results):
    response = client.get(f"/partner/v2/goods?max={max_results}&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= max_results

@pytest.mark.parametrize("node_id", [1, 5])
def test_get_goods_by_node(client: Client, node_id):
    response = client.get(f"/partner/v2/goods?max=10&offset=0&nodeId={node_id}")
    assert response.status_code == 200
    data = response.json()
    for item in data:
        assert "nodeId" in item and item["nodeId"] == node_id

def test_get_goods_by_id(client: Client):
    response = client.get(f"/partner/v2/goods/345")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data

def test_put_goods(client: Client, goods_data):
    goods_data['name'] = 'Updated Test Product'
    goods_data['nodeId'] = 1
    goods_data['externalId'] = None
    response = client.put("/partner/v2/goods/345", json=goods_data)
    assert response.status_code == 200

def test_delete_goods(client: Client):
    response = client.delete(f"/partner/v2/goods/345")
    assert response.status_code == 204

@pytest.mark.parametrize("offset", [10, 20])
def test_get_goods_with_offset(client: Client, offset):
    response = client.get(f"/partner/v2/goods?max=10&offset={offset}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 10

def test_post_goods_with_hidden(client: Client, goods_data):
    goods_data['name'] = 'Test Product'
    goods_data['nodeId'] = 1
    goods_data['externalId'] = None
    goods_data['hidden'] = True
    response = client.post("/partner/v2/goods", json=goods_data)
    assert response.status_code == 200

def test_get_goods_hidden(client: Client):
    response = client.get(f"/partner/v2/goods/345")
    assert response.status_code == 200
    data = response.json()
    assert "hidden" in data

def test_put_goods_hidden(client: Client, goods_data):
    goods_data['name'] = 'Updated Test Product'
    goods_data['nodeId'] = 1
    goods_data['externalId'] = None
    goods_data['hidden'] = True
    response = client.put("/partner/v2/goods/345", json=goods_data)
    assert response.status_code == 200

def test_delete_goods_hidden(client: Client):
    response = client.delete(f"/partner/v2/goods/345")
    assert response.status_code == 204

