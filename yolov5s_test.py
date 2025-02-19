from ut_yolo5 import predict_yolo
from ut_yolo5 import predict_all_frames
import torch
import pandas as pd
from plots_results import plot_focus_map

#extract frames from the video

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

for i in range(1,2):
    frames_dir = "extracted_frames/vid"+str(i)
    results_path = "results_yolo5s/"
    pred = predict_all_frames(model, frames_dir)
    df = pd.concat(pred).reset_index(drop=True)
    df.to_csv(results_path + "vid"+str(i) + ".csv")
    path = results_path + "vid"+str(i) + ".csv"
    plot_focus_map(path)
