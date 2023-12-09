from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import uuid

def image_to_pdf(image_path):
    
    pdf_filename = str(uuid.uuid4()) + ".pdf"

    
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    
    img = Image.open(image_path)


    img_width, img_height = img.size

    
    c.setPageSize((img_width, img_height))

    
    c.drawImage(image_path, 0, 0, width=img_width, height=img_height)

    
    c.save()

    return pdf_filename

if __name__ == "__main__":
    image_path = "images/sample2.jpg"

    pdf_filename = image_to_pdf(image_path)
    print(f"PDF saved as: {pdf_filename}")
