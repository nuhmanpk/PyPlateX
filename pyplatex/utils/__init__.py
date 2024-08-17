import numpy as np
import re

def format_plate_number(recognized_plate):
    if not recognized_plate or not recognized_plate.pages:
        return None

    plate_number = ""
    confidence_scores = []

    # Define a pattern for valid license plate characters
    valid_characters_pattern = re.compile(r'[A-Z0-9\- ]')  # Allows letters, digits, dashes, and spaces

    # Process the recognized_plate Document
    for page in recognized_plate.pages:
        for block in page.blocks:
            for line in block.lines:
                for word in line.words:
                    if word.confidence > 0.5:  # Threshold confidence level
                        # Filter valid characters
                        filtered_word = ''.join(char for char in word.value if valid_characters_pattern.match(char))
                        if filtered_word:
                            plate_number += filtered_word + " "
                            confidence_scores.append(word.confidence)

    # Calculate average confidence
    average_confidence = np.mean(confidence_scores) if confidence_scores else 0.0

    # Round the average confidence to 2 decimal places
    average_confidence = round(average_confidence, 2)

    # Strip extra spaces and apply formatting rules
    plate_number = plate_number.strip()
    plate_number = re.sub(r'\s+', ' ', plate_number)  # Replace multiple spaces with a single space

    # Further clean up plate number by removing unwanted leading/trailing characters
    plate_number = re.sub(r'^[\- ]+|[\- ]+$', '', plate_number)  # Remove leading and trailing dashes and spaces

    # Optionally, remove excess or incorrect characters (e.g., single dashes or misplaced spaces)
    plate_number = re.sub(r'[\- ]{2,}', ' ', plate_number)  # Replace multiple dashes or spaces with a single space

    return plate_number, average_confidence
    
