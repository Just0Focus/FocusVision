import pytesseract
# Performs optical character recognition (OCR) on a screenshot
# using Tesseract and displays the extracted text.
#
# Configures Tesseract engine, takes a screenshot, preprocesses
# it, runs OCR, and displays results in a new window.
import cv2
import numpy as np
import pyautogui
import tkinter as tk
import os

# Tesseract OCR Engine must be installed on the system

tess_disclaimer = """
\nYou may need to install Tesseract OCR Engine.
Newer versions of Apache's Tesseract on windows are no longer compiled by Apache.
\nMannheim University Library Took the honor of providing updated WinEXE.
\nLink: https://github.com/UB-Mannheim/tesseract/wiki\n
"""

# Set up the OCR engine
tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

print("\nTesseract Path:", '"' + pytesseract.pytesseract.tesseract_cmd)
# Check if tesseract.exe exists in the tessdata directory path
if os.path.exists(tesseract):
    version = pytesseract.get_tesseract_version()
    print("V.[", version, "] Installed.")
    print("Config Path:", '"' + tessdata_dir_config.split("C:\Program Files\\")[1])
else:
    print("\nTesseract not found. Please check the installation path.")
    print(tess_disclaimer)
    exit()


# Define a function to run OCR on the captured image
def read_text():
    # Capture a screenshot of the area under the window
    img = pyautogui.screenshot(
        region=(
            (root.winfo_x() - 10),
            root.winfo_y(),
            root.winfo_width(),
            root.winfo_height(),
        )
    )

    # Convert the image to grayscale and threshold it
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Apply erosion and dilation filters to remove noise
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=3)
    img_erosion = cv2.erode(img_dilation, kernel, iterations=2)

    # Perform OCR on the processed image
    text = pytesseract.image_to_string(
        img_erosion, lang="eng", config=tessdata_dir_config
    )
    ##text = pytesseract.image_to_string(img, config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()-._`\s- --user-words custom_user_words.txt --user-patterns custom_user_patterns.txt')

    # Create new window with the extracted text
    top = tk.Toplevel()
    top.title("Extracted Text")
    top.geometry("600x400")
    top.resizable(False, False)
    # Create a text box to display the extracted text
    text_box = tk.Text(top, wrap="word")
    text_box.pack()
    text_box.insert(tk.END, text)


# Create the window
root = tk.Tk()
root.title("Transparent OCR")
root.geometry("1200x600")
root.resizable(True, True)

# Create a button to run OCR
button = tk.Button(root, text="Read", command=read_text)
button.pack()

# Make the window transparent
root.attributes("-alpha", 0.5)

# Run the main event loop
root.mainloop()
