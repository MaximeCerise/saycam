from ut_plots import plot_focus_map

for i in range(1,6):
    path = "results_yolo5s/vid"+str(i)+".csv"
    plot_focus_map(path)