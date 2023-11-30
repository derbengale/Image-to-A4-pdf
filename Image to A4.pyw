import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QComboBox
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QPixmap, QImageReader, QTransform, QPageSize
from PIL import Image

class ImageToPDFConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("Drag and Drop Image Here or Click 'Open File'", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.openFileButton = QPushButton('Open File', self)
        self.openFileButton.clicked.connect(self.openFileDialog)

        self.dpiComboBox = QComboBox(self)
        self.dpiComboBox.addItems(["72", "150", "300", "600"])
        self.dpiComboBox.setCurrentIndex(2)  # Default to 300 DPI

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.dpiComboBox)
        layout.addWidget(self.openFileButton)

        self.setAcceptDrops(True)
        self.setWindowTitle('Image to PDF Converter')
        self.resize(400, 300)

    def openFileDialog(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filePath:
            self.processImage(filePath)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        url = event.mimeData().urls()[0]
        imagePath = url.toLocalFile()
        self.processImage(imagePath)

    def processImage(self, imagePath):
        with Image.open(imagePath) as img:
            if img.width > img.height:
                img = img.rotate(90, expand=True)

            pdf_path = "output.pdf"
            a4_size = QPageSize(QPageSize.A4).size(QPageSize.Point)

            dpi = int(self.dpiComboBox.currentText())
            scale = dpi / 72  # Base scaling on 72 DPI (standard screen resolution)
            new_width = int(a4_size.width() * scale)
            new_height = int(a4_size.height() * scale)

            # Resize the image using LANCZOS resampling
            img.thumbnail((new_width, new_height), Image.LANCZOS)

            # Create a blank A4 canvas and paste the image onto it
            canvas = Image.new('RGB', (new_width, new_height), 'white')
            img_x = (canvas.width - img.width) // 2
            img_y = (canvas.height - img.height) // 2
            canvas.paste(img, (img_x, img_y))

            canvas.save(pdf_path, "PDF", resolution=dpi)

        QMessageBox.information(self, "Conversion Complete", f"PDF created: {pdf_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if len(sys.argv) > 1:
        window = ImageToPDFConverter()
        window.processImage(sys.argv[1])
    else:
        window = ImageToPDFConverter()
        window.show()

    sys.exit(app.exec())
