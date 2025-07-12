from flask import Flask, request, jsonify
from predict import predict_text, predict_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

## Text Endpoint
@app.route("/predict-text", methods=["POST"])
def handle_text():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    prediction = predict_text(text)
    return jsonify({"prediction": prediction})

## Image Endpoint
@app.route("/predict-image", methods=["POST"])
def handle_image():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    image_file = request.files["image"]
    prediction = predict_image(image_file)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)