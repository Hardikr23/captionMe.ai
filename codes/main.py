from captions_users_vectorisation import *
from image_clasification import *

import time
from datetime import datetime

def get_user_img():
    file_path = input("We're all set, let's get your image :")
    return file_path

def get_user_mood():
    mood = input("Feel free to enter a mood from the below list :\n Happy \n Angry \n Sad \n Surprise \n Fear")
    return mood

print("User Logged in :",str(datetime.now()))
print("CaptionMe.ai : predicting your next instagram caption")
time.sleep(2)

print("Analysing corpora of captions and generating feature vectors . . .")
print("Getting your predictions ready . . .")

caption_db_loc = read_captions_csv("../caption_data/captions_csv.csv")
celeb_personality_vectors = read_celeb_csv("../caption_data/celeb_tweets.csv")

file_path = get_user_img()

# predictedArr = main_predict(file_path)
predictedArr = ['sun_captions', 'beach_captions', 'people_captions']

print("Good news!!! We are done analysing your image.")
time.sleep(2)
print("How about you tell us how you feel about the image : ")
mood = get_user_mood()

def get_filtered_caption_list(predictedArr, mood, caption_db_loc):
    caption_file_id = open(caption_db_loc,"r")
    caption_raw_data = caption_file_id.read()
    caption_dataset = json.load(caption_raw_data)

    filtered_captions = [caption_dataset[theme][mood] for theme in predictedArr]
    filtered_captions = sum(filtered_captions, [])
    
    return(filtered_captions)


filtered_captions_list = get_filtered_caption_list(predictedArr, mood, caption_db_loc)
print("We have filtered a total of {} number of captions as per your image and the mood.".format(len(filtered_captions_list)))
time.sleep(2)
celeb = input("Who would you like to be today : \n1. Ellen\n2. BarackObama\n3. Rihanna\n4. Cristiano\n5. JustinBieber")
print("Now personalizing the top 5 captions that are best for you . . .")

def get_personalized_captions(filtered_captions_list, celeb_vector):
    # filtered_vectors = [np.array(caption_dict["vector"]) for caption_dict in filtered_captions_list]
    celeb_vector = np.array(celeb_vector)
    for caption_dict in filtered_captions_list:
        dist = np.linalg.norm(celeb_vector - caption_dict["vector"])
        caption_dict["distance"] = dist
    
    sorted_caption_list = sorted(filtered_captions_list, key=lambda vec: vec['distance'])
    return sorted_caption_list[:5]


personalized_captions = get_personalized_captions(filtered_captions_list, celeb_personality_vectors[celeb])
print("Voila !!!. Your personalized caption suggestions are ready")
print("Drum Rolls . . .")
time.sleep(3)
print("\n".join(personalized_captions))

