# ============================================================
# INDIAN CATTLE BREED AI
# V4 EFFICIENTNET-B0 MODEL
# ============================================================

import os

import torch
import torch.nn as nn

from PIL import Image

from torchvision import transforms
from torchvision.models import efficientnet_b0


# ============================================================
# MODEL PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "V4_EfficientNetB0_best.pth"
)


# ============================================================
# DEVICE
# ============================================================

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)


# ============================================================
# CHECK MODEL
# ============================================================

if not os.path.exists(MODEL_PATH):

    raise FileNotFoundError(
        "\n"
        "V4 MODEL NOT FOUND!\n\n"
        f"Expected location:\n{MODEL_PATH}\n\n"
        "Please place:\n"
        "V4_EfficientNetB0_best.pth\n"
        "inside backend/models/\n"
    )


# ============================================================
# LOAD CHECKPOINT
# ============================================================

print("=" * 70)
print("Loading Indian Cattle AI V4 model...")
print("=" * 70)

checkpoint = torch.load(
    MODEL_PATH,
    map_location=device
)


# ============================================================
# CHECK CHECKPOINT
# ============================================================

if "class_names" not in checkpoint:

    raise KeyError(
        "Checkpoint does not contain 'class_names'."
    )


if "num_classes" not in checkpoint:

    raise KeyError(
        "Checkpoint does not contain 'num_classes'."
    )


if "model_state_dict" not in checkpoint:

    raise KeyError(
        "Checkpoint does not contain 'model_state_dict'."
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

class_names = checkpoint["class_names"]

num_classes = checkpoint["num_classes"]


# Convert class names to normal Python list
class_names = list(class_names)


# ============================================================
# VALIDATE CHECKPOINT
# ============================================================

if num_classes != len(class_names):

    raise ValueError(
        "Checkpoint class mismatch!\n"
        f"num_classes = {num_classes}\n"
        f"class_names = {len(class_names)}"
    )


# ============================================================
# CREATE EFFICIENTNET-B0
# ============================================================

model = efficientnet_b0(
    weights=None
)


# Replace classifier
model.classifier[1] = nn.Linear(
    model.classifier[1].in_features,
    num_classes
)


# ============================================================
# LOAD TRAINED WEIGHTS
# ============================================================

model.load_state_dict(
    checkpoint["model_state_dict"]
)


# ============================================================
# MOVE MODEL
# ============================================================

model = model.to(device)


# ============================================================
# EVALUATION MODE
# ============================================================

model.eval()


# ============================================================
# IMAGE TRANSFORMATION
# ============================================================

transform = transforms.Compose([

    transforms.Resize(
        (224, 224)
    ),

    transforms.ToTensor(),

    transforms.Normalize(

        mean=[
            0.485,
            0.456,
            0.406
        ],

        std=[
            0.229,
            0.224,
            0.225
        ]
    )
])


# ============================================================
# MODEL INFORMATION
# ============================================================

print("MODEL LOADED SUCCESSFULLY")
print("-" * 70)

print("Model path:")
print(MODEL_PATH)

print("Device:")
print(device)

print("Model:")
print("EfficientNet-B0")

print("Number of classes:")
print(num_classes)

if "best_val_accuracy" in checkpoint:

    print(
        "Best validation accuracy:",
        checkpoint["best_val_accuracy"]
    )

print("\nFirst classes:")

for i, name in enumerate(
    class_names[:10]
):

    print(
        f"{i}: {name}"
    )

print("=" * 70)


# ============================================================
# PREDICT BREED
# ============================================================

def predict_breed(
    image: Image.Image
):

    # --------------------------------------------------------
    # CHECK IMAGE
    # --------------------------------------------------------

    if image is None:

        raise ValueError(
            "Image is None."
        )


    # --------------------------------------------------------
    # CONVERT RGB
    # --------------------------------------------------------

    if image.mode != "RGB":

        image = image.convert(
            "RGB"
        )


    # --------------------------------------------------------
    # TRANSFORM IMAGE
    # --------------------------------------------------------

    image_tensor = (

        transform(image)

        .unsqueeze(0)

        .to(device)
    )


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    with torch.no_grad():

        outputs = model(
            image_tensor
        )

        probabilities = torch.softmax(
            outputs,
            dim=1
        )


    # --------------------------------------------------------
    # TOP 3
    # --------------------------------------------------------

    k = min(
        3,
        num_classes
    )

    top_probabilities, top_indices = torch.topk(
        probabilities,
        k=k,
        dim=1
    )


    # --------------------------------------------------------
    # BUILD TOP PREDICTIONS
    # --------------------------------------------------------

    top_predictions = []


    for probability, index in zip(

        top_probabilities[0],

        top_indices[0]
    ):

        class_index = index.item()

        breed_name = class_names[
            class_index
        ]

        confidence = round(
            probability.item() * 100,
            2
        )


        top_predictions.append({

            "breed": breed_name,

            "confidence": confidence
        })


    # --------------------------------------------------------
    # BEST PREDICTION
    # --------------------------------------------------------

    best_prediction = top_predictions[0]


    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    return {

        "breed":
            best_prediction["breed"],

        "confidence":
            best_prediction["confidence"],

        "top_3":
            top_predictions
    }