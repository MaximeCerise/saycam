from ultralytics import YOLO
import pandas as pd
from ut_plots import plot_focus_map
from ut_yolo11 import predict_all_frames_yolo11

frames_dir = "vid_frames/vid5_frames"
model = YOLO('yolo11s.pt')
results_path = "results_yolo11s/"
pred = predict_all_frames_yolo11(model_yolo11=model, frames_dir=frames_dir)
df = pd.concat(pred).reset_index(drop=True)

df.to_csv(results_path + "vid5" + ".csv")
path = results_path + "vid5" + ".csv"