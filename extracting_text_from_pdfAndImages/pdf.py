

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import pytesseract
from PIL import Image

def convert_images_to_pdf(image_folder, output_pdf):
    
    c = canvas.Canvas(output_pdf, pagesize=letter)

    
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        
        extracted_text = pytesseract.image_to_string(Image.open(image_path))

        
        c.drawString(100, 700, extracted_text)

        
        c.drawImage(image_path, 100, 100, width=400, height=500)

        
        c.showPage()

    
    c.save()

if __name__ == "__main__":
    image_folder = "sample"
    output_pdf = "output.pdf"

    convert_images_to_pdf(image_folder, output_pdf)
