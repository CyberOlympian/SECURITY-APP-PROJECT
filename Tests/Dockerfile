# VULNERABLE: Using outdated Python version with known security issues
FROM python:3.8-stretch

# VULNERABILITY: Running as root (default)
# No USER directive = container runs with root privileges

WORKDIR /app

# VULNERABILITY: Installing packages with deprecated versions
COPY requirements.txt .
RUN pip install -r requirements.txt

# VULNERABILITY: Copy all files including sensitive data
COPY . .

# VULNERABILITY: Port exposed unnecessarily
EXPOSE 5000 8080 9000

# VULNERABILITY: Debug mode enabled
ENV FLASK_DEBUG=True
ENV FLASK_ENV=development

# NO HEALTHCHECK configured

# Running Flask in development mode via entrypoint
ENTRYPOINT ["python"]
CMD ["app/main.py"]
