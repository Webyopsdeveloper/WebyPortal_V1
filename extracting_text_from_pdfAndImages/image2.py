#working final 
# from PIL import Image
# from pytesseract import pytesseract
# import enum


# class OS(enum.Enum):
#     Mac = 0
#     Windows = 1


# class Language(enum.Enum):
#     ENG = 'eng'
#     RUS = 'rus'
#     ITA = 'ita'


# class ImageReader:
#     windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     pytesseract.tesseract_cmd = windows_path
#     print('Running on: WINDOWS\n')
    
#     def extract_text(self, image: str, lang: Language) -> str:
#         img = Image.open(image)
#         extracted_text = pytesseract.image_to_string(img, lang=lang.value)
#         return extracted_text


# if __name__ == '__main__':
#     ir = ImageReader()
#     # Multiple languages can be used with: 'eng+ita+rus'
#     text = ir.extract_text(image='images/sample2.jpg', lang=Language.ENG)

#     # Do some light processing before printing the text
#     processed_text = ' '.join(text.split())
#     print(processed_text)

from PIL import Image
from pytesseract import pytesseract
import enum
import os

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'

class ImageReader:
    windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = windows_path
    # print('Running on: WINDOWS\n')

    def extract_text(self, image: str, lang: Language) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text

if __name__ == '__main__':
    ir = ImageReader()

    
    input_folder = 'input'

    
    items_sold_list = []

    
    image_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.lower().endswith(('.jpg', '.png', '.jpeg'))]

    
    for image_file in image_files:
        
        text = ir.extract_text(image=image_file, lang=Language.ENG)

        
        items_sold_idx = text.lower().find('items sold')

        if items_sold_idx != -1:
            
            extracted_text_after_items_sold = text[items_sold_idx + len('items sold'):]

            
            processed_text = ' '.join(extracted_text_after_items_sold.split())

            
            items_sold_list.append(processed_text)

    
    
    
    for idx, item in enumerate(items_sold_list, 1):
        print(f"{idx}. {item[7:33]}")
