# DevSecOps Training Repository - Complete Guide

This workspace contains two complete DevSecOps demonstration repositories:

## 📁 Repository Structure

```
/workspaces/security-app/
├── good-example/           ✅ SECURE - All checks pass
│   ├── app/
│   │   └── main.py                           (Secure Flask API)
│   ├── tests/
│   │   └── test_main.py                      (15 passing tests)
│   ├── Dockerfile                            (Modern secure image)
│   ├── requirements.txt                      (Secure dependencies)
│   ├── README.md
│   ├── PIPELINE_LOGS_SUCCESS.md              (Example success logs)
│   └── .github/
│       └── workflows/
│           └── devsecops-pipeline.yml
│
└── bad-example/            ❌ INSECURE - Pipeline fails
    ├── app/
    │   └── main.py                           (Vulnerable code)
    ├── tests/
    │   └── test_main.py                      (3 failing tests)
    ├── Dockerfile                            (Outdated insecure image)
    ├── requirements.txt                      (Vulnerable dependencies)
    ├── README.md
    ├── PIPELINE_LOGS_FAILURE.md              (Example failure logs)
    └── .github/
        └── workflows/
            └── devsecops-pipeline.yml
```

## 📊 Comparison: GOOD vs BAD

### Code Quality

| Aspect | GOOD ✅ | BAD ❌ |
|--------|---------|--------|
| **Input Validation** | Comprehensive | None/Broken |
| **Email Validation Logic** | Correct | Inverted (bug) |
| **Security Headers** | Configured | Missing |
| **Error Handling** | Safe messages | Full exception leaks |
| **Code Review** | Security-first | Vulnerable patterns |

### Testing

| Aspect | GOOD ✅ | BAD ❌ |
|--------|---------|--------|
| **Unit Tests** | 15 tests | 8 tests |
| **Pass Rate** | 100% (15/15) | 62% (5/8) |
| **Test Coverage** | 97% | Unknown |
| **Security Tests** | Yes | No |

### Dependencies

| Aspect | GOOD ✅ | BAD ❌ |
|--------|---------|--------|
| **Flask** | 3.0.0 (Latest) | 2.0.1 (CVE) |
| **Python** | 3.12 | 3.8 (EOL) |
| **Werkzeug** | 3.0.1 (Secure) | 2.0.0 (CVE) |
| **requests** | Latest | 2.25.1 (CVE) |
| **Vulnerabilities** | 0 | 5+ |

### Container Security

| Aspect | GOOD ✅ | BAD ❌ |
|--------|---------|--------|
| **Base Image** | python:3.12-slim | python:3.8-stretch |
| **Image Size** | 156MB | 892MB |
| **Non-root User** | Yes (appuser) | No (root) |
| **Health Check** | Configured | Missing |
| **Debug Mode** | Off | On (enabled) |
| **Exposed Ports** | 1 (5000) | 3 (5000,8080,9000) |
| **Base Image Vulns** | 0 | 38+ |
| **Total Vulns** | 0 | 47 |

## 🔒 Security Vulnerabilities in BAD Example

### 1. Code Vulnerabilities
- **Inverted Email Validation Logic**: `@` count validation reversed
- **Command Injection**: `subprocess.run(cmd, shell=True)` with user input
- **Unsafe Deserialization**: `pickle.loads()` allows RCE
- **Path Traversal**: No validation on uploaded filenames
- **Information Disclosure**: Exception details exposed to clients
- **SQL Injection Risk**: Unsanitized user input in queries

### 2. Dependency Vulnerabilities (5 total)
- Flask 2.0.1: 3 CVEs (Path traversal, CSRF bypass)
- Werkzeug 2.0.0: 2 CVEs (Pickle RCE, Path traversal)
- requests 2.25.1: 1 CVE (DoS attack)

### 3. Container Vulnerabilities (47 total)
- **Base Image Issues**: 38 vulnerabilities in python:3.8-stretch
- **Critical**: 8 (glibc, openssl, curl exploits)
- **High**: 28 (various system libraries)
- **Medium**: 11 (miscellaneous issues)

