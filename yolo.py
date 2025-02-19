import torch
# Charger YOLOv5 depuis torch.hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' est une version légère

# Charger une image
img = "im1.png"

# Faire une prédiction
results = model(img)

# Afficher les résultats
results.show()  # Affiche l'image avec les boîtes englobantes
print(results.pandas().xyxy[0])  # Affiche les détections sous forme de tableau

