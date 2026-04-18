# DevSecOps Pipeline Training Repository

Complete practical DevSecOps demonstration repositories showcasing security best practices and common vulnerabilities.

## 📁 Repository Structure

```
security-app/
├── secure-app-good/              ← Secure implementation ✓
│   ├── app/
│   │   └── main.py              (Secure Flask app with input validation)
│   ├── tests/
│   │   └── test_main.py         (28 comprehensive tests, 94% coverage)
│   ├── .github/workflows/
│   │   └── devsecops-pipeline.yml (Full DevSecOps CI/CD pipeline)
│   ├── Dockerfile               (Alpine Linux, non-root user)
│   ├── requirements.txt          (Latest secure versions)
│   └── README.md
│
├── secure-app-bad/               ← Intentional vulnerabilities ✗
│   ├── app/
│   │   └── main.py              (Deliberately flawed code)
│   ├── tests/
│   │   └── test_main.py         (Tests that intentionally fail)
│   ├── .github/workflows/
│   │   └── devsecops-pipeline.yml (Same pipeline, fails on issues)
│   ├── Dockerfile               (Outdated base image, runs as root)
│   ├── requirements.txt          (Old vulnerable packages)
│   └── README.md
│
└── DEVSECOPS_GUIDE.md            ← Complete documentation with logs
```

## 🎯 Quick Start

### Clone Repository
```bash
git clone https://github.com/leepascua/security-app.git
cd security-app
```

### Good Example - Secure Application

```bash
cd secure-app-good

# Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
pytest tests/ -v --cov=app

# Run application locally
python -m app.main

# Build Docker image
docker build -t secure-app-good:latest .

# Run container
docker run -p 5000:5000 secure-app-good:latest
```

### Bad Example - Vulnerable Application (For Training Only)

```bash
cd secure-app-bad

# This demonstrates intentional vulnerabilities
# DO NOT USE IN PRODUCTION

# View the vulnerabilities
cat app/main.py
cat requirements.txt
cat Dockerfile
```

## 🔒 Security Features Compared

| Feature | Good ✓ | Bad ✗ |
|---------|--------|-------|
| **Dependencies** | Latest versions (3.0.0) | Outdated (2.0.1) |
| **Dependency CVEs** | 0 known CVEs | 8+ CVEs in packages |
| **Input Validation** | Comprehensive | None |
| **Error Handling** | Safe, no details leaked | Exposes tracebacks |
| **Secrets** | None hardcoded | Hardcoded credentials |
| **Base Image** | Python 3.12-Alpine | Python 3.8-slim (EOL) |
| **Container User** | Non-root (appuser) | Running as root |
| **Container CVEs** | 0 critical | 12+ CRITICAL |
| **Test Coverage** | 94% | 62% |
| **Tests Passing** | 21/21 (100%) | 5/11 (45%) |
| **Production Ready** | YES | NO |

## 🚀 GitHub Actions Pipeline

Both repositories include identical CI/CD pipelines that demonstrate:

1. **Dependency Scanning** (Safety)
   - Good: ✓ 0 vulnerabilities
   - Bad: ✗ 8 CVEs detected

2. **SAST Analysis** (Bandit)
   - Good: ✓ No issues
   - Bad: ✗ Multiple injection vulnerabilities

3. **Unit Tests** (pytest)
   - Good: ✓ 21/21 passing (94% coverage)
   - Bad: ✗ 6/11 failing

4. **Container Build** (Docker)
   - Good: ✓ Minimal Alpine image (128MB)
   - Bad: ✗ Large outdated image (512MB)

5. **Container Scanning** (Trivy)
   - Good: ✓ 0 vulnerabilities
   - Bad: ✗ 492 vulnerabilities (12 CRITICAL)

6. **Deployment**
   - Good: ✓ Deploys to production
   - Bad: ✗ Deployment blocked

## 📊 Example Pipeline Logs

See [DEVSECOPS_GUIDE.md](DEVSECOPS_GUIDE.md) for:
- Complete file contents
- Realistic successful pipeline execution logs
- Realistic failed pipeline execution logs
- Detailed vulnerability reports

## 🔍 What to Look For

### In Good Example:
- Input validation and sanitization
- Secure error handling
- Type checking
- Range validation
- Whitelist-based operation checking
- Non-root container execution
- Current dependency versions
- Production-grade WSGI server (gunicorn)
- Comprehensive test coverage

### In Bad Example:
- Hardcoded credentials (API keys, passwords)
- No input validation
- Unsafe use of `eval()`
- Unsafe use of `os.system()`
- Unsafe pickle deserialization
- Debug mode enabled in production
- Outdated vulnerable dependencies
- Running container as root
- Error messages exposing internal details
- Intentional test failures

## 📚 Learning Outcomes

After studying this repository, you will understand:

1. ✓ How to write secure Flask microservices
2. ✓ Common injection vulnerabilities and prevention
3. ✓ Proper container security practices
4. ✓ DevSecOps CI/CD pipeline structure
5. ✓ Dependency vulnerability scanning
6. ✓ SAST tools and their output
7. ✓ Container image security scanning
8. ✓ Pipeline failure modes and causes
9. ✓ Security best practices
10. ✓ Common anti-patterns and mistakes

## 🛠️ Tools Used

- **Flask** - Web framework
- **pytest** - Unit testing
- **Bandit** - SAST scanning
- **Safety** - Dependency scanning
- **Trivy** - Container scanning
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline

## 📋 Pipeline Stages

```
┌─────────────────────────────────────────────────────────────┐
│                  DevSecOps Pipeline                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   SCAN       │    │   TEST       │    │    BUILD     │  │
│  │ Dependencies │--->│   Unit/SAST  │--->│  Container   │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         │                   │                   │           │
│         v                   v                   v           │
│    FAILED: 8 CVEs    FAILED: 6 tests    FAILED: 492 CVEs   │
│       (Bad)              (Bad)              (Bad)           │
│                                                             │
│  ┌──────────────┐                                           │
│  │   DEPLOY     │                                           │
│  │   SUCCESS    │ ← GOOD example only                       │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
```

## 🔐 Collaborators

To add collaborators:
1. Go to Settings → Collaborators
2. Add email or GitHub username
3. Select permission level
4. Send invitation

Suggested: r@iclassed.com for security team review

## 📖 Documentation

- `DEVSECOPS_GUIDE.md` - Complete file contents and pipeline logs
- `secure-app-good/README.md` - Good example details
- `secure-app-bad/README.md` - Bad example training guide

## 🎓 Usage Scenarios

### Security Training
Use the Bad example to teach common vulnerabilities

### CI/CD Learning
Study both pipelines to learn DevSecOps practices

### Code Review
Use Bad example in code review training

### Compliance
Demonstrate security scanning compliance

### Interview Preparation
Reference for security-focused engineering interviews

## ⚠️ Disclaimer

The **Bad example** is intentionally insecure for educational purposes.
**DO NOT DEPLOY OR USE IN PRODUCTION.**

The **Good example** represents production-ready patterns.

## 📞 Support

For questions or improvements:
- Review the code comments
- Check DEVSECOPS_GUIDE.md for detailed explanations
- Consult security best practices documentation

## 📄 License

This training repository is provided as-is for educational purposes.

---

**Last Updated:** April 11, 2026
**Repository:** https://github.com/leepascua/security-app
