GITHUB ACTIONS WORKFLOW EXECUTION LOG - BAD EXAMPLE
====================================================

Workflow: DevSecOps CI/CD Pipeline - BAD Example
Branch: main
Commit: b4g3f2d9e8c7f6a5f4e3d2c1b0a9z8y7x6w5v4u3
Status: ❌ FAILED

═══════════════════════════════════════════════════════════════════════

JOB 1: DEPENDENCY SCAN
Status: ❌ FAILED

Step 1: Checkout code
✅ Checking out repository...
✅ Fetched 2 commits
✅ Repository ready at: /home/runner/work/insecure-app

Step 2: Set up Python 3.8
⚠️  Python 3.8 selected (DEPRECATED - EOL since October 2024)
✅ Python version: Python 3.8.18 (default, Sep 11 2023, 13:44:46)
✅ pip version: pip 20.3.4 (old version)

Step 3: Install security tools
✅ Installing safety package for dependency scanning
✅ Successfully installed safety-2.3.5

Step 4: Run dependency vulnerability scan
⚠️  Scanning dependencies for known vulnerabilities...

Safety Scan Results:
═════════════════════════════════════════════════════════

🚨 CRITICAL VULNERABILITIES DETECTED 🚨

Using 4 packages:
  Flask==2.0.1                 ❌ VULNERABLE - 3 HIGH severity CVEs
  pytest==6.2.0                ✅ OK
  Werkzeug==2.0.0              ❌ VULNERABLE - 2 HIGH severity CVEs
  requests==2.25.1             ❌ VULNERABLE - 1 CRITICAL severity CVE

Vulnerability Details:
─────────────────────────────────────────────────

[1] Flask - CVE-2021-22885
    Severity: HIGH
    Description: Werkzeug before 2.0.1 mishandles specially crafted HTTP
                 requests, leading to path traversal vulnerability
    Published: 2021-05-12
    CVSS Score: 7.2

[2] Flask - CVE-2021-22886  
    Severity: HIGH
    Description: Before Werkzeug 2.0.1, certain specially crafted cookies
                 could bypass CSRF protections
    Published: 2021-05-12
    CVSS Score: 6.8

[3] Werkzeug==2.0.0 - CVE-2021-21241
    Severity: HIGH
    Description: Werkzeug 2.0.0 uses unsafe pickle which can lead to
                 arbitrary code execution
    Published: 2021-02-17
    CVSS Score: 9.8

[4] Werkzeug==2.0.0 - CVE-2021-3020
    Severity: CRITICAL
    Description: Path traversal vulnerability in development mode when
                 running with static file serving
    Published: 2021-04-28
    CVSS Score: 8.6

[5] requests==2.25.1 - CVE-2021-33503
    Severity: CRITICAL
    Description: Uncontrolled resource consumption in requests library
                 allows denial of service attacks
    Published: 2021-06-09
    CVSS Score: 9.1

═════════════════════════════════════════════════════════════════════════

Summary:
❌ 5 vulnerabilities found
❌ 3 HIGH severity vulnerabilities  
❌ 2 CRITICAL severity vulnerabilities
❌ All dependencies have known CVEs

Recommendation: Upgrade to latest stable versions immediately

Safety Exit Code: 1 (FAIL)

⚠️  JOB 1 FAILED: Vulnerability threshold exceeded
═══════════════════════════════════════════════════════════════════════

JOB 2: UNIT TESTS  
Status: ❌ FAILED (after dependency-scan)

Step 1: Checkout code
✅ Repository ready

Step 2: Set up Python 3.8
✅ Python 3.8.18 environment ready (outdated)

Step 3: Install dependencies
⚠️  Installing from requirements.txt
  Installing Flask-2.0.1 (with known CVEs)
  Installing pytest-6.2.0
  Installing Werkzeug-2.0.0 (with known CVEs)
  Installing requests-2.25.1 (with known CVEs)
⚠️  All dependencies installed (note: vulnerable versions)

Step 4: Run unit tests
❌ Running pytest...

collected 8 items

