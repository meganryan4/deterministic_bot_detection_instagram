import requests

def get_user_id(access_token, username):
    """ Get user id 
	
	API Endpoint:
		'https://graph.instagram.com/v19.0/me?fields=id,username&access_token={access_token}'

    Args:
        access_token: the input user access token
        username: the input username

	Returns:
		object: user id

	"""

    # Get user ID from username
    url = f'https://graph.instagram.com/v19.0/me?fields=id,username&access_token={access_token}'
    response = requests.get(url)

    # catch json error - means access token is incorrect
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise a HTTPError for bad responses
        data = response.json()
    except requests.RequestException as e:
        # this is the error thrown if the access token is invalid
        print(f"Error making request: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None

    print(url)

    if 'error' in data:
        print(f"Error: {data['error']['message']}")
        return None
    elif data.get('username') != username:
        # if the username does not match the access token
        print(f"Error: entered username did not match the username associated with this access token")
        return None
    else:
        return data.get('id')