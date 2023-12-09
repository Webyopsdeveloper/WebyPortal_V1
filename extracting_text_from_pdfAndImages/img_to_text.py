import pytesseract
from PIL import Image

def image_to_text(image_path):
    try:
        
        image = Image.open(image_path)

        
        text = pytesseract.image_to_string(image)

        
        return text

    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    image_path = "images/sample2.jpg"  
    extracted_text = image_to_text(image_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("Failed to extract text from the image.")
