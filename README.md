# DevSecOps Pipeline Training Repository

Complete practical DevSecOps demonstration repositories showcasing security best practices and common vulnerabilities.

## Repository Structure

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

## Example Pipeline Logs

See [DEVSECOPS_GUIDE.md](DEVSECOPS_GUIDE.md) for:
- Complete file contents
- Realistic successful pipeline execution logs
- Realistic failed pipeline execution logs
- Detailed vulnerability reports


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


## Tools Used

- **Flask** - Web framework
- **pytest** - Unit testing
- **Bandit** - SAST scanning
- **Safety** - Dependency scanning
- **Trivy** - Container scanning
- **Docker** - Containerization

## Pipeline Stages

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

## 📖 Documentation

- `DEVSECOPS_GUIDE.md` - Complete file contents and pipeline logs
- `secure-app-good/README.md` - Good example details



---

**Last Updated:** April 11, 2026
**Repository:** https://github.com/leepascua/security-app
