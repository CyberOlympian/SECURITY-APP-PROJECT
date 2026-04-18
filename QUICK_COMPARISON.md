# DevSecOps Examples - Quick Comparison

## 🎯 At a Glance

### ✅ GOOD Example
```
Status: ✅ PASSING
├── Code: Secure & Validated
├── Tests: 15 tests, 100% pass, 97% coverage
├── Dependencies: 0 CVEs
├── Container: 156MB, non-root user
├── Pipeline: All 5 stages pass ✅
└── Result: Ready for production! 🚀
```

### ❌ BAD Example
```
Status: ❌ FAILING
├── Code: Vulnerable (6 issues)
├── Tests: 8 tests, 62% pass (3 fail)
├── Dependencies: 5 CVEs
├── Container: 892MB, runs as root
├── Pipeline: 3 stages fail ❌
└── Result: NOT ready for production ⛔
```

---

## 📊 Visual Comparison

```
METRIC                  GOOD ✅           BAD ❌
────────────────────────────────────────────────────
Input Validation        ✅ Full           ❌ None
Email Logic            ✅ Correct         ❌ Inverted
Security Headers       ✅ Present         ❌ Missing
Error Handling         ✅ Safe            ❌ Leaky
Tests Count            ✅ 15              ❌ 8
Test Pass Rate         ✅ 100%            ❌ 62%
Code Coverage          ✅ 97%             ❌ Unknown
Dependencies CVEs      ✅ 0               ❌ 5
Container Base         ✅ Python 3.12     ❌ Python 3.8 (EOL)
Container Size         ✅ 156MB           ❌ 892MB
Container User         ✅ appuser         ❌ root
Health Check           ✅ Yes             ❌ No
Dep Scan               ✅ PASS (0 vulns)  ❌ FAIL (5 vulns)
Unit Tests             ✅ PASS (15/15)    ❌ FAIL (5/8)
Container Build        ✅ PASS            ✅ PASS
Container Scan         ✅ PASS (0 vulns)  ❌ FAIL (47 vulns)
Deploy Status          ✅ SUCCESS         ❌ FAILED
────────────────────────────────────────────────────
```

---

## 🔑 Key Files

### GOOD Example - Review These:
```
good-example/
├── ✅ app/main.py              - Study: Input validation patterns
├── ✅ tests/test_main.py       - Study: Security testing
├── ✅ requirements.txt         - Study: Dependency management
├── ✅ Dockerfile               - Study: Container security
└── ✅ PIPELINE_LOGS_SUCCESS.md - Study: Successful pipeline
```

### BAD Example - Review These:
```
bad-example/
├── ❌ app/main.py              - Study: What NOT to do
├── ❌ tests/test_main.py       - Study: Test failures
├── ❌ requirements.txt         - Study: CVE discovery
├── ❌ Dockerfile               - Study: Security risks
└── ❌ PIPELINE_LOGS_FAILURE.md - Study: Failure scenarios
```

---

## 💡 Main Differences

### Code Security
```
GOOD: if not email or len(email) > 254:
          return error
      if '@' not in email: ... return invalid
      else: ... return valid
      ✅ Correct logic

BAD:  if not email:
          raise ValueError(...)  # Exception leaked!
      if email.count('@') != 1:
          return valid             ❌ Wrong!
      else: return invalid        ❌ Wrong!
      ❌ Inverted logic + info disclosure
```

### Dependencies
```
GOOD: Flask==3.0.0      (Latest, no CVEs)
      Werkzeug==3.0.1   (Latest, no CVEs)
      Total: 0 CVEs ✅

BAD:  Flask==2.0.1      (CVE-2021-22885, CVE-2021-22886, +1)
      Werkzeug==2.0.0   (CVE-2021-21241, CVE-2021-3020)
      Total: 5 CVEs ❌
```

### Container
```
GOOD: python:3.12-slim          ✅ Modern, minimal
      156MB                      ✅ Small
      Non-root user             ✅ Secure
      Health check              ✅ Present

BAD:  python:3.8-stretch        ❌ Old, EOL
      892MB                      ❌ Large
      root user                 ❌ Dangerous
      No health check           ❌ Missing
      38 base image vulns       ❌ Critical
```

---

## 🧪 Test Results

### GOOD Example Tests:
```
✅ TestHealthEndpoint::test_health_check
✅ TestGetUser::test_get_user_valid_id
✅ TestGetUser::test_get_user_invalid_negative_id
✅ TestGetUser::test_get_user_invalid_large_id
✅ TestValidateEmail::test_validate_email_valid
✅ TestValidateEmail::test_validate_email_invalid_format
✅ TestValidateEmail::test_validate_email_empty
✅ TestValidateEmail::test_validate_email_wrong_content_type
✅ TestProcessData::test_process_data_string
✅ TestProcessData::test_process_data_integer
✅ TestProcessData::test_process_data_string_too_long
✅ TestProcessData::test_process_data_invalid_type
✅ TestErrorHandling::test_404_not_found
✅ TestSecurityHeaders::test_security_headers_present
✅ TestSecurityHeaders::test_security_headers_configured

RESULT: 15 passed ✅ (97% coverage)
```

