import asyncio
import cv2
from pyplatex.models import DETECTION_BASE_MODEL
from ultralytics import YOLO
import numpy as np
from PIL import Image
from cv2filters import Filters

class ANPR:
    def __init__(self):
        self.model = YOLO(DETECTION_BASE_MODEL)
        self.filters = Filters()

    async def load_image(self, image_path):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, Image.open, image_path)

    async def detect(self, image_path, max_detections=1, confidence=0.6, save_image=False, PADDING=5):
        # Load and preprocess the image
        image = await self.load_image(image_path)
        image = image.convert("RGB")
        image = np.array(image)

        # Predict 
        results = await asyncio.to_thread(self.model.predict, source=image, max_det=max_detections, conf=confidence)

        detected_plates = []
        for result in results:
            boxes = result.boxes.xyxy[0].numpy() if result.boxes else []
            conf = result.boxes.conf[0].numpy() if len(result.boxes.conf) > 0 else 0
            detected_plates.append((boxes, conf))

        if save_image and detected_plates:
            x1, y1, x2, y2 = boxes
            x1 = max(0, int(x1) - PADDING)
            y1 = max(0, int(y1) - PADDING)
            x2 = min(image.shape[1], int(x2) + PADDING)
            y2 = min(image.shape[0], int(y2) + PADDING)
            cropped_image = image[y1:y2, x1:x2]

            output_path = "cropped_plate.jpg" 
            await asyncio.to_thread(cv2.imwrite, output_path, cropped_image)

        return detected_plates
