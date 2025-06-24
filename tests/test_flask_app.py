from src.main import app
import pytest

@pytest.fixture
def client():
    # create a test client using flask application configures for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

    
def test_home_page_loads(client):
    # Test GET request to home page
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data # Check if form is present in html



def test_marks_post_valid_data(client):
    # Test POST request with valid marks
    data = {'Physics':'80',
            'Maths':'90',
            'Chemistry':'85',
            'Hindi': '75',
            'English':'95'
            }
    response = client.post('/submit', data=data)
    assert response.status_code == 200
    assert b'85.0' in response.data



def test_marks_post_missing_data(client):
    # Test POST request with missing field (English missing)
    data = {
        'Physics': '80',
        'Maths': '90',
        'Chemistry': '85',
        'Hindi': '75'
    }
    response = client.post('/submit', data=data)
    
    # Your current app will raise KeyError, so expect failure (status code != 200)
    assert response.status_code != 200



# def test_marks_post_invalid_data(client):
#     # Test POST request with invalid (non-integer) data
#     data = {
#         'Physics': 'eighty',
#         'Maths': '90',
#         'Chemistry': '85',
#         'Hindi': '75',
#         'English': '95'
#     }
#     response = client.post('/submit', data=data)
    
#     # Your app will raise ValueError on int conversion, so expect failure
#     assert response.status_code != 200
#     assert b"Please enter valid integer marks" in response.data
