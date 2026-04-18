from App.main import app

- name: Run unit tests with coverage
  run: |
    pytest -v --cov=App --cov-report=term-missing --cov-report=html --tb=short
