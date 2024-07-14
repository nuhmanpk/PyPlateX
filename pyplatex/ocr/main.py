from fast_plate_ocr import ONNXPlateRecognizer

class OCR:
    def __init__(self):
        self.fast_plate_model = ONNXPlateRecognizer('argentinian-plates-cnn-model')

    def recognize_plate(self, image_path):
        result = self.fast_plate_model.run(image_path)
        
        plates = self.process_results(result)
        
        return plates