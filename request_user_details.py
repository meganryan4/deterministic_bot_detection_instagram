from defines import make_api_call

def get_user_med_count( creds ):
	""" Get account details for a users account
	
	API Endpoint:
		https://graph.instagram.com/{graph-api-version}/{ig-user-id}/?fields={fields}&access_token={access_token}

	Args:
        creds: the input user credentials

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'media_count' # fields to get back
	endpointParams['access_token'] = creds['access_token'] # access token

	url = creds['endpoint_base'] + creds['instagram_account_id'] + '/?fields' # endpoint url

	response = make_api_call( url, endpointParams, creds['debug'] ) # make the api call
	
	return response['json_data']['media_count']