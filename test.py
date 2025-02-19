from torchvision import transforms
from PIL import Image
import torch
import matplotlib.pyplot as plt
import numpy as np

# Charger le modèle
model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet50', pretrained=True)
model.eval()

# Charger une image
image_path = "im1.png"
image = Image.open(image_path).convert("RGB")

# Prétraitement de l'image
preprocess = transforms.Compose([
    transforms.ToTensor(),  # Convertir en tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalisation
])

input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)  # Ajouter une dimension de batch

# Déplacer sur GPU si disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
input_batch = input_batch.to(device)
model = model.to(device)

# Inférence
with torch.no_grad():
    output = model(input_batch)["out"][0]  # Récupérer la sortie du modèle

# Convertir la sortie en masque de segmentation
output_predictions = output.argmax(0)

# Visualiser le masque
plt.imshow(output_predictions.cpu(), cmap="viridis")
plt.show()
