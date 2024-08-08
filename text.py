import cv2
import numpy as np
import easyocr


def ocr_basic(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def ocr_with_easyocr(image_path):
    reader = easyocr.Reader(['en'])

    img = cv2.imread(image_path)
    result = reader.readtext(img)

    for detection in result:
        bbox, text, prob = detection
        print(f"text detected: {text}")

image_file = '2D7M.png'

ocr_basic(image_file)
ocr_with_easyocr(image_file)