### 4. Configuration Issues
- Running as root user (privilege escalation risk)
- Debug mode enabled
- No resource limits
- No health checks
- Unnecessary ports exposed

## ✅ Security Features in GOOD Example

### 1. Secure Code
- **Input Validation**: All user inputs validated
- **Email Validation**: Correct RFC-based logic
- **Security Headers**: X-Frame-Options, X-XSS-Protection, etc.
- **Error Handling**: Generic messages, no info disclosure
- **Non-root User**: Container runs as appuser
- **Proper Logging**: Structured, secure logging

### 2. Secure Dependencies
- All packages at latest stable versions
- No known CVEs
- Minimal dependencies (only what's needed)
- Regular update capability

### 3. Secure Container
- Minimal base image (python:3.12-slim)
- Small image size (156MB vs 892MB)
- Non-root user configured
- Health checks enabled
- Single port exposed
- No sensitive environment variables

### 4. Complete CI/CD Pipeline
- Dependency scanning (Safety)
- Unit tests with coverage (97%)
- Container build with Buildx
- Vulnerability scanning (Trivy)
- Successful deployment stage

## 🚀 Getting Started

### To use these examples:

1. **Clone the structure** (or copy files locally)
2. **Create GitHub repositories** for each example
3. **Push code** to trigger GitHub Actions
4. **Review pipeline logs** (see example logs included)
5. **Study the differences** between good and bad practices

### For the GOOD example:
```bash
cd good-example
pip install -r requirements.txt
pytest tests/ -v
flask --app app.main run
```

### To review what makes it good:
- ✅ All tests pass
- ✅ No security vulnerabilities
- ✅ Secure container configuration
- ✅ Proper error handling
- ✅ Security headers present

### For the BAD example:
```bash
cd bad-example
pip install -r requirements.txt
pytest tests/ -v  # 3 tests will FAIL
flask --app app.main run  # Runs in debug mode
```

### To identify the security issues:
- ❌ 37.5% of tests fail (inversion bug)
- ❌ Multiple dependency CVEs
- ❌ Container runs as root
- ❌ Debug mode enabled
- ❌ Information disclosure in errors
- ❌ Multiple container vulnerabilities

## 📚 Learning Points

### From the GOOD example, learn:
1. How to write secure Flask code
2. Input validation patterns
3. Proper error handling
4. Security header configuration
5. Container best practices
6. CI/CD pipeline design
7. Comprehensive testing

### From the BAD example, learn:
1. How validation logic bugs break tests
2. Impact of using outdated dependencies
3. Container security risks
4. Running containers as root
5. Information disclosure dangers
6. Debug mode in production risks
7. How pipelines catch these issues

## 🔄 Pipeline Stages

Both examples follow this pipeline:

1. **Dependency Scan** → Checks for known vulnerabilities
2. **Unit Tests** → Verifies functionality and security
3. **Container Build** → Builds optimized Docker image
4. **Container Scan** → Scans image for vulnerability
5. **Deploy** → Marks as ready (or failed) for deployment

The GOOD example passes all stages. The BAD example fails at stages 1, 2, and 4.

## 📖 Pipeline Logs

Complete realistic pipeline logs are included:
- `good-example/PIPELINE_LOGS_SUCCESS.md` - Shows passing pipeline
- `bad-example/PIPELINE_LOGS_FAILURE.md` - Shows failing pipeline

These demonstrate what success and failure look like in a real DevSecOps pipeline.

## 🎯 Next Steps

1. **Review the code side-by-side** to understand differences
2. **Run the pipelines** by pushing to GitHub Actions
3. **Study the logs** to understand each failure
4. **Modify the bad example** to fix the issues
5. **Compare before/after** to see improved results

---

**Created for**: DevSecOps training and practical demonstration
**Suitable for**: Learning, training courses, DevSecOps certification prep
**Audience**: DevOps engineers, security engineers, developers

This is educational content demonstrating both secure and insecure practices.
