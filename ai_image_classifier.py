from PIL import Image
from io import BytesIO
import requests
from keras.models import load_model
import numpy as np

def preprocess_img(image_url):
    """ Preprocess Instagram images to fit model
	
	Args:
		image_url: the single URL for the image to be processed

	Returns:
		array: the image set up as an array that matches the data used in the model

	"""

    # Get image from URL
    response = requests.get(image_url)
    # Error handling for failed image retrieval
    if response.status_code != 200:
        print(f"Failed to retrieve image from {image_url}. Status code: {response.status_code}")
        return None
    img = Image.open(BytesIO(response.content))

    # Set image to 32x32 to match with training data
    preprocessed_img = img.resize((32, 32))

    return np.array(preprocessed_img)

def detect_ai_image(image_urls):
    """ Request data from endpoint with params
	
	Args:
		image_urls: an array of strings of the URLs for all images posted

	Returns:
		array: the array of human probability scores

	"""

    # Set human/bot probability score
    human_probability = []

    # Load the model from the saved file
    loaded_model = load_model('model.h5')

    # for all image URLs passes in
    for url in image_urls:
        preprocessed_img = preprocess_img(url)
        # Reshape the image for model prediction
        preprocessed_img = np.expand_dims(preprocessed_img, axis=0)
        prediction = loaded_model.predict(preprocessed_img)
        # The first index gives FAKE (or AI) image probability
        ai_probability = prediction[0][0]
        human_probability.append(ai_probability)

    return human_probability