### BAD Example Tests:
```
✅ TestHealthEndpoint::test_health_check
✅ TestGetUser::test_get_user_valid_id
❌ TestValidateEmail::test_validate_email_valid
   → AssertionError: assert False is True
   → Email marked as INVALID (should be VALID)
❌ TestValidateEmail::test_validate_email_invalid_format
   → AssertionError: assert True is False
   → Email marked as VALID (should be INVALID)
❌ TestValidateEmail::test_validate_email_multiple_at_signs
   → AssertionError: assert True is False
   → Same validation bug

✅ TestProcessData::test_process_data_simple
✅ TestErrorHandling::test_missing_email_field

RESULT: 5 passed, 3 failed ❌ (62% pass rate)
CAUSE: Inverted email validation logic
```

---

## 🔒 Vulnerabilities at a Glance

### GOOD Example Security Issues:
```
Total vulnerabilities: 0 ✅
- Code vulnerabilities: 0 ✅
- Dependency CVEs: 0 ✅
- Container vulnerabilities: 0 ✅

Status: SECURE FOR PRODUCTION ✅
```

### BAD Example Security Issues:
```
Total vulnerabilities: 6 code + 5 CVEs + 47 container = 58 ❌

Code Issues (6):
  1. ❌ Inverted email validation logic
  2. ❌ Command injection (shell=True)
  3. ❌ Unsafe pickle deserialization (RCE)
  4. ❌ Path traversal in uploads
  5. ❌ Information disclosure (exceptions)
  6. ❌ SQL injection risk

Dependency CVEs (5):
  1. ❌ Flask 2.0.1: Path traversal
  2. ❌ Flask 2.0.1: CSRF bypass
  3. ❌ Werkzeug 2.0.0: Pickle RCE
  4. ❌ Werkzeug 2.0.0: Path traversal
  5. ❌ requests 2.25.1: DoS

Container Vulnerabilities (47):
  - Base image: 38 vulnerabilities
  - Packages: 9 vulnerabilities
  - Critical: 8
  - High: 28

Status: NOT SAFE FOR PRODUCTION ⛔
```

---

## 🚀 Pipeline Results

### GOOD Example Pipeline:
```
┌─────────────────────────┐
│ Dependency Scan         │
│ ✅ 0 vulnerabilities    │
│ Status: PASS            │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Unit Tests              │
│ ✅ 15/15 passed         │
│ ✅ 97% coverage         │
│ Status: PASS            │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Container Build         │
│ ✅ Image built          │
│ ✅ 156MB                │
│ Status: PASS            │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Container Scan          │
│ ✅ 0 vulnerabilities    │
│ ✅ Non-root user        │
│ Status: PASS            │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Deploy                  │
│ ✅ All checks passed    │
│ ✅ READY FOR PROD       │
│ Status: SUCCESS         │
└─────────────────────────┘

OVERALL: ✅ ALL PASS - DEPLOY!
```

### BAD Example Pipeline:
```
┌─────────────────────────┐
│ Dependency Scan         │
│ ❌ 5 vulnerabilities    │
│ ❌ 3 HIGH, 2 CRITICAL   │
│ Status: FAIL ❌         │
└————————————┬─────────────┘
             ↓
┌─────────────────────────┐
│ Unit Tests              │
│ ❌ 5/8 passed           │
│ ❌ 3 tests failed       │
│ Status: FAIL ❌         │
└———————————┬──────────────┘
             ↓
┌─────────────────────────┐
│ Container Build         │
│ ⚠️ Image built anyways  │
│ ⚠️ 892MB (insecure)     │
│ Status: PASS (warning)  │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Container Scan          │
│ ❌ 47 vulnerabilities   │
│ ❌ 8 CRITICAL found     │
│ ❌ Running as root      │
│ Status: FAIL ❌         │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Deploy                  │
│ ⏭️ SKIPPED              │
│ (dependencies failed)   │
│ Status: SKIPPED         │
└─────────────────────────┘

OVERALL: ❌ FAILED - DO NOT DEPLOY!
```

---

## 📚 Where to Find Things

| What | Where | Why |
|------|-------|-----|
| Overview | [INDEX.md](INDEX.md) | Start here |
| Full comparison | [README_COMPLETE_GUIDE.md](README_COMPLETE_GUIDE.md) | Detailed analysis |
| All code | [FILE_REFERENCE.md](FILE_REFERENCE.md) | Code review |
| GitHub setup | [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) | How to share |
| Success logs | [good-example/PIPELINE_LOGS_SUCCESS.md](good-example/PIPELINE_LOGS_SUCCESS.md) | What works |
| Failure logs | [bad-example/PIPELINE_LOGS_FAILURE.md](bad-example/PIPELINE_LOGS_FAILURE.md) | What fails |
| Secure code | [good-example/app/main.py](good-example/app/main.py) | Best practices |
| Vulnerable code | [bad-example/app/main.py](bad-example/app/main.py) | Anti-patterns |

---

## ✨ Summary

| Aspect | GOOD | BAD | Learn |
|--------|------|-----|-------|
| **Tests** | 15 pass | 3 fail | Bugs break tests |
| **Code** | Secure | 6 issues | Validation matters |
| **Deps** | 0 CVEs | 5 CVEs | Keep deps updated |
| **Container** | 156MB | 892MB | Use slim images |
| **User** | Non-root | Root | Security matters |
| **Pipeline** | All pass | 3 fail | Automation catches bugs |

---

## 🎯 Quick Actions

1. **Learn**: Read [README_COMPLETE_GUIDE.md](README_COMPLETE_GUIDE.md)
2. **Review**: Compare code files side-by-side
3. **Understand**: Read pipeline execution logs
4. **Share**: Follow [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md)
5. **Deploy**: Push to GitHub and watch pipelines run

---

**Everything Ready**: ✅  
**Time to Act**: Now! 🚀
