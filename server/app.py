import uuid
from flask import Flask, jsonify, request

from config import app
from models import Sortie, SortieSchema


if __name__ == '__main__':
    app.run(host='localhost')