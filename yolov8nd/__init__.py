# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.2.9"

import os

# Set ENV Variables (place before imports)
os.environ["OMP_NUM_THREADS"] = "1"  # reduce CPU utilization during training

from yolov8nd.data.explorer.explorer import Explorer
from yolov8nd.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
from yolov8nd.utils import ASSETS, SETTINGS
from yolov8nd.utils.checks import check_yolo as checks
from yolov8nd.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "Explorer",
)
