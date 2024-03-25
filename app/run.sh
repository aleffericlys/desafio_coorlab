#!/bin/bash

pip install flask
pip install flask-cors

python3 app/backend/main.py & cd app/frontend && npm install && npm run serve