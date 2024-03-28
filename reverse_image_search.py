import requests

def reverse_image_search(image_url):
    """ Send JSON request for reverse image searching
	
	Args:
		image_url: the single URL for the image to be processed

	Returns:
		Boolean: True if a duplicate was found, False if not

	"""

    # url for API
    url = "https://google-reverse-image-api.vercel.app/reverse"
    data = {"imageUrl": image_url}
    
    # send json request
    response = requests.post(url, json=data)

    # if a duplicate image was found return True, otherwise return False
    if response.ok:
        print(response.json())
        return True
    else:
        print(response.status_code)
        return False