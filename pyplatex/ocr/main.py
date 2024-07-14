import subprocess
import sys
from fast_plate_ocr import ONNXPlateRecognizer
import pytesseract  # Ensure this import is present
import asyncio
import cv2
import os

class OCR:
    def __init__(self):
        self.fast_plate_model = ONNXPlateRecognizer('argentinian-plates-cnn-model')
        self.check_tesseract_installation()

    def check_tesseract_installation(self):
        try:
            # Check if Tesseract is installed
            subprocess.run(["tesseract", "--version"], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            if sys.platform == "darwin":
                print("Installing Tesseract on macOS...")
                subprocess.run(["brew", "install", "tesseract"], check=True)
            elif sys.platform.startswith("linux"): 
                print("Installing Tesseract on Linux...")
                subprocess.run(["sudo", "apt", "install", "tesseract-ocr"], check=True)
            elif sys.platform == "win32":  # Windows
                print("Please install Tesseract for Windows manually from the Tesseract at UB Mannheim page.")
            else:
                print("Unsupported OS. Please install Tesseract manually.")
        

    async def recognize_plate(self, image_tensor, model='tesseract'):
        if model == 'fast_plate_model':
            result = self.fast_plate_model.run(image_tensor)
            return result
        
        # Default to Tesseract OCR
        temp_image_path = "temp_image.png"
        await asyncio.to_thread(cv2.imwrite, temp_image_path, image_tensor)
        
        result = await asyncio.to_thread(pytesseract.image_to_string, temp_image_path)

        os.remove(temp_image_path)
        return result
