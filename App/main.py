"""
Insecure Flask API microservice with deliberate vulnerabilities
Demonstrates poor security practices
"""
from flask import Flask, request, jsonify
import pickle
import os
from datetime import datetime

app = Flask(__name__)

# Security issue: Debug mode can be enabled via environment
DEBUG_MODE = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'version': '1.0.0'}), 200

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID - VULNERABLE: no input validation"""
    # Security issue: Direct concatenation in query (SQL injection potential)
    # In real scenario, this would be vulnerable if connected to database
    user = {
        'id': user_id,  # No validation!
        'name': f'User {user_id}',
        'email': f'user{user_id}@example.com'
    }
    return jsonify(user), 200

@app.route('/api/validate', methods=['POST'])
def validate_email():
    """Validate email - VULNERABLE: improper error handling"""
    try:
        # Security issue: No check for JSON content-type
        data = request.get_json(force=True)  # force=True is dangerous
        email = data.get('email')
        
        # Security issue: Full exception message leaked to client
        if not email:
            raise ValueError("Email field is missing from database record ID 12345")
        
        # Broken validation logic - this is the intentional bug
        # The logic is inverted - it marks invalid emails as valid
        if email.count('@') != 1:  # Bug: wrong validation
            return jsonify({'valid': True}), 200  # Should be False!
        
        return jsonify({'valid': False}), 200  # Should be True!
    except Exception as e:
        # Security issue: Full exception traceback exposed to client
        import traceback
        return jsonify({
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 400

@app.route('/api/process', methods=['POST'])
def process_data():
    """Process data - VULNERABLE: insecure deserialization"""
    try:
        data = request.get_json(force=True)
        serialized_data = data.get('data', b'')
        
        # CRITICAL VULNERABILITY: Unsafe pickle deserialization
        # This allows arbitrary code execution (RCE)
        result = pickle.loads(serialized_data)
        
        return jsonify({'result': str(result)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload - VULNERABLE: no validation"""
    # Security issue: No file type validation, path traversal possible
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # VULNERABILITY: No validation of filename - path traversal possible
    # e.g., a file named "../../etc/passwd" would write outside intended directory
    filename = file.filename
    upload_dir = '/tmp/uploads'
    
    # Path traversal vulnerability
    filepath = os.path.join(upload_dir, filename)
    file.save(filepath)
    
    return jsonify({'message': f'File saved to {filepath}'}), 200

@app.route('/api/debug', methods=['GET'])
def debug_info():
    """Debug endpoint - SHOULD NEVER BE IN PRODUCTION"""
    if not DEBUG_MODE:
        return jsonify({'error': 'Not available'}), 404
    
    # Leaking sensitive information
    return jsonify({
        'debug': True,
        'environment': dict(os.environ),
        'python_version': os.sys.version,
        'config': app.config
    }), 200

@app.route('/api/command', methods=['POST'])
def execute_command():
    """Execute system command - CRITICAL VULNERABILITY"""
    data = request.get_json(force=True)
    cmd = data.get('command')
    
    # CRITICAL: Command injection vulnerability
    # OS command executed with user input
    import subprocess
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    return jsonify({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    }), 200

if __name__ == '__main__':
    # VULNERABILITY: Debug mode enabled in production
    app.run(host='0.0.0.0', port=5000, debug=DEBUG_MODE)
