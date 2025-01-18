from PIL import Image
import pytesseract


image = Image.open("/Users/minousatmac/Development/II-BDCC/CV-TP/img.png")


# Effectuer l'OCR
#extracted_text = pytesseract.image_to_string(image, lang='eng')

# Afficher le texte extrait
print("Texte extrait de l'image :")
#print(extracted_text)
