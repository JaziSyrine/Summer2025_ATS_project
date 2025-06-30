import paddle
paddle.set_device('cpu')

from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

ocr = PaddleOCR(lang='en')
image_path = r"C:\Users\Asus\Documents\Summer Internship 2025\ATS_projet\Summer2025_ATS_project\converted_images\page_1.png"
img = Image.open(image_path)
img_np = np.array(img)

result = ocr.ocr(img_np)
print("THIS IS THE RESULT HERE ! ==> ",result)
