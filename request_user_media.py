from defines import make_api_call

def get_user_media(creds, pagingUrl = '' ) :
	""" Get users media
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username' # fields to get back
	endpointParams['access_token'] = creds['access_token'] # access token

	if ( '' == pagingUrl ) : # get first page
		url = creds['endpoint_base'] + creds['instagram_account_id'] + '/media' # endpoint url
	else : # get specific page
		url = pagingUrl  # endpoint url

	return make_api_call( url, endpointParams, creds['debug'] ) # make the api call


def get_user_images(creds, pagingUrl = '' ) :
	""" Get users media
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'media_type,media_url,username' # fields to get back
	endpointParams['access_token'] = creds['access_token'] # access token

	if ( '' == pagingUrl ) : # get first page
		url = creds['endpoint_base'] + creds['instagram_account_id'] + '/media' # endpoint url
	else : # get specific page
		url = pagingUrl  # endpoint url

	response = make_api_call( url, endpointParams, creds['debug'] ) # make the api call

	# make array to store image urls
	media_urls = []
	# run through all image urls from response[json_data][data][post_number][media_url]
	# if media is an image or part of an album/carousel
	for media in response['json_data'].get('data', []):
		if media.get('media_type') == "CAROUSEL_ALBUM" or media.get('media_type') == "IMAGE":
			media_urls.append(media.get('media_url', ''))
		
	return media_urls