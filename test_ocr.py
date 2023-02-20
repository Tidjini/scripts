from pix2text import Pix2Text
import cv2
import matplotlib.pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)

# Naming a window
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)

# Using resizeWindow()
cv2.resizeWindow("Resized_Window", 600, 800)


def get_image(picture_path):
    """Try to get image from picture path with zoom

    defaut zoom, is matched with my tests
    """
    try:
        return cv2.imread(picture_path)
    except Exception as e:
        print("Get Image Exception due, to:", e)

    return None


def apply_zoom(image, zoom=4):
    h, w = image.shape[:2]
    image = cv2.resize(image, (w * zoom, h * zoom))
    return image


def threshold(image):
    """This steps are copied from StackoverFlow

    todo put the link here
    """
    # Grayscale, Gaussian blur, Otsu's threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh


def remove_noise(image):

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    return 255 - opening


image = get_image('pic1.jpg')
# image = apply_zoom(ORIGINAL, 1)
# for i in range(1000):
image = remove_noise(image)
# image = threshold(image)
cv2.imshow("Resized_Window", image)
cv2.waitKey()
# image = apply_zoom(image, 1)
# image = threshold(image)
# for i in range(500):
#     image = remove_noise(image)
cv2.imwrite('pic1.traited.jpg', image)


p2t = Pix2Text(analyzer_config=dict(model_name='layout'))
# 也可以使用 `p2t.recognize(img_fp)` 获得相同的结果
outs = p2t('pic1.traited.jpg', resized_shape=600)
# print(outs)
# 如果只需要识别出的文字和Latex表示，可以使用下面行的代码合并所有结果
only_text = '\n'.join([out['text'] for out in outs])
print("Pix 2 Text")
print(only_text)


data = pytesseract.image_to_string(image)
print("pytesseract")
print(data)
