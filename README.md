# 📱 QR Code Generator Using Python

## 📌 About the Project

The QR Code Generator is a simple Python GUI application that converts text and website URLs into QR codes. Users can preview the generated QR code and save it as a PNG image for later use.

The application is built using Python, Tkinter, the qrcode library, and Pillow.

## ✨ Features

- Generate QR codes from text and website URLs.
- Preview the generated QR code in the application window.
- Save QR codes as PNG image files.
- Simple and user-friendly graphical interface.
- Input validation for empty text.
- Supports scanning generated QR codes with a smartphone.

## 🛠️ Technologies Used

- **Python 3** — Core programming language.
- **Tkinter** — Graphical user interface.
- **qrcode** — QR code generation.
- **Pillow** — Image processing and display.

## 📋 Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible editor.
- Internet connection for installing the required packages.

## 📦 Installation

Install the required library using the following command:

```bash
python -m pip install "qrcode[pil]"
```

This installs the QR code generation library and its image-processing dependency.

## 🚀 How to Run the Project

**Step 1:** Download or clone this repository.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Open the terminal in the project folder.

**Step 4:** Run the following command:

```bash
python main.py
```

**Step 5:** Enter your text or website URL in the input box.

**Step 6:** Click **Generate QR Code** to create and preview the QR code.

**Step 7:** Click **Save QR Code as PNG** to save the generated image.

## 📂 Project Structure

```text
QR code generator/
├── main.py
└── README.md
```

## 💻 Example

Input:

```text
https://www.google.com
```

Output:

A QR code that can be scanned using a smartphone to open the website.

## 📚 Concepts Learned

- Python functions
- GUI development using Tkinter
- Working with external Python libraries
- QR code generation
- Image processing using Pillow
- Exception handling and input validation
- Saving files using a file dialog

## 🔮 Future Improvements

- Customize QR code colors.
- Add a logo to the QR code.
- Generate QR codes in different image formats.
- Add a QR code history feature.
- Support batch QR code generation.

## 👨‍💻 Author

Created as a beginner-friendly Python programming project.

## 📄 License

This project is available for learning and educational purposes.
