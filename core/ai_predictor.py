
import json
from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "crop_disease_model.keras"
LABELS_PATH = BASE_DIR / "class_labels.json"

IMAGE_SIZE = (128, 128)

# Load model and labels once
model = tf.keras.models.load_model(MODEL_PATH)

with open(LABELS_PATH, "r", encoding="utf-8-sig") as file:
    CLASS_LABELS = json.load(file)


def predict_leaf_disease(image_file):
    """
    Predict the class of a tomato leaf image.

    Returns:
        dict containing disease name and confidence percentage.
    """
    with Image.open(image_file) as image:
        image = image.convert("RGB")
        image = image.resize(IMAGE_SIZE)

        image_array = np.array(image, dtype=np.float32)
        image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)[0]

    predicted_index = int(np.argmax(predictions))
    confidence = float(predictions[predicted_index]) * 100

    return {
        "class_name": CLASS_LABELS[predicted_index],
        "confidence": round(confidence, 2),
    }
