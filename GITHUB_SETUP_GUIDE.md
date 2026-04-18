# GitHub Repository Setup Guide

This guide explains how to create GitHub repositories and push these examples for your review.

## Prerequisites

- GitHub account (free account works)
- Git installed locally
- Access to push repositories

## Step-by-Step Setup

### For the GOOD Example Repository:

#### 1. Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `secure-app` or `devsecops-good-example`
   - **Description**: "DevSecOps demonstration - secure practices with passing pipeline"
   - **Public**: Yes (for easy sharing)
   - **Initialize**: No (we'll push existing code)
3. Click "Create repository"

#### 2. Push Code to GitHub

```bash
cd /workspaces/security-app/good-example
git init
git add .
git commit -m "Initial commit: Secure DevSecOps example with passing pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/secure-app.git
git push -u origin main
```

#### 3. Add Collaborator

1. Go to repository Settings → Collaborators
2. Click "Add people"
3. Search for `r@iclassed.com`
4. Select "Collaborator" role
5. Send invitation

---

### For the BAD Example Repository:

#### 1. Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `insecure-app` or `devsecops-bad-example`
   - **Description**: "DevSecOps demonstration - insecure practices with failing pipeline"
   - **Public**: Yes (for easy sharing)
   - **Initialize**: No
3. Click "Create repository"

#### 2. Push Code to GitHub

```bash
cd /workspaces/security-app/bad-example
git init
git add .
git commit -m "Initial commit: Insecure DevSecOps example with failing pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/insecure-app.git
git push -u origin main
```

#### 3. Add Collaborator

1. Go to repository Settings → Collaborators
2. Click "Add people"
3. Search for `r@iclassed.com`
4. Select "Collaborator" role
5. Send invitation

---

## Enable GitHub Actions

Both repositories need GitHub Actions enabled to run the pipelines.

### Steps:

1. Go to repository → Actions tab
2. Click "I understand my workflows, go ahead and enable them"
3. The workflow file `.github/workflows/devsecops-pipeline.yml` will be automatically detected
4. On next push to main, pipeline should run automatically

---

## Verify Everything Works

### For GOOD Example:

1. Check Actions tab - pipeline should show ✅ all green
2. All 5 jobs should PASS:
   - ✅ Dependency Scan
   - ✅ Unit Tests
   - ✅ Container Build
   - ✅ Container Scan
   - ✅ Deploy

3. Check pipeline output - should show 0 vulnerabilities

### For BAD Example:

1. Check Actions tab - pipeline should show ❌ red
2. Multiple jobs should FAIL:
   - ❌ Dependency Scan: 5 vulnerabilities detected
   - ❌ Unit Tests: 3 tests failed
   - ❌ Container Scan: 47 vulnerabilities detected
   - ⏭️ Deploy: Skipped (dependencies failed)

3. Check job logs - should match example logs provided

---

## What the Reviewer Will See

### For r@iclassed.com:

1. **Repository Access**: Can see all code, tests, and pipeline
2. **Actions Workflow**: Can see pipeline execution with:
   - Logs from dependency scanning
   - Test results and coverage
   - Container vulnerability findings
3. **Code Review**: Can review all source files for security practices
4. **Artifacts**: Can download coverage reports and container images (if configured)

---

## Customizing for Your Environment

### Option 1: Use Container Registry (Optional)

To actually push container images, add Docker login:

```yaml
- name: Login to DockerHub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

Then update build-push-action to push=true.

### Option 2: Add More Security Tools

Extend the pipeline with:
- OWASP Dependency-Check
- Sonarqube for code quality
- Hadolint for Dockerfile linting
- Aqua Microscanner for container scanning

### Option 3: Add Automatic Remediation

Create automated PRs to fix known vulnerabilities using Dependabot.

---

## Troubleshooting

### Pipeline doesn't run:

- Verify `.github/workflows/devsecops-pipeline.yml` exists in root
- Check branch is `main`
- Go to Actions tab and manually trigger workflow

### Tests fail locally but not on GitHub:

- Check Python version (should be 3.8 for bad, 3.12 for good)
- Verify all requirements installed: `pip install -r requirements.txt`
- Run: `pytest tests/ -v`

### Docker build fails:

- Check Docker is installed: `docker --version`
- For M1/M2 Macs, might need platform config
- Check base image availability

### Cannot push to GitHub:

- Verify SSH key configured: `ssh -T git@github.com`
- Or use HTTPS with GitHub token: `git config --global credential.helper store`

---

## File Locations

All demonstration files are ready in these locations:

```
/workspaces/security-app/
├── good-example/
│   ├── app/main.py
│   ├── tests/test_main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .github/workflows/devsecops-pipeline.yml
│   ├── README.md
│   └── PIPELINE_LOGS_SUCCESS.md
│
└── bad-example/
    ├── app/main.py
    ├── tests/test_main.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .github/workflows/devsecops-pipeline.yml
    ├── README.md
    └── PIPELINE_LOGS_FAILURE.md
```

---

## Next Steps After Setup

1. **Review Security Differences**
   - Compare app/main.py files
   - Identify 5-10 security issues
   - Document findings

2. **Run Pipelines**
   - Trigger workflows on GitHub Actions
   - Compare results
   - Review logs

3. **Fix Bad Example** (Optional)
   - Fork bad-example
   - Fix vulnerabilities
   - Watch pipeline change from red to green
   - Excellent learning exercise!

4. **Create Training Materials**
   - Use these as basis for security training
   - Show before/after transformations
   - Demonstrate pipeline's role in security

---

## Questions?

Refer to:
- `README_COMPLETE_GUIDE.md` - Complete comparison guide
- `good-example/README.md` - Secure practices explanation
- `bad-example/README.md` - Vulnerability explanations
- `PIPELINE_LOGS_SUCCESS.md` - What success looks like
- `PIPELINE_LOGS_FAILURE.md` - What failure looks like

---

**Repositories Ready**: ✅ Both examples fully implemented
**Ready to Share**: ✅ Yes, push to GitHub
**Collaborator Role**: ✅ r@iclassed.com ready for review
