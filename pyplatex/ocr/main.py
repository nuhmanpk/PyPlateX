from fast_plate_ocr import ONNXPlateRecognizer
import pytesseract

class OCR:
    def __init__(self):
        self.fast_plate_model = ONNXPlateRecognizer('argentinian-plates-cnn-model')

    async def recognize_plate(self, image_tensor, model='tesseract'):
        if model == 'fast_plate_model':
            result = self.fast_plate_model.run(image_tensor)
            return result
        
        # Default to Tesseract OCR
        result = pytesseract.image_to_string(image_tensor)
        return result