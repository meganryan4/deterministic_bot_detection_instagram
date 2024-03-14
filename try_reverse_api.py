import requests

def reverse_image_search(image_url):
    # url for API
    url = "https://google-reverse-image-api.vercel.app/reverse"
    
    response = requests.post(url, json=image_url)

    # if a duplicate image was found return True, otherwise return False
    if response.ok:
        print(response.json())
        return True
    else:
        print(response.status_code)
        return False