from request_user_details import get_user_med_count
from get_user_profile_details import get_profile_details_selenium

def bot_likeness_scorer(creds, ai_probabilities, images_found_rev):
    """ Determines bot likeness score
	
	Args:
		creds: the account credentials entered
        ai_probabilities: array of AI image prediciton probabilities
        images_found_rev: array of True/False whether an image was found using reverse image search

	Returns:
		array: the array of the bot likeness score and the string array of the account's characteristics

	"""

    # get the total post count of the user
    post_count = get_user_med_count(creds)

    # a high follow ratio is good
    has_profile_pic, followed, follow_ratio = True, False, 0#get_profile_details_selenium(creds)

    print(post_count)

    # to find the number of digits in the username
    username = creds['ig_username']
    digits_in_username = sum(c.isdigit() for c in username)

    ai_prob_ratio, ai_tot, rev_ratio, rev_tot = 0, 0, 0, 0

    for prob in ai_probabilities:
        if prob > 0.5:
            ai_tot +=1
    
    for img in  images_found_rev:
        if img == True:
            rev_tot +=1

    if post_count != 0:
        ai_prob_ratio = ai_tot / post_count
        rev_ratio = rev_tot / post_count

    score = 0.0 # [post_count] + [has_profile_pic] + [followed] + [follow_ratio] + [digits_in_username] + [ai_prob_ratio] + [rev_ratio]

    if post_count == 0:
        score += 0.1
    elif post_count < 3:
        score += 0.05

    if not has_profile_pic:
        score += 0.2
    
    if not followed:
        score += 0.1

    if follow_ratio < 0.2:
        score += 0.15
    elif follow_ratio < 0.5:
        score += 0.1

    if digits_in_username == 0:
        pass
    elif digits_in_username == 1:
        score += 0.02
    elif digits_in_username == 2:
        score += 0.04
    elif digits_in_username == 3:
        score += 0.08
    elif digits_in_username >= 4:
        score += 0.1

    # if 20% or more of the images are probably AI, increase score
    if ai_prob_ratio > 0.2:
        score += 0.16
    elif ai_prob_ratio > 0.4:
        score += 0.2
    elif ai_prob_ratio > 0.6:
        score += 0.4
    elif ai_prob_ratio > 0.8:
        score += 0.8
    elif ai_prob_ratio >= 1:
        score += 0.9

    # if 10% or more of the images are from Google, higher bot likelihood
    if rev_ratio > 0.1:
        score += 0.1
    elif rev_ratio > 0.2:
        score += 0.16
    elif rev_ratio > 0.4:
        score += 0.2
    elif rev_ratio > 0.6:
        score += 0.4
    elif rev_ratio > 0.8:
        score += 0.8
    elif rev_ratio >= 1:
        score += 0.9

    # if it's an empty account - it's very likely a bot
    if post_count == 0 and not has_profile_pic and not followed:
        score += 0.4
    

    # score should never be 100% to allow for possible error
    if score >= 1:
        score = 0.999999

    characteristics = []
    if post_count < 2:
        characteristics.append('Your post count is very low.\n')
    if has_profile_pic == False:
        characteristics.append('You do not have a unique profile picture.\n')
    if followed == False:
        characteristics.append('You have no followers.\n')
    if follow_ratio < 0.5:
        characteristics.append('Your following to follower ratio is low.\nYou follow at least twice as many people \nas who follow you.\n')
    if digits_in_username >= 1:
        characteristics.append('Your username contains one or more digits.\n')
    if ai_prob_ratio != 0:
        characteristics.append('Your posts likely contain AI images.\n')
    if rev_ratio != 0:
        characteristics.append('Your posts contain one or more images easily found on reverse image search.\n')
    
    bot_likenesses = []
    bot_likenesses.append(score) # may have to convert this to a string
    bot_likenesses.append(characteristics)

    return bot_likenesses
