import os
import asyncio
import cv2
from datetime import datetime
from pyplatex.models import DETECTION_BASE_MODEL
from ultralytics import YOLO
import numpy as np
from PIL import Image
from cv2filters import Filters
from pyplatex.ocr import OCR

class ANPR:
    def __init__(self):
        self.model = YOLO(DETECTION_BASE_MODEL)
        self.filters = Filters()
        self.ocr = OCR()  # Initialize OCR

    async def load_image(self, image_path):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, Image.open, image_path)

    async def detect(self, image_path, max_detections=1, confidence=0.6, save_image=False, padding=5, folder_name=None, use_ocr=False):
        # Load and preprocess the image
        image = await self.load_image(image_path)
        image = image.convert("RGB")
        image = np.array(image)

        # Predict 
        results = await asyncio.to_thread(self.model.predict, source=image, max_det=max_detections, conf=confidence)

        detected_plates = []
        output_info = {
            "detected": False,
            "confidence": 0,
            "saved_path": None,
            "image_tensor": None,
            "recognized_plate": None
        }

        for result in results:
            boxes = result.boxes.xyxy[0].numpy() if result.boxes else []
            conf = result.boxes.conf[0].numpy() if len(result.boxes.conf) > 0 else 0
            
            if boxes.size > 0:
                detected_plates.append((boxes, conf))
                output_info["detected"] = True
                output_info["confidence"] = conf

        if save_image and detected_plates:
            # Set folder name
            if folder_name is None:
                folder_name = "detected_plates"
            # Create directory if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Create unique output path
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(folder_name, f"cropped_plate_{timestamp}.jpg")

            # Add padding
            x1, y1, x2, y2 = boxes
            x1 = max(0, int(x1) - padding)
            y1 = max(0, int(y1) - padding)
            x2 = min(image.shape[1], int(x2) + padding)
            y2 = min(image.shape[0], int(y2) + padding)
            cropped_image = image[y1:y2, x1:x2]

            await asyncio.to_thread(cv2.imwrite, output_path, cropped_image)
            output_info["image_tensor"] = cropped_image
            output_info["saved_path"] = output_path 

            # Perform OCR if enabled
            if use_ocr:
                recognized_plate = self.ocr.recognize_plate(cropped_image)
                output_info["recognized_plate"] = recognized_plate

        return output_info
