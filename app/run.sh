#!/bin/bash

pip install flask
pip insall flask-cors
npm install vue

python3 app/backend/main.py & cd app/frontend && npm run serve