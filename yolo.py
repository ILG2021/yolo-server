import argparse
import base64
import io
import json
import yolov7
from PIL import Image
from flask import Flask, request, jsonify

app = Flask(__name__)
yolo_model = None


@app.route('/', methods=["GET"])
def index():
    return "<h1>Hello, yolo v5!</h1>"


@app.route('/persons', methods=["POST"])
def persons():
    if request.method != "POST":
        return
    instances = request.get_json()['img']
    results = []
    if instances and len(instances) > 0:
        for instance in instances:
            encoded_data = instance.split(',')[1]
            im = Image.open(io.BytesIO(base64.b64decode(encoded_data)))
            ai_results = yolo_model(im, size=320)  # reduce size=320 for faster inference
            input_dict = json.loads(ai_results.pandas().xyxy[0].to_json(orient="records"))
            output_dict = [x for x in input_dict if x['name'] == 'person']
            results.append(len(output_dict))
            print(len(output_dict))
    return jsonify(results)

@app.route('/objects', methods=["POST"])
def objects():
    if request.method != "POST":
        return
    instances = request.get_json()['img']
    results = []
    if instances and len(instances) > 0:
        for instance in instances:
            encoded_data = instance.split(',')[1]
            im = Image.open(io.BytesIO(base64.b64decode(encoded_data)))
            ai_results = yolo_model(im, size=320)  # reduce size=320 for faster inference
            input_dict = json.loads(ai_results.pandas().xyxy[0].to_json(orient="records"))
            results.append(input_dict)
    return json.dumps(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=1235, type=int, help="port number")
    opt = parser.parse_args()

    yolo_model = yolov7.load('yolov7.pt')
    app.run(host="0.0.0.0", port=opt.port)  # debug=True causes Restarting with stat
