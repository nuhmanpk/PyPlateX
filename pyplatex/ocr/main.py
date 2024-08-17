import asyncio
import os
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from pyplatex.utils import format_plate_number


class OCR:
    def __init__(self):
        self.predictor = ocr_predictor(pretrained=True)

    async def recognize_plate(self, image_path):
        loop = asyncio.get_event_loop()

        doc = await loop.run_in_executor(None, lambda: DocumentFile.from_images(image_path))

        result = await loop.run_in_executor(None, self.predictor, doc)

        os.remove(image_path)

        plate_number, plate_number_confidence = format_plate_number(result)

        return plate_number, plate_number_confidence
