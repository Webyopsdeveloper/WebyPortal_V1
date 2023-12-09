import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials.json'

def detect_text(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return "No text found in the image."

if __name__ == "__main__":
    image_path = "images/sample1.jpg"
    extracted_text = detect_text(image_path)
    print("Extracted Text:")
    print(extracted_text)
