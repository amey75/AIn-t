import numpy as np

## Text model
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch

text_model_path = "./text_model" 

# Load tokenizer and model
text_tokenizer = DistilBertTokenizerFast.from_pretrained(text_model_path)
text_model = DistilBertForSequenceClassification.from_pretrained(text_model_path)
text_model.eval() 

def predict_text(text: str):
    inputs = text_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = text_model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1).numpy()
    label = np.argmax(probs, axis=1)[0]
    return "AI-Generated" if label == 1 else "Real"


## Image Model
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load the full model (architecture + weights)
image_model = load_model("cnn_model.h5")  # update path if needed

def predict_image(file):
    # Read image from Flask file upload
    np_img = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Resize and preprocess
    img = cv2.resize(img, (32, 32))  
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    prob = image_model.predict(img)[0][0]
    label = int(prob > 0.5)
    return "AI-generated" if label == 1 else "Real"