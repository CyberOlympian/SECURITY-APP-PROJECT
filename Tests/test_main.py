"""
Unit tests for the Flask API microservice
"""
import pytest
import json
from app.main import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestHealthEndpoint:
    def test_health_check(self, client):
        """Test health check endpoint returns 200"""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'version' in data

class TestGetUser:
    def test_get_user_valid_id(self, client):
        """Test retrieving user with valid ID"""
        response = client.get('/api/users/123')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == 123
        assert data['name'] == 'User 123'
        assert '@example.com' in data['email']
    
    def test_get_user_invalid_negative_id(self, client):
        """Test retrieving user with negative ID returns error"""
        response = client.get('/api/users/-1')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data

    def test_get_user_invalid_large_id(self, client):
        """Test retrieving user with ID out of range"""
        response = client.get('/api/users/9999999')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data

class TestValidateEmail:
    def test_validate_email_valid(self, client):
        """Test email validation with valid email"""
        response = client.post('/api/validate',
            data=json.dumps({'email': 'test@example.com'}),
            content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['valid'] is True

    def test_validate_email_invalid_format(self, client):
        """Test email validation with invalid format"""
        response = client.post('/api/validate',
            data=json.dumps({'email': 'notanemail'}),
            content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['valid'] is False

    def test_validate_email_empty(self, client):
        """Test email validation with empty email"""
        response = client.post('/api/validate',
            data=json.dumps({'email': ''}),
            content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data

    def test_validate_email_wrong_content_type(self, client):
        """Test validation endpoint without JSON content type"""
        response = client.post('/api/validate',
            data='email=test@example.com',
            content_type='application/x-www-form-urlencoded')
        assert response.status_code == 400

class TestProcessData:
    def test_process_data_string(self, client):
        """Test processing string data"""
        response = client.post('/api/process',
            data=json.dumps({'value': 'test data'}),
            content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'result' in data

    def test_process_data_integer(self, client):
        """Test processing integer data"""
        response = client.post('/api/process',
            data=json.dumps({'value': 42}),
            content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'result' in data

    def test_process_data_string_too_long(self, client):
        """Test processing string longer than 1000 characters"""
        long_string = 'x' * 1001
        response = client.post('/api/process',
            data=json.dumps({'value': long_string}),
            content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data

    def test_process_data_invalid_type(self, client):
        """Test processing invalid data type"""
        response = client.post('/api/process',
            data=json.dumps({'value': ['invalid', 'list']}),
            content_type='application/json')
        assert response.status_code == 400

class TestErrorHandling:
    def test_404_not_found(self, client):
        """Test 404 error handling"""
        response = client.get('/api/nonexistent')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data

class TestSecurityHeaders:
    def test_security_headers_present(self, client):
        """Test that security headers are present in response"""
        response = client.get('/health')
        assert 'X-Content-Type-Options' in response.headers
        assert response.headers['X-Content-Type-Options'] == 'nosniff'
        assert 'X-Frame-Options' in response.headers
        assert response.headers['X-Frame-Options'] == 'DENY'
        assert 'X-XSS-Protection' in response.headers
