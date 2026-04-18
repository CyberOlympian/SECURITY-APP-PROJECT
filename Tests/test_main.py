from App.main import app

- name: Install app dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt

- name: Set PYTHONPATH
  run: echo "PYTHONPATH=." >> $GITHUB_ENV
