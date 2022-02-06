from captions_users_vectorisation import *
from image_classification import *

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

predictedArr = image_classification.main_predict(file_path)

print("Good news!!! We are done analysing your image.")
time.sleep(2)
print("How about you tell us how you feel about the image : ")
mood = get_user_mood()

def fetch_caption_list(predictedArr, mood, caption_db_loc, )
for detected_themes in predictedArr:


