
import matplotlib.pyplot as plt

# Epoch numbers
epochs = range(1, 16)

# Actual training results from terminal output
train_accuracy = [
    45.56, 64.80, 70.38, 72.53, 74.73,
    76.02, 78.24, 82.31, 83.98, 84.22,
    86.87, 87.29, 89.94, 90.14, 91.80
]

val_accuracy = [
    60.88, 73.84, 69.68, 72.74, 76.16,
    74.82, 74.94, 85.45, 81.66, 86.80,
    85.82, 83.01, 91.32, 91.32, 85.57
]

train_loss = [
    1.2014, 0.8126, 0.6874, 0.6165, 0.5769,
    0.5518, 0.5097, 0.4504, 0.4082, 0.3923,
    0.3360, 0.3251, 0.2821, 0.2635, 0.2318
]

val_loss = [
    0.9086, 0.6450, 0.6213, 0.6191, 0.5538,
    0.6083, 0.6071, 0.4014, 0.4469, 0.3632,
    0.3725, 0.4713, 0.2798, 0.2825, 0.4492
]

# Graph 1: Accuracy
plt.figure(figsize=(9, 5))

plt.plot(
    epochs,
    train_accuracy,
    marker="o",
    label="Training Accuracy"
)

plt.plot(
    epochs,
    val_accuracy,
    marker="o",
    label="Validation Accuracy"
)

plt.title("CropMind AI - Training vs Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy (%)")
plt.xticks(list(epochs))
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("training_accuracy.png", dpi=300)
plt.show()

# Graph 2: Loss
plt.figure(figsize=(9, 5))

plt.plot(
    epochs,
    train_loss,
    marker="o",
    label="Training Loss"
)

plt.plot(
    epochs,
    val_loss,
    marker="o",
    label="Validation Loss"
)

plt.title("CropMind AI - Training vs Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(list(epochs))
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("training_loss.png", dpi=300)
plt.show()

print("Training graphs generated successfully!")
print("1. training_accuracy.png")
print("2. training_loss.png")
