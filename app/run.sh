#!/bin/bash

pip install flask
pip insall -U flask-cors
npm install vue

python3 app/backend/main.py & cd app/frontend && npm run serve