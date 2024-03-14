import requests
import json

def get_creds() :
	""" Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""

	creds = dict() # dictionary to hold everything
	creds['access_token'] = ''# access token for use with all api calls
	creds['client_id'] = 'FB-APP-CLIENT-ID' # client id from facebook app IG Graph API Test
	creds['client_secret'] = 'FB-APP-CLIENT-SECRET' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.instagram.com/' # base domain for api calls
	creds['graph_version'] = 'v19.0' # version of the api we are hitting - latest as of 25/01/24
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'yes' # debug mode for api call
	creds['page_id'] = 'FB-PAGE-ID' # users page id
	creds['instagram_account_id'] = '' # users instagram account id
	creds['ig_username'] = ''# ig username

	return creds

def make_api_call( url, endpointParams, debug = 'no' ) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		display_api_call_data( response ) # display response

	return response # get and return content

def display_api_call_data( response ) :
	""" Print out to cli response from api call """

	print("\nURL: ") # title
	print(response['url']) # display url hit
	print("\nEndpoint Params: ") # title
	print(response['endpoint_params_pretty']) # display params passed to the endpoint
	print("\nResponse: ") # title
	print(response['json_data_pretty']) # make look pretty for cli
