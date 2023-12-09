import pytesseract
from PIL import Image
import PyPDF2


def read_image(image_path):
    
    image = Image.open(image_path)
    
    text = pytesseract.image_to_string(image)
    
    return text


def read_pdf(pdf_path):
    
    with open(pdf_path, 'rb') as file:
        
        pdf_reader = PyPDF2.PdfReader(file)
        
        text = ""
        
        for page_num in range(len(pdf_reader.pages)):
            
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    return text


image_path = 'demo.jpg'
pdf_path = 'pdf.pdf'


image_text = read_image(image_path)
print("Text extracted from the image:")
print(image_text)


pdf_text = read_pdf(pdf_path)
print("Text extracted from the PDF file:")
print(pdf_text)

