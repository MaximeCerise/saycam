from ut_yolo5 import predict_yolo
from ut_yolo5 import predict_all_frames
import torch
import pandas as pd
from ut_plots import plot_focus_map

#extract frames from the video
for i in range(1,6):
    frames_dir = "vid_frames/vid"+str(i)+"_frames"
    results_path = "results_yolo5s/"
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' est une 
    pred = predict_all_frames(model, frames_dir)
    df = pd.concat(pred).reset_index(drop=True)
    df.to_csv(results_path + "vid"+str(i) + ".csv")
    path = results_path + "vid"+str(i) + ".csv"
    #plot_focus_map(path)
