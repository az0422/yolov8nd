# YOLOv8-ND
YOLOv8-ND: New Detection Algorithm for Fast and Lightweight Object Detection

## How to use (Examples)
* Train: `yolov8nd detect train model=yolov8ndn.pt data=coco128.yaml epochs=50`
* Validation: `yolov8nd detect val model=yolov8ndn.pt data=coco128.yaml`
* Predict: `yolov8nd detect predict model=yolov8ndn.pt source=https://ultralytics.com/images/bus.jpg`

## Experimental Environment
* CPU: i5-13500 (E-Core: 2.0GHz, P-Core: 3.0GHz)
* Memory: DDR4 64GB (3200MHz, 128bit width)
* GPU: RTX 4070 (max 2.4GHz, 125W)
* OS: Ubuntu 22.04 LTS

## Performance and Comparison

| Models            | Size  | mAP50-95<br><sup>(%)  | Params<br><sup>(M)| GFLOPs    | Speed<br><sup>GPU(ms) | Speed<br><sup>CPU(ms) |
|-------------------|-------|-----------------------|-------------------|-----------|-----------------------|-----------------------|
| YOLOv8ndn         | 640   | 36.4                  | 3.2               | 7.6       | 4.1                   | 36.9                  |
| YOLOv8nds         | 640   | 44.0                  | 12.3              | 27.1      | 4.2                   | 88.2                  |
| YOLOv8ndm         | 640   | 48.9                  | 26.9              | 74.9      | 6.1                   | 205.5                 |
| YOLOv8ndl         | 640   | 51.1                  | 43.5              | 157.1     | 9.6                   | 390.5                 |
|                   |       |                       |                   |           |                       |                       |
| YOLOv8ndn-lite    | 640   | 34.9                  | 2.4               | 5.9       | 3.6                   | 30.9                  |
| YOLOv8nds-lite    | 640   | 43.2                  | 9.2               | 21.1      | 3.7                   | 73.7                  |
| YOLOv8ndm-lite    | 640   | 48.5                  | 22.2              | 63.7      | 5.3                   | 181.4                 |
| YOLOv8ndl-lite    | 640   | 50.4                  | 38.2              | 139.7     | 8.6                   | 352.4                 |
|                   |       |                       |                   |           |                       |                       |
| YOLOv8n           | 640   | 37.5                  | 3.2               | 8.9       | 4.4                   | 40.9                  |
| YOLOv8s           | 640   | 44.7                  | 11.2              | 28.6      | 4.5                   | 91.5                  |
| YOLOv8m           | 640   | 50.1                  | 25.9              | 78.9      | 6.5                   | 215.1                 |
| YOLOv8l           | 640   | 52.9                  | 43.7              | 165.2     | 10.1                  | 406.5                 |

Train parameters: `batch=16 epochs=500 optimizer=SGD lr0=0.01 momentum=0.937 data=coco.yaml`

Validation parameters: `data=coco.yaml batch=1 device=0|cpu`


## TODO
* Prepare for weights: YOLOv8nd-aux

## Acknowlege

Template from https://github.com/ultralytics/ultralytics (version: 8.1.25)
