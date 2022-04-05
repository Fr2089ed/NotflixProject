from flask import Flask
import sqlite3,
app = Flask(__name__)
accounts = sqlite3.connect("accounts.db")
videos = sqlite3.connect("videos.db")