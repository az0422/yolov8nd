# YOLOv8-ND
YOLOv8-ND: New Detection Algorithm for Fast and Lightweight Object Detection

## System Environment
* CPU: Xeon 4216 x2
* Memory: 192GB
* GPU: RTX A5000 x3
* OS: Ubuntu 22.04 LTS

## Performance and Comparison

| Models            | Size  | mAP50-95 (%)  | Params (M)| GFLOPs    | Speed<br><sup>CPU(ms) | Speed<br><sup>GPU(ms) |
|-------------------|-------|---------------|-----------|-----------|-----------------------|-----------------------|
| YOLOv8ndn         | 640   |               |           |           |                       |                       |
| YOLOv8nds         | 640   |               |           |           |                       |                       |
| YOLOv8ndm         | 640   |               |           |           |                       |                       |
| YOLOv8ndl         | 640   |               |           |           |                       |                       |
| YOLOv8ndx         | 640   |               |           |           |                       |                       |
|                   |       |               |           |           |                       |                       |
| YOLOv8n           | 640   | 37.5          | 8.7       | 8.9       |                       | 8.9                   |
| YOLOv8s           | 640   | 44.7          | 11.2      | 28.6      |                       | 9.1                   |
| YOLOv8m           | 640   | 50.1          | 25.9      | 78.9      |                       | 11.3                  |
| YOLOv8l           | 640   | 52.9          | 43.7      | 165.2     |                       | 13.4                  |
| YOLOv8x           | 640   | 54.0          | 68.2      | 257.8     |                       | 14.5                  |

Train parameters: `batch=16 epochs=500 optimizer=SGD lr0=0.01 momentum=0.937 data=coco.yaml`

Validation parameters: `data=coco.yaml batch=1 device=0|cpu`


## TODO
Prepare weights and compare


## Reference

Template from https://github.com/ultralytics/ultralytics (version: 8.1.25)
