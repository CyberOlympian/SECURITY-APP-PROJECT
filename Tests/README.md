# DevSecOps Bad Example - Insecure Flask Microservice

This repository demonstrates **insecure** DevSecOps practices with an intentionally failing CI/CD pipeline.

## Vulnerabilities Intentionally Included

❌ **Code Vulnerabilities**
- Broken email validation logic (intentional bug)
- Command injection vulnerability
- Unsafe pickle deserialization (RCE risk)
- Path traversal in file upload
- Information disclosure via error messages
- Debug mode enabled in production
- No input validation
- SQL injection potential

❌ **Failed Tests**
- Email validation test failures due to logic bug
- Multiple test failures demonstrating the impact

❌ **Vulnerable Dependencies**
- Flask 2.0.1 (outdated, has known CVEs)
- Werkzeug 2.0.0 (vulnerable version)
- requests 2.25.1 (outdated)

❌ **Insecure Container**
- Python 3.8-stretch (very outdated, many vulnerabilities)
- Running as root user
- Debug mode enabled
- Unnecessary ports exposed
- No health checks

❌ **Failing Security Pipeline**
- Dependency scan: HIGH severity vulnerabilities detected
- Unit tests: Multiple test failures
- Container scan: CRITICAL security findings
- Pipeline exit code: FAILED

## Repository Structure

```
bad-example/
├── app/
│   └── main.py (WITH VULNERABILITIES)
├── tests/
│   └── test_main.py (WITH FAILING TESTS)
├── Dockerfile (INSECURE)
├── requirements.txt (VULNERABLE DEPENDENCIES)
└── .github/
    └── workflows/
        └── devsecops-pipeline.yml (WILL FAIL)
```

## Pipeline Status

❌ **FAILED** - Multiple security checks and tests failed

### Failure Summary:
1. ❌ **Dependency Scan FAILED** - 5 vulnerabilities detected (HIGH, CRITICAL)
2. ❌ **Unit Tests FAILED** - 2 of 3 tests failed due to validation logic bug
3. ❌ **Container Scan FAILED** - 12+ vulnerabilities in base image

## This is a Training Resource

This repository intentionally contains security vulnerabilities for educational purposes. These vulnerabilities should be studied to understand:

- How validation logic bugs break functionality
- Impact of using outdated dependencies
- Container security best practices
- Python security issues
- How proper CI/CD pipelines catch these issues

**DO NOT USE THESE PATTERNS IN PRODUCTION CODE**
