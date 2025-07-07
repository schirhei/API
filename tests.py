from main import test_client
from datetime import datetime

def test_root():
    response = test_client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello World"}

def test_time():
    response = test_client.get('/time')
    assert response.status_code == 200
    assert response.json().get('Time')

def test_get_order_id():
    response = test_client.get('/order/1')
    assert response.status_code == 200
    assert response.json()['Order'][0] == ["Name", 1234567891012131, "Wireless Data"]

def test_checkout():
    response = test_client.post('/checkout', content = '{"name": "Testname", "creditCard": 9876543210987654, "product": "TELUS Phone Plan 20GB"}')
    assert response.status_code == 200
    assert isinstance(response.json()['Order ID'], int)