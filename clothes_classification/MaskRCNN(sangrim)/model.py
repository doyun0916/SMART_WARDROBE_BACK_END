import glob
import multiprocessing as mp
import os
import time
import cv2
import tqdm
import io
import numpy as np

from detectron2.config import get_cfg
from detectron2.data.detection_utils import read_image
from detectron2.utils.logger import setup_logger
from detectron2 import model_zoo

from .predictor import Visualization

CLASS = [
    "short_sleeved_shirt",
    "long_sleeved_shirt",
    "short_sleeved_outwear",
    "long_sleeved_outwear",
    "vest",
    "sling",
    "shorts",
    "trousers",
    "skirt",
    "short dress",
    "long dress",
    "vest dress",
    "sling dress",
]


class Model:
    def __init__(self, weights_path, threshold=0.8):
        """
        Mask RCNN Prediction Model
        Args:
            weights_path (string): Trained Model weights.pth path
            threshold (float): Model prediction threshold (default: 0.8)
        """

        self.weights_path = weights_path
        self.threshold = threshold
        self.setup_cfg()
        self.predictor = Visualization(self.cfg)

    def setup_cfg(self, cfg_path=False):
        """
        Model setup config file
        Args:
            cfg path (string): Model cfg Path
        """
        cfg = get_cfg()
        if not cfg_path:
            cfg.merge_from_file(
                model_zoo.get_config_file(
                    "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
                )
            )
            cfg.MODEL.WEIGHTS = self.weights_path
            cfg.DATALOADER.NUM_WORKERS = 6
            cfg.SOLVER.IMS_PER_BATCH = 2
            cfg.SOLVER.BASE_LR = 0.00025
            cfg.SOLVER.MAX_ITER = 10000
            cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 512
            cfg.MODEL.ROI_HEADS.NUM_CLASSES = 13
            cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.threshold
            cfg.MODEL.DEVICE = "cpu"
            cfg.freeze()
        else:
            cfg.merge_from_file(cfg_path)
        self.cfg = cfg

    def predict_from_image(self, image_path, download=False):
        """
        Visualizes predictions on frames of the imgae.
        Args:
           image_path (string): Image path
           download (boolean): Whether download output image
        Yields:
            Predict result(dictionary):
        """
        img = read_image(image_path, format="BGR")
        predictions = {
            "result": {"width": img.shape[1], "height": img.shape[0], "objects": []}
        }
        outputs, visualized_output = self.predictor.run_on_image(img)

        if download:
            visualized_output.save("./output.jpg")
        if "instances" in outputs:
            instances = outputs["instances"]
            pred_boxes = instances.pred_boxes.tensor.numpy()
            pred_masks = instances.pred_masks.numpy()
            pred_classes = instances.pred_classes.numpy()
            scores = instances.scores.numpy()

        for i in range(len(scores)):
            instance = {
                "class": CLASS[pred_classes[i]],
                "classId": pred_classes[i],
                "score": scores[i],
                "x1": pred_boxes[i][0],
                "y1": pred_boxes[i][1],
                "x2": pred_boxes[i][2],
                "y2": pred_boxes[i][3],
                "pred_masks": pred_masks[i],
            }
            predictions["result"]["objects"].append(instance)

        return predictions
