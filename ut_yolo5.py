import torch
import os
from glob import glob

def predict_yolo(model_yolo, img):
    results = model_yolo(img)
    return results.pandas().xyxy[0]

def get_path_frames(frames_dir):
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif")
    images = []
    for ext in extensions:
        images.extend(glob(os.path.join(frames_dir, ext)))
    for img_path in images:
        print(f"Traitement de : {img_path}")
    return images

def predict_all_frames(model_yolo, frames_dir):
    frames = get_path_frames(frames_dir=frames_dir)
    predictions = []
    for frame in frames :
        predictions.append(predict_yolo(model_yolo,frame))
    return predictions
