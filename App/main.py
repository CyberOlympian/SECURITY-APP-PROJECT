Secure Flask API microservice
Demonstrates secure coding practices
"""
from flask import Flask, request, jsonify
import logging
import os
from functools import wraps
import json

app = Flask(__name__)

# Configure secure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security headers
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

def validate_request(f):
    """Decorator to validate incoming requests"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == 'POST':
            if not request.is_json:
                return jsonify({'error': 'Content-Type must be application/json'}), 400
        return f(*args, **kwargs)
    return decorated_function

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'version': '1.0.0'}), 200

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID - with input validation"""
    if user_id < 0 or user_id > 1000000:
        logger.warning(f"Invalid user_id requested: {user_id}")
        return jsonify({'error': 'Invalid user ID'}), 400
    
    # Simulated user retrieval
    user = {
        'id': user_id,
        'name': f'User {user_id}',
        'email': f'user{user_id}@example.com'
    }
    return jsonify(user), 200

@app.route('/api/validate', methods=['POST'])
@validate_request
def validate_email():
    """Validate email address with secure input handling"""
    try:
        data = request.get_json(force=False, strict=True)
        email = data.get('email', '').strip()
        
        if not email or len(email) > 254:
            return jsonify({'error': 'Invalid email length'}), 400
        
        # Basic email validation
        if '@' not in email or '.' not in email.split('@')[-1]:
            return jsonify({'valid': False}), 200
        
        return jsonify({'valid': True}), 200
    except Exception as e:
        logger.error(f"Error validating email: {str(e)}", exc_info=True)
        return jsonify({'error': 'Invalid request format'}), 400

@app.route('/api/process', methods=['POST'])
@validate_request
def process_data():
    """Process data with input validation"""
    try:
        data = request.get_json(force=False, strict=True)
        value = data.get('value')
        
        # Validate input type and value
        if not isinstance(value, (int, str)):
            return jsonify({'error': 'Invalid input type'}), 400
        
        if isinstance(value, str) and len(value) > 1000:
            return jsonify({'error': 'Input too long'}), 400
        
        result = f"Processed: {str(value)[:100]}"
        return jsonify({'result': result}), 200
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({'error': 'Invalid input'}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}", exc_info=True)
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Use environment variable for debug mode, default to False in production
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
