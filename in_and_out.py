from gui_input import input_creds_GUI
from request_user_media import get_user_images
from ai_image_detect import detect_ai_image_selenium
from try_reverse_api import reverse_image_search
from bot_likeness_calculator import bot_likeness_scorer
from output import generate_graph

# input user credentials and get that user's media
new_creds = input_creds_GUI()

# get specific image media from user saved as array
image_urls = get_user_images(new_creds)
print(image_urls)

# find ai probability scores for all images
ai_probabilities = detect_ai_image_selenium(image_urls)

# for all images perform reverse image searching
images_found_rev = []
for image in image_urls:
    reverse_result = reverse_image_search(image)
    images_found_rev.append(reverse_result)
    print(images_found_rev)

bot_likelihoods = bot_likeness_scorer(new_creds, ai_probabilities, images_found_rev)

bot_likelihood_score = bot_likelihoods[0]
bot_likeness_chars =bot_likelihoods[1]

#thread ai images
#thread reverse image searching
#thread bot detection

generate_graph(ai_probabilities, images_found_rev, bot_likelihood_score, bot_likeness_chars)