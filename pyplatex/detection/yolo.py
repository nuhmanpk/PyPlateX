from pyplatex.models.base_model import DETECTION_BASE_MODEL
from ultralytics import YOLO
import numpy as np
from PIL import Image
from cv2filters import Filters


class ANPR:
    def __init__(self):
        self.model = YOLO(DETECTION_BASE_MODEL)
        self.filters = Filters()

    def detect(self, image_path, max_detections=1, confidence=0.6, save_image=False):
        # Load and preprocess the image
        image = Image.open(image_path)
        # handling 4 channel images
        image = image.convert("RGB")
        image = np.array(image)

        results = self.model.predict(
            source=image, max_det=max_detections, conf=confidence
        )

        detected_plates = []
        for result in results:
            boxes = result.boxes.xyxy[0].numpy() if result.boxes else []
            confidence = (
                result.boxes.conf[0].numpy() if len(result.boxes.conf) > 0 else 0
            )
            detected_plates.append((boxes, confidence))

        if save_image:
            x1, y1, x2, y2 = boxes
            self.filters.crop_image(image, x1, y1, x2, y2)

        return detected_plates
