# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Run a Flask REST API exposing one or more YOLOv5s models
"""

import argparse
from PIL import Image
import io
import torch
from flask import Flask, request, jsonify
import base64,json

app = Flask(__name__)
models = {}


@app.route('/', methods=["GET"])
def index():
    return "<h1>Hello, yolo v5!</h1>"


@app.route('/persons', methods=["POST"])
def analyze():
    if request.method != "POST":
        return
    instances = request.get_json()['img']
    results = []
    if instances and len(instances) > 0:
        for instance in instances:
            encoded_data = instance.split(',')[1]
            im = Image.open(io.BytesIO(base64.b64decode(encoded_data)))
            ai_results = models['yolov5s'](im, size=320)  # reduce size=320 for faster inference
            input_dict = json.loads(ai_results.pandas().xyxy[0].to_json(orient="records"))
            output_dict = [x for x in input_dict if x['name'] == 'person']
            results.append(len(output_dict))
            print(len(output_dict))
    return jsonify(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=1235, type=int, help="port number")
    parser.add_argument('--model', nargs='+', default=['yolov5s'], help='model(s) to run, i.e. --model yolov5n yolov5s')
    opt = parser.parse_args()

    for m in opt.model:
        models[m] = torch.hub.load("ultralytics/yolov5", m, force_reload=True, skip_validation=True)

    app.run(host="0.0.0.0", port=opt.port)  # debug=True causes Restarting with stat
