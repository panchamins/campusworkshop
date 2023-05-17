"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi8143hp8u7g2egps70-a.oregon-postgres.render.com",
        database="todo_bm9r",
        user="root",
        password="YlxtBX6hu6mv4kvjzWEaph0U5CP4YoRb")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
