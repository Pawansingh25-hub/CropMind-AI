
import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

SOURCE_DIR = Path("training_data")
OUTPUT_DIR = Path("dataset_split")

CLASSES = [
    "Tomato___Early_blight",
    "Tomato___healthy",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold"
]

# Safety check: original dataset must exist
if not SOURCE_DIR.exists():
    raise FileNotFoundError("training_data folder not found!")

# Prevent accidental deletion of an existing split
if OUTPUT_DIR.exists():
    raise FileExistsError(
        "dataset_split already exists. Rename or inspect it first."
    )

# Create output folders
for split in ["train", "val", "test"]:
    for class_name in CLASSES:
        (OUTPUT_DIR / split / class_name).mkdir(
            parents=True, exist_ok=True
        )

for class_name in CLASSES:
    class_dir = SOURCE_DIR / class_name

    images = sorted([
        p for p in class_dir.iterdir()
        if p.is_file() and p.suffix.lower() in
        [".jpg", ".jpeg", ".png", ".bmp"]
    ])

    if not images:
        raise ValueError(f"No images found in {class_dir}")

    # First: 70% train, 30% temporary
    train_images, temp_images = train_test_split(
        images,
        test_size=0.30,
        random_state=42
    )

    # Second: divide remaining 30% equally
    val_images, test_images = train_test_split(
        temp_images,
        test_size=0.50,
        random_state=42
    )

    split_data = {
        "train": train_images,
        "val": val_images,
        "test": test_images
    }

    for split_name, file_list in split_data.items():
        destination = OUTPUT_DIR / split_name / class_name

        for image_path in file_list:
            shutil.copy2(image_path, destination / image_path.name)

    print(
        f"{class_name}: "
        f"Train={len(train_images)}, "
        f"Val={len(val_images)}, "
        f"Test={len(test_images)}"
    )

print("\nDataset splitting completed successfully!")
print("Original training_data folder remains unchanged.")
