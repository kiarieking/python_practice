#!/usr/bin/bash

echo "hello world"

pwd

python3 --version

python3 -m venv venv

. venv/bin/activate

pip install -r odoo_sandbox/requirements.txt
