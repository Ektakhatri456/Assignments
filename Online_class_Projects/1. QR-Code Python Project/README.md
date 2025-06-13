# 📱 QR Code Encoder & Decoder

A Python-based project to generate and decode QR codes containing custom messages. This project demonstrates how to use the qrcode, Pillow, and pyzbar libraries for creating and reading QR codes in Python.

# 📂 Project Files

File	Description
---------------------------
📌encode.py:	Generates a QR code with a custom message and saves it as an image.
📌decode.py:	Reads the QR code image and decodes the hidden message.

# 📦 Requirements
Before running the project, install the required dependencies:
     "pip install qrcode[pil] pyzbar pillow"

# 🚀 How to Use

## 1️⃣ Encode a QR Code
Run the encode.py file to generate a QR code image with your custom message.
        "python encode.py"
        
The encoded QR code image will be saved in the specified directory as myqrcode.png.

## 2️⃣ Decode a QR Code
Run the decode.py file to read and display the message encoded in a QR code image.
         "python decode.py"
         
The decoded message will be printed in the terminal.

     
