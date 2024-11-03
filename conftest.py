import pytest
from httpx import Client, Response
import base64
import uuid
from datetime import datetime

@pytest.fixture(scope='session')
def client():
    authString = base64.b64encode(b'549756189636:OTBhZmRmOTctOGIzMS00ZDM5LWE5YjAtZmE2NDNiZjc3Yzky')
    headers={
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8',
        'Authorization': 'Basic ' + authString.decode("utf-8"),
        'X-Origin-Request-Id': str(uuid.uuid4()),
        'X-Timestamp': datetime.now().isoformat(),
    }
    return Client(base_url='http://api.uds.app', headers=headers)

@pytest.fixture(scope='session')
def goods_data():
    return {
        "name": "Test Product",
        "nodeId": 1,
        "externalId": None,
        "data": {"property1": "value1", "property2": "value2"},
        "hidden": False
    }

