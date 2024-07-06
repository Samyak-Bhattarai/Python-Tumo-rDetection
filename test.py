import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

# Load the trained model
def test_model(image_name):
    model = load_model('BrainTumor10EpochsCategorical.h5')

    # Create the full image path
    image_path = 'C:\\Users\\samyy\\Desktop\\PROJECTS\\PYTHON\\Brain Tumor Detection\\Python-TumorPrediction\\pred\\' + image_name
    print(f"Image path: {image_path}")

    # Load and process the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Check the file path and ensure the file exists.")
        return

    img = Image.fromarray(image)
    img = img.resize((64, 64))
    img = np.array(img)

    input_img = np.expand_dims(img, axis=0)

    result = model.predict(input_img)

    predicted_class = np.argmax(result, axis=1)

    return predicted_class[0]

if __name__ == '__main__':
    predicted_class = test_model('pred0.jpg')
    print(f"Predicted Class: {predicted_class}")
