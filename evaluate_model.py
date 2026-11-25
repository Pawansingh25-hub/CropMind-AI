
import tensorflow as tf
import numpy as np
import json
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Paths
TEST_DIR = Path("dataset_split/test")
MODEL_PATH = Path("crop_disease_model.keras")

IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32

print("Loading trained CNN model...")

# Load best saved model
model = tf.keras.models.load_model(MODEL_PATH)

# Load class labels
with open("class_labels.json", "r") as file:
    class_names = json.load(file)

print("Classes:", class_names)

# Load independent test dataset
print("\nLoading test dataset...")

test_ds = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# Check class order
if test_ds.class_names != class_names:
    raise ValueError(
        "Class order mismatch between model and test dataset!"
    )

# Get true labels
y_true = np.concatenate([
    labels.numpy() for images, labels in test_ds
])

# Get predictions
print("\nGenerating predictions...")

y_prob = model.predict(test_ds)
y_pred = np.argmax(y_prob, axis=1)

# Calculate metrics
accuracy = accuracy_score(y_true, y_pred)

print("\n========== MODEL EVALUATION ==========")

print(f"Test Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:\n")

report = classification_report(
    y_true,
    y_pred,
    labels=range(len(class_names)),
    target_names=class_names,
    zero_division=0
)

print(report)

# Confusion Matrix
cm = confusion_matrix(
    y_true,
    y_pred,
    labels=range(len(class_names))
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)

fig, ax = plt.subplots(figsize=(10, 8))

display.plot(
    cmap="Blues",
    xticks_rotation=45,
    ax=ax
)

plt.title("CropMind AI - CNN Confusion Matrix")
plt.tight_layout()

plt.savefig(
    "confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Save numerical results
results = {
    "test_accuracy": round(float(accuracy * 100), 2),
    "test_images": int(len(y_true)),
    "class_names": class_names,
    "confusion_matrix": cm.tolist()
}

with open("evaluation_results.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nEvaluation completed successfully!")
print("Confusion matrix saved: confusion_matrix.png")
print("Results saved: evaluation_results.json")
