# Image to A4 Converter
 Converts images to PDF with the twist that A4 format is enforced. It was created to add full page images to my appendix of my masterthesis in Overleaf. 

This Python script provides a simple and efficient GUI tool to convert images into PDF format. The script utilizes the PySide6 library for the graphical user interface and the PIL (Python Imaging Library) for image processing. Below is a guide on how to use and understand the script.

## Requirements

To run this script, ensure you have the following installed:
- Python
- PySide6
- PIL (Python Imaging Library)

You can install PySide6 and PIL using pip:
```bash
pip install PySide6 Pillow
```

## Features

- **Drag and Drop:** Users can drag and drop an image file directly into the window.
- **File Selection Dialog:** Users can also select an image file using a file dialog.
- **DPI Selection:** The tool allows selecting the desired DPI (Dots Per Inch) for the output PDF. Available options are 72, 150, 300, and 600 DPI.
- **Automatic Rotation:** The script automatically rotates the image if it's wider than taller to fit an A4 page properly.
- **Centering Image:** The image is centered on an A4-sized canvas.

## Usage

1. **Starting the Application:**
   Run the script to start the application. If an image path is provided as a command-line argument, the script processes it immediately. Otherwise, the GUI window opens for interaction.

2. **Selecting or Dropping an Image:**
   You can either drag and drop an image into the window or click 'Open File' to select an image.

3. **Select Desired DPI:**
   Choose the desired DPI for the PDF from the dropdown menu.

4. **Converting the Image:**
   The script will process the image, adjusting its size and orientation, and then save it as a PDF named 'output.pdf' in the script's directory.

5. **Completion Notification:**
   A message box notifies the user when the conversion is complete.

## Note

- The script is designed to be straightforward and user-friendly, catering to basic image-to-PDF conversion needs.
- The PDF output is saved in the same directory as the script with a fixed name 'output.pdf'. Subsequent conversions will overwrite the existing file.

---
