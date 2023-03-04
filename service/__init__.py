from flask import Flask
from flask_cors import CORS
import logging
import misc

app = Flask(__name__,
    static_folder = '../static',
    static_url_path = '/_service/static',
    template_folder = '../templates',
)

CORS(app, origins = "*", supports_credentials = True)

# Load All Submodules
import service.join