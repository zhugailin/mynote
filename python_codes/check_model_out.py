"查看模型的输出"

import torch
m = torch.load("/home/lyh/yolov5-6.1/runs/train/exp10/weights/best.pt")
print(m['model'].names)