# Transparent OCR

This project performs optical character recognition (OCR) on a screenshot using Tesseract and displays the extracted text in a new window.

## Installation
- Tesseract OCR Engine must be installed on the system. You may need to install Tesseract OCR Engine. Newer versions of Apache's Tesseract on windows are no longer compiled by Apache.
  - Mannheim University Library Took the honor of providing updated WinEXE. [Link](https://github.com/UB-Mannheim/tesseract/wiki)

## Setup
- Set up the OCR engine by configuring the Tesseract engine and specifying the Tesseract path.
- Create venv using `python -m venv .venv`.
- Activate venv using `.venv\Scripts\activate` or something.
- Run with `python main.py`

## How to Use
1. Run the script and a window will open.
2. Click the "Read" button to capture a screenshot of the area under the window, preprocess it, run OCR, and display the results in a new window.

## Disclaimer
If Tesseract is not found, please check the installation path. Also, refer to the Tesseract disclaimer provided in the code.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- PyAutoGUI (`pyautogui`)
- Pytesseract (`pytesseract`)
- Tkinter (`tk`)