from request_user_details import get_user_med_details

def bot_likeness_scorer(creds, ai_probabilities, images_found_rev):
    #this creates a bot likeness score for your account
    #[post_count] + [has_profile_pic] + [followed] + [follow_ratio] + [digits_in_username] + [ai_probabilities] + [images_found_rev]
    post_count = get_user_med_details(creds)
    print(post_count)
    post_count_score = 0

    # to find the number of digits in the username
    username = creds['ig_username']
    digits_in_username = sum(c.isdigit() for c in username)

    score = 0.0
    characteristics = ['Bot likeness is not calculated in this version']

    bot_likenesses = []
    bot_likenesses.append(score) # may have to convert this to a string
    bot_likenesses.append(characteristics)

    return bot_likenesses
