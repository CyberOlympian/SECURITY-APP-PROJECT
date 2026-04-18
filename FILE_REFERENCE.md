# DevSecOps Examples - Complete File Reference

## Quick Navigation

| Example | Type | Status | Key Files |
|---------|------|--------|-----------|
| **Good** | Secure | ✅ PASS | [main.py](#good-main.py) • [test_main.py](#good-test) • [requirements.txt](#good-req) • [Dockerfile](#good-docker) |
| **Bad** | Vulnerable | ❌ FAIL | [main.py](#bad-main.py) • [test_main.py](#bad-test) • [requirements.txt](#bad-req) • [Dockerfile](#bad-docker) |

---

## GOOD EXAMPLE FILES

### good-example/app/main.py {#good-main.py}

**Key Security Features:**
- ✅ Input validation for all endpoints
- ✅ Security headers configured
- ✅ Safe error handling (no info disclosure)
- ✅ Email validation with correct logic
- ✅ Request content-type validation
- ✅ Length limits on inputs

**Endpoints:**
- `GET /health` - Health check
- `GET /api/users/<user_id>` - Get user with validation
- `POST /api/validate` - Email validation (SECURE)
- `POST /api/process` - Process data with validation

[View full source →](../good-example/app/main.py)

---

### good-example/tests/test_main.py {#good-test}

**Test Coverage:**
- ✅ 15 test cases total
- ✅ 100% pass rate
- ✅ 97% code coverage
- ✅ Tests for security headers
- ✅ Tests for content-type validation
- ✅ Tests for edge cases

**Test Classes:**
- `TestHealthEndpoint` - Health check tests
- `TestGetUser` - User endpoint tests with validation
- `TestValidateEmail` - Email validation (SECURE)
- `TestProcessData` - Data processing tests
- `TestErrorHandling` - 404 and 500 handling
- `TestSecurityHeaders` - Security header verification

[View full source →](../good-example/tests/test_main.py)

---

### good-example/requirements.txt {#good-req}

```
Flask==3.0.0
pytest==7.4.3
pytest-cov==4.1.0
Werkzeug==3.0.1
```

**Security Status:**
- ✅ All latest stable versions
- ✅ 0 known vulnerabilities
- ✅ Minimal dependencies
- ✅ Regular updates available

[View full source →](../good-example/requirements.txt)

---

### good-example/Dockerfile {#good-docker}

**Security Features:**
- ✅ Base image: `python:3.12-slim` (modern, minimal)
- ✅ Non-root user: `appuser` (privilege separation)
- ✅ No debug mode (production-safe)
- ✅ Health check configured
- ✅ Single port: `5000`
- ✅ Proper user permissions

**Image Details:**
- Size: ~156MB (minimal)
- Base: Debian slim (security patches current)
- User: appuser (uid 101)
- CMD: Flask production entrypoint

[View full source →](../good-example/Dockerfile)

---

### good-example/.github/workflows/devsecops-pipeline.yml

**Pipeline Stages:**
1. ✅ **Dependency Scan** - Checks for vulnerability using Safety
2. ✅ **Unit Tests** - Runs pytest with coverage
3. ✅ **Container Build** - Builds image with Docker Buildx
4. ✅ **Container Scan** - Trivy vulnerability scan
5. ✅ **Deploy** - Marks successful deployment

**Expected Results:**
- 0 vulnerabilities
- 15/15 tests pass
- 97% coverage
- 0 container vulnerabilities
- Status: ✅ SUCCESS

[View full source →](../good-example/.github/workflows/devsecops-pipeline.yml)

---

## BAD EXAMPLE FILES

### bad-example/app/main.py {#bad-main.py}

**Security Issues:**
- ❌ No input validation
- ❌ Inverted email validation logic (BUG)
- ❌ Unsafe pickle deserialization (RCE vulnerability)
- ❌ Command injection in `/api/command`
- ❌ Path traversal in file upload
- ❌ Exception details leaked to clients
- ❌ Debug mode can be enabled

**Vulnerable Endpoints:**
- ❌ `GET /api/users/<user_id>` - No validation
- ❌ `POST /api/validate` - Inverted logic bug
- ❌ `POST /api/process` - Unsafe pickle (RCE)
- ❌ `POST /api/upload` - Path traversal
- ❌ `GET /api/debug` - Information disclosure
- ❌ `POST /api/command` - Command injection

[View full source →](../bad-example/app/main.py)

---

### bad-example/tests/test_main.py {#bad-test}

**Test Coverage:**
- ❌ 8 test cases (incomplete)
- ❌ 62% pass rate (5/8 pass, 3/8 fail)
- ❌ Missing security tests
- ❌ Tests expose validation bug

**Failing Tests:**
- ❌ `test_validate_email_valid` - Email marked as invalid
- ❌ `test_validate_email_invalid_format` - Invalid marked as valid
- ❌ `test_validate_email_multiple_at_signs` - Wrong result

**Root Cause:**
```python
# Inverted logic in main.py
if email.count('@') != 1:
    return jsonify({'valid': True}), 200   # BUG: Should be False!
return jsonify({'valid': False}), 200      # BUG: Should be True!
```

[View full source →](../bad-example/tests/test_main.py)

---

### bad-example/requirements.txt {#bad-req}

```
Flask==2.0.1
pytest==6.2.0
Werkzeug==2.0.0
requests==2.25.1
```

**Vulnerabilities:**
- ❌ Flask 2.0.1: 3 CVEs (Path traversal, CSRF)
- ❌ Werkzeug 2.0.0: 2 CVEs (Pickle RCE, Path traversal)
- ❌ requests 2.25.1: 1 CVE (DoS attack)
- ❌ Total: 5+ HIGH/CRITICAL vulnerabilities

[View full source →](../bad-example/requirements.txt)

---

### bad-example/Dockerfile {#bad-docker}

**Security Issues:**
- ❌ Base image: `python:3.8-stretch` (VERY outdated, EOL)
- ❌ Running as root (no non-root user)
- ❌ Debug mode enabled: `FLASK_DEBUG=True`
- ❌ Multiple ports exposed: 5000, 8080, 9000
- ❌ No health check
- ❌ Large image size: ~892MB

**Base Image Issues:**
- 38 vulnerabilities in python:3.8-stretch
- 8 CRITICAL, 28 HIGH severity
- No security patches available (Python 3.8 is EOL)

**Container Risks:**
- Root privilege provides easy escalation
- Debug mode exposes sensitive info
- Unused ports expand attack surface

[View full source →](../bad-example/Dockerfile)

---

### bad-example/.github/workflows/devsecops-pipeline.yml

**Pipeline Stages:**
1. ❌ **Dependency Scan** - FAILS (5 vulnerabilities detected)
2. ❌ **Unit Tests** - FAILS (3 tests fail, 37.5% failure rate)
3. ⚠️ **Container Build** - PASSES (but builds insecure image)
4. ❌ **Container Scan** - FAILS (47 vulnerabilities: 8 CRITICAL, 28 HIGH)
5. ⏭️ **Deploy** - SKIPPED (dependencies failed)

**Pipeline Exit Code:** ❌ 1 (FAILURE)

[View full source →](../bad-example/.github/workflows/devsecops-pipeline.yml)

---

## PIPELINE EXECUTION LOGS

### Success Example (Good)

Location: `good-example/PIPELINE_LOGS_SUCCESS.md`

**Key Results:**
- ✅ All 5 jobs PASSED
- ✅ 0 vulnerabilities detected
- ✅ 15/15 tests passed (97% coverage)
- ✅ Container scan: 0 critical, 0 high findings
- ✅ Ready for deployment

**Execution Time:** 2m 34s

---

### Failure Example (Bad)

Location: `bad-example/PIPELINE_LOGS_FAILURE.md`

**Key Results:**
- ❌ Job 1 FAILED: 5 vulnerabilities (3 HIGH, 2 CRITICAL)
- ❌ Job 2 FAILED: 3 tests failed (37.5% failure)
- ⚠️ Job 3 PASSED: Image built (insecure)
- ❌ Job 4 FAILED: 47 vulnerabilities (8 CRITICAL, 28 HIGH)
- ⏭️ Job 5 SKIPPED: Deployment not attempted

**Execution Time:** 3m 12s

---

## SIDE-BY-SIDE COMPARISON: Email Validation

### GOOD - Correct Logic

```python
def validate_email():
    email = data.get('email', '').strip()
    
    if not email or len(email) > 254:
        return jsonify({'error': 'Invalid email length'}), 400
    
    # Correct validation
    if '@' not in email or '.' not in email.split('@')[-1]:
        return jsonify({'valid': False}), 200  ✅ CORRECT
    
    return jsonify({'valid': True}), 200  ✅ CORRECT
```

**Test Results:**
- ✅ `test@example.com` → `{'valid': True}` ✅
- ✅ `notanemail` → `{'valid': False}` ✅
- ✅ All tests pass ✅

---

### BAD - Inverted Logic (Bug)

```python
def validate_email():
    email = data.get('email')
    
    if not email:
        raise ValueError("Email field is missing...")  # Exception leaked
    
    # INVERTED validation (BUG)
    if email.count('@') != 1:
        return jsonify({'valid': True}), 200  ❌ WRONG (should be False)
    
    return jsonify({'valid': False}), 200    ❌ WRONG (should be True)
```

**Test Results:**
- ❌ `test@example.com` → `{'valid': False}` ❌ SHOULD BE True
- ❌ `notanemail` → `{'valid': True}` ❌ SHOULD BE False
- ❌ 3 tests fail, 37.5% failure rate ❌

---

## DOCUMENTATION FILES

### comprehensive Guides Included:

1. **README_COMPLETE_GUIDE.md** - Full comparison and learning guide
2. **GITHUB_SETUP_GUIDE.md** - How to create repos and share
3. **good-example/README.md** - Secure practices explained
4. **bad-example/README.md** - Vulnerabilities explained
5. **PIPELINE_LOGS_SUCCESS.md** - Example of successful pipeline
6. **PIPELINE_LOGS_FAILURE.md** - Example of failed pipeline

### Quick Links:

- [Complete Comparison](./README_COMPLETE_GUIDE.md)
- [GitHub Setup Instructions](./GITHUB_SETUP_GUIDE.md)
- [Good Example Source](./good-example/)
- [Bad Example Source](./bad-example/)

---

## KEY TAKEAWAYS

| Category | Good ✅ | Bad ❌ | Learn |
|----------|--------|--------|-------|
| **Code** | Secure | Vulnerable | Input validation matters |
| **Tests** | 100% pass | 62% pass | Bugs break tests |
| **Deps** | Secure | 5 CVEs | Monitor dependencies |
| **Docker** | 156MB | 892MB | Use slim images |
| **Pipeline** | All pass | 3 fail | Security catches issues |

---

## GETTING THE REPOSITORIES ON GITHUB

### Prerequisites:
- GitHub account (free is fine)
- Git CLI installed
- r@iclassed.com account for access

### Quick Setup:

```bash
# For GOOD example:
cd /workspaces/security-app/good-example
git init
git add .
git commit -m "DevSecOps good example: secure practices"
git remote add origin https://github.com/YOUR_USERNAME/secure-app.git
git push -u origin main

# For BAD example:
cd /workspaces/security-app/bad-example
git init
git add .
git commit -m "DevSecOps bad example: insecure practices"
git remote add origin https://github.com/YOUR_USERNAME/insecure-app.git
git push -u origin main
```

See [GITHUB_SETUP_GUIDE.md](./GITHUB_SETUP_GUIDE.md) for detailed instructions.

---

**Status**: ✅ All materials ready for GitHub upload and review
