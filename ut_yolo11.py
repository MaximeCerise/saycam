from ultralytics import YOLO
import pandas as pd
import os
from glob import glob

def predict_yolo11(model_yolo11, img):
    # Access the detection results
    # The output is a list of Results objects (one for each image)
    # For a single image, we take the first element of the list
    results = model_yolo11(img)[0]

    # Convert results to a pandas DataFrame
    # Extract bounding boxes, confidence scores, and class labels
    boxes = results.boxes.xyxy.cpu().numpy()  # Bounding boxes in [x1, y1, x2, y2] format
    confidences = results.boxes.conf.cpu().numpy()  # Confidence scores
    class_ids = results.boxes.cls.cpu().numpy()  # Class IDs
    class_names = [results.names[int(cls_id)] for cls_id in class_ids]  # Class names

    # Create a DataFrame
    results_df = pd.DataFrame({
        'xmin': boxes[:, 0],  # xmin = x1
        'ymin': boxes[:, 1],  # ymin = y1
        'xmax': boxes[:, 2],  # xmax = x2
        'ymax': boxes[:, 3],  # ymax = y2
        'confidence': confidences,  # Score de confiance
        'class': class_ids,  # ID de la classe
        'name': class_names  # Nom de la classe
    })
    return results_df

def get_path_frames_yolo11(frames_dir):
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif")
    frames = []
    for ext in extensions:
        frames.extend(glob(os.path.join(frames_dir, ext)))
    for img_path in frames:
        print(f"Traitement de : {img_path}")
    return frames

def predict_all_frames_yolo11(model_yolo11, frames_dir):
    frames = get_path_frames_yolo11(frames_dir=frames_dir)
    predictions = []
    for frame in frames :
        predictions.append(predict_yolo11(model_yolo11,frame))
    return predictions