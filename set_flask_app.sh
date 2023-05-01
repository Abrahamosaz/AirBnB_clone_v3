#!/usr/bin/env bash
mkdir web_dynamic
cp -r web_flask/static web_dynamic
cp -r web_flask/templates/100-hbnb.html web_dynamic
cp -r web_flask/__init__.py web_dynamic
cp -r web_flask/100-hbnb.py web_dynamic
mv web_dynamic/100-hbnb.py 0-hbnb.py
mv web_dynamic/100-hbnb.html 0-hbnb.html
sed s|/hbnb/|/0-hbnb/|  web_dynamic/0-hbnb.py
