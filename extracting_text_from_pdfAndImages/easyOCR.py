import easyocr

def extract_text_from_image(image_path, language='en'):
    try:
        
        reader = easyocr.Reader([language])

        
        result = reader.readtext(image_path)

        
        extracted_text_list = [detection[1] for detection in result]

        
        extracted_text = '\n'.join(extracted_text_list)

        return extracted_text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    image_path = 'C:\Users\Vacha Patel\OneDrive\Desktop\work\may\reading_pdf_images_script\input\sample1.jpg'
    extracted_text = extract_text_from_image(image_path)
    print(extracted_text)
