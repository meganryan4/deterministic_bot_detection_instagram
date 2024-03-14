import matplotlib.pyplot as plt
import numpy as np

def generate_graph(probability_scores, images_found, bot_likelihood_score, bot_likeness_chars):
    # Calculate the percentage of images found
    num_images = len(images_found)
    percent_found = (sum(images_found) / num_images) * 100

    # Calculate the mean of the probability scores
    mean_score = np.mean(probability_scores)

    # Create a figure with subplots
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12, 4))#, gridspec_kw={'width_ratios': [4, 1, 2]})

    # Set the width of the bars
    bar_width = 0.4

    prob_scores = [1.0 - num for num in probability_scores]
    # Create a bar plot to represent the probability scores
    index = np.arange(num_images)
    colors = ['red' if score < 0.5 else 'green' for score in probability_scores]
    bars = ax1.bar(index, prob_scores, width=bar_width, color=colors)

    # Add labels and title to the bar plot
    ax1.set_xlabel('Image')
    ax1.set_ylabel('Probability Score')
    ax1.set_title('AI Likelihood Prediction')

    # Set the x-axis ticks and labels
    ax1.set_xticks(index)
    ax1.set_xticklabels([f'{i+1}' for i in range(num_images)])

    # Create a pie chart for the mean of the probability scores
    labels = ['Not AI', 'AI']
    sizes = [mean_score, 1 - mean_score]
    colors = ['green', 'red']
    ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))

    # Add title to the pie chart
    ax2.set_title('Mean AI Likelihood')
    if mean_score < 0.5:
        text_color = 'green'
    else:
        text_color = 'red'
    #ax2.text(0.5, 0.5, f'Most of the images are likely NOT AI', ha='center', va='center', color='blue', fontweight='bold')

    # Display the percentage of images found with adjusted text position
    ax3.text(0.5, 0.5, f'{percent_found:.2f}%\n of account images\nwere found using\nreverse image search', ha='center', va='center', color='blue', fontweight='bold')

    # Hide the axes of ax2
    ax3.set_axis_off()

    # Display the percentage of images found with adjusted text position
    bot_score = bot_likelihood_score * 100
    if bot_likelihood_score < 0.5:
        text_col = 'green'
    else:
        text_col = 'red'
    ax4.text(0.5, 0.5, f'Your bot likeness score is\n {bot_score}%\n\nAccount similarity to a bot is due to:\n {" ".join(bot_likeness_chars)}\n', ha='center', va='center', color=text_col, fontweight='bold')


    # Hide the axes of ax2
    ax4.set_axis_off()

    # Adjust layout to prevent overlap
    plt.tight_layout()
    #plt.title("Social Media Account AI and Bot Detection")

    # Show the plot
    plt.show()

# Example usage with multiple images
#bot_likelihood_score = 0.12
#bot_likeness_chars = ['Use of image(s) found on Google\nUse of AI image(s)\nAccount has 2 numbers in username']
#probability_scores = [0.85, 0.92, 0.76, 0.68, 0.94, 0.90, 0.72, 0.82, 0.3]
#images_found = [True, False, False, True, False, False, False, False, False]

#generate_graph(bot_likelihood_score, bot_likeness_chars, probability_scores, images_found)
