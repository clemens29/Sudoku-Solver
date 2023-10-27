import cv2
import pytesseract
import numpy as np

#Bild laden
image = cv2.imread('images/sudoku_1.png')

#Vorarbeiten
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
_, thresh = cv2.threshold(denoised, 127, 255, cv2.THRESH_BINARY_INV)

#Konturen finden
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

numbers = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 10 and h > 10:
        number = thresh[y:y+h, x:x+w]
        numbers.append(number)

#Zahlen erkennen
recognized_numbers = []
for number in numbers:
    number = cv2.resize(number, (28, 28))
    number = cv2.copyMakeBorder(number, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    number = cv2.resize(number, (28, 28))
    number = cv2.bitwise_not(number)
    number = number / 255.0
    number = number.reshape(1, 28, 28, 1)
    number = number.astype('float32')
    number = number.reshape(number.shape[0], 28, 28, 1)
    number = number.astype('float32')
    prediction = pytesseract.image_to_string(number, config='--psm 10 --oem 3 -c tessedit_char_whitelist=123456789')
    if prediction == '':
        prediction = 0
    else:
        prediction = int(prediction)
    recognized_numbers.append(prediction)

#Zahlen ausgeben
#Zahlen in 9x9 Matrix umwandeln
#recognized_numbers = np.array(recognized_numbers).reshape(9, 9)

print(recognized_numbers)