tests/test_main.py::TestHealthEndpoint::test_health_check PASSED [ 12%]
tests/test_main.py::TestGetUser::test_get_user_valid_id PASSED [ 25%]
tests/test_main.py::TestValidateEmail::test_validate_email_valid FAILED [ 37%]
tests/test_main.py::TestValidateEmail::test_validate_email_invalid_format FAILED [ 50%]
tests/test_main.py::TestValidateEmail::test_validate_email_multiple_at_signs FAILED [ 62%]
tests/test_main.py::TestProcessData::test_process_data_simple PASSED [ 75%]
tests/test_main.py::TestErrorHandling::test_missing_email_field PASSED [ 87%]

═════════════════════════════════════════════════════════════════════════

FAILURES:
─────────────────────────────────────────────────────

FAILED tests/test_main.py::TestValidateEmail::test_validate_email_valid

def test_validate_email_valid(client):
    """Test email validation with valid email - WILL FAIL DUE TO BUG"""
    response = client.post('/api/validate',
        data=json.dumps({'email': 'test@example.com'}),
        content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
>   assert data['valid'] is True
E   AssertionError: assert False is True
E   Test expects: True (valid email)
E   Got: False (WRONG!)

File: tests/test_main.py:43
Line: 43


FAILED tests/test_main.py::TestValidateEmail::test_validate_email_invalid_format

def test_validate_email_invalid_format(client):
    """Test email validation with invalid format - WILL ALSO FAIL"""
    response = client.post('/api/validate',
        data=json.dumps({'email': 'notanemail'}),
        content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
>   assert data['valid'] is False
E   AssertionError: assert True is False
E   Test expects: False (invalid email)
E   Got: True (WRONG!)

File: tests/test_main.py:52
Line: 52

Root Cause: Email validation logic is inverted in app/main.py
The validation function at line 34 has incorrect logic:

  if email.count('@') != 1:
      return jsonify({'valid': True}), 200   # Bug: Should be False!
  
  return jsonify({'valid': False}), 200      # Bug: Should be True!


FAILED tests/test_main.py::TestValidateEmail::test_validate_email_multiple_at_signs

def test_validate_email_multiple_at_signs(client):
    """Test email with multiple @ signs - WILL FAIL"""
    response = client.post('/api/validate',
        data=json.dumps({'email': 'test@@example.com'}),
        content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
>   assert data['valid'] is False
E   AssertionError: assert True is False
E   Same validation logic bug as above

File: tests/test_main.py:58
Line: 58

═════════════════════════════════════════════════════════════════════════

Summary:
❌ 8 tests executed
❌ 5 tests passed
❌ 3 tests FAILED
❌ Failure rate: 37.5%

Exit Code: 1 (TEST FAILURE)

⚠️  JOB 2 FAILED: Unit tests did not pass

═════════════════════════════════════════════════════════════════════════

JOB 3: CONTAINER BUILD
Status: ⚠️  PASSED (continuing despite previous failures)

Step 1: Set up Docker Buildx
✅ Docker buildx v0.12.0
✅ Available builders: default

Step 2: Build container image
⚠️  Building Docker image with vulnerable base...

Building for platform: linux/amd64

FROM python:3.8-stretch
 ---> 5d2c3b1a0f9e (sha256:...) ⚠️ VERY OLD BASE IMAGE
 ---> Running in xyz9876abc15

⚠️  No non-root user created (running as root!)
✅ Set working directory: /app
✅ Copied requirements.txt
⚠️  Installed vulnerable dependencies
✅ Copied application code
⚠️  No file permission hardening
⚠️  Running as root (default)
⚠️  Exposed multiple unnecessary ports: 5000, 8080, 9000
⚠️  Debug mode enabled: FLASK_DEBUG=True

✅ Successfully tagged: insecure-app:b4g3f2d9e8c7f6a5f4e3d2c1b0a9z8y7x6w5v4u3
⚠️  Image size: 892MB (very large!)
⚠️  Build completed in 45.12s (long build time)

Step 3: Upload container artifact
✅ Uploading image to: artifact-storage
✅ Artifact size: 768MB
✅ Upload completed

═════════════════════════════════════════════════════════════════════════

JOB 4: CONTAINER SECURITY SCAN
Status: ❌ FAILED (after container-build)

Step 1: Download container image
✅ Downloaded artifact
✅ Loading image from tar...

Loaded image: insecure-app:b4g3f2d9e8c7f6a5f4e3d2c1b0a9z8y7x6w5v4u3

Step 2: Run Trivy vulnerability scanner
❌ Trivy v0.44.3
❌ Scanning image: insecure-app:b4g3f2d9e8c7f6a5f4e3d2c1b0a9z8y7x6w5v4u3

Trivy Vulnerability Report
═════════════════════════════════════════════════════════════════════

Image: insecure-app:b4g3f2d9e8c7f6a5f4e3d2c1b0a9z8y7x6w5v4u3
Scanned at: 2024-04-10T15:32:18.456Z

Total: 47 vulnerabilities (Base image: 38, Python packages: 9)
❌ CRITICAL: 8 critical vulnerabilities found
❌ HIGH:     28 high severity vulnerabilities
⚠️  MEDIUM:   11 medium severity vulnerabilities

CRITICAL VULNERABILITIES:
─────────────────────────────────────────────────────

[CRITICAL] glibc - CVE-2023-4927
  Package: glibc 2.24-11+deb9u4
  Severity: CRITICAL (CVSS 9.8)
  Description: Memory corruption and arbitrary code execution
  Fixed in: 2.31-12

[CRITICAL] openssl - CVE-2023-3817
  Package: openssl 1.1.0f-1
  Severity: CRITICAL (CVSS 9.6)
  Description: Possible infinite loop when using X.509 certificates
  Fixed in: 1.1.1n

[CRITICAL] curl - CVE-2022-32208
  Package: curl 7.52.1-5+deb9u16
  Severity: CRITICAL (CVSS 9.1)
  Description: FTP path traversal attack
  Fixed in: 7.68.0

[CRITICAL] Python Package Vulnerabilities (from requirements.txt):
  - Flask==2.0.1: CVE-2021-22885 (CRITICAL)
  - Werkzeug==2.0.0: CVE-2021-3020 (CRITICAL)
  - requests==2.25.1: CVE-2021-33503 (CRITICAL)

HIGH SEVERITY VULNERABILITIES (Sample):
─────────────────────────────────────────────────────

[HIGH] zlib - CVE-2018-25032
  Package: zlib 1.2.8
  Severity: HIGH (CVSS 7.4)
  [... 27 more HIGH severity issues ...]

Image Configuration Issues:
❌ Container running as root user (HIGH RISK)
❌ Debug mode enabled in environment (SECURITY RISK)
❌ Multiple ports exposed unnecessarily (8080, 9000)
❌ No non-root user configured
❌ No health check defined
❌ No resource limits

Scan Recommendations:
1. Upgrade base image immediately: python:3.8-stretch → python:3.12-slim
2. Fix validation logic bug in app/main.py
3. Update all dependencies to latest versions
4. Configure non-root user in Dockerfile
5. Remove debug mode from production environment
6. Only expose required ports

Scan completed with findings!
❌ Exit code: 1 (FAIL - critical vulnerabilities found)

═════════════════════════════════════════════════════════════════════════

JOB 5: DEPLOY STATUS
Status: ❌ SKIPPED (due to job dependencies failing)

Step 1: Check deployment status (SKIPPED)
The pipeline stopped at container-scan due to:
  ❌ Critical vulnerabilities detected
  ❌ Previous job failed: container-scan

Deployment was not attempted.

═════════════════════════════════════════════════════════════════════════

WORKFLOW FAILED: ❌ MULTIPLE CRITICAL ISSUES
─────────────────────────────────────────────────────

Failed Jobs:
  ❌ Dependency Scan: 5 vulnerabilities detected (3 HIGH, 2 CRITICAL)
  ❌ Unit Tests: 3 tests failed (37.5% failure rate)
  ❌ Container Scan: 47 vulnerabilities (8 CRITICAL, 28 HIGH)

Pipeline Summary:
  Timestamp: 2024-04-10T15:48:32Z
  Build Time: 3m 12s
  Total Jobs: 5
  Completed: 4
  Passed: 1
  Failed: 3
  Skipped: 1
  Final Status: ❌ FAILED

Workflow Exit Code: 1 (FAILURE)

═════════════════════════════════════════════════════════════════════════
WORKFLOW COMPLETED: ❌ FAILED - NOT SUITABLE FOR DEPLOYMENT
═════════════════════════════════════════════════════════════════════════
