"""
John Doe's Flask API.
"""
import os
import configparser
from flask import Flask,abort,send_from_directory,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"


@app.route("/<string:file>")
def files(file):
    try:
        if "~" in file or ".." in file:
            return send_from_directory("pages/","403.html"),403
        return send_from_directory("pages/",file),200
    except:
        return send_from_directory("pages/","404.html"),404
    


def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
port = config["SERVER"]["PORT"]
debug = config["SERVER"]["DEBUG"]






if __name__ == "__main__":
    app.run(debug=debug, host='0.0.0.0',port=port)
