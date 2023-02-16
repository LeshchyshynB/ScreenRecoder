import cv2
from datetime import datetime
path = "F:/Records_video/"
video_format = ".mp4"#.avi | .mp4 |
codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')#*'XVID' | *'mp4v' | 'm', 'p', '4', 'v' | *'MJPG'
resolution = (1366, 768)
x = 0
y = 0
x2, y2 = resolution
pos = {"x": x, "y": y, "x2": x2-x, "y2": y2-y}
mon = (pos["y"], pos["x"], pos["x2"], pos["y2"])
filename = str(input("-Video name?-\n:> "))
if filename:
	path = path + filename + video_format
else:
	path = path + str(datetime.now()) + video_format
fps = 60
out = cv2.VideoWriter(path, codec, fps, resolution)