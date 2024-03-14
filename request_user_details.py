from defines import make_api_call

def get_user_details( params ) :
	""" Get insights for a users account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}
		https://graph.instagram.com/{graph-api-version}/{ig-user-id}/?fields={fields}&access_token={access_token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['metric'] = 'follower_count,impressions,profile_views,reach' # fields to get back
	endpointParams['period'] = 'day' # period
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/insights' # endpoint url

	return make_api_call( url, endpointParams, params['debug'] ) # make the api call

def get_user_med_details( creds ):
	""" Get account details for a users account
	
	API Endpoint:
		https://graph.instagram.com/{graph-api-version}/{ig-user-id}/?fields={fields}&access_token={access_token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,username,media_count' # fields to get back
	endpointParams['access_token'] = creds['access_token'] # access token

	url = creds['endpoint_base'] + creds['instagram_account_id'] + '/?fields' # endpoint url

	response = make_api_call( url, endpointParams, creds['debug'] ) # make the api call
	
	return response['json_data']['media_count']