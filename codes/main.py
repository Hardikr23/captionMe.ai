from captions_users_vectorisation import *
from image_clasification import *

import time
from datetime import datetime

def get_user_img():
    file_path = input("We're all set, let's get your image :\n")
    return file_path

def get_user_mood():
    mood = input("Feel free to enter a mood from the below list :\n Happy \n Angry \n Sad \n Surprise \n Fear\n")
    return mood

def get_filtered_caption_list(predictedArr, mood, caption_db_loc):
    caption_file_id = open("/Users/anahitabilimoria/Desktop/captionMe.ai/codes/all_captions_info.json","r")
    # caption_raw_data = caption_file_id.read()
    caption_dataset = json.load(caption_file_id)

    filtered_captions = [caption_dataset[theme][mood] for theme in predictedArr]
    filtered_captions = sum(filtered_captions, [])
    
    return(filtered_captions)

def get_personalized_captions(filtered_captions_list, celeb_vector):
    # filtered_vectors = [np.array(caption_dict["vector"]) for caption_dict in filtered_captions_list]
    # celeb_vector = np.array(celeb_vector)
    for caption_dict in filtered_captions_list:
        cap_vec= caption_dict["vector"].values()
        dist = np.linalg.norm(np.array(celeb_vector) - np.array(list(cap_vec)))
        caption_dict["distance"] = dist
    
    sorted_caption_list = sorted(filtered_captions_list, key=lambda vec: vec['distance'])
    sorted_caption_list= [x["caption"] for x in sorted_caption_list]
    return sorted_caption_list[:5]

print("User Logged in : {}\n".format(str(datetime.now())))
# print()
print("CaptionMe.ai : predicting your next instagram caption\n")
# print()
time.sleep(2)

print("Analysing corpora of captions and generating feature vectors . . .\n")
# print()
print("Getting your predictions ready . . .\n")
# print()

# caption_db_loc = read_captions_csv("./caption_data/themes_captions.csv")
caption_db_loc = "/Users/anahitabilimoria/Desktop/captionMe.ai/codes/all_captions_info.json"
# celeb_personality_vectors = read_celeb_csv("./caption_data/celeb_tweets.csv")
cele_data  = open("celeb_emotion_dict.json", 'r')
celeb_personality_vectors = json.load(cele_data)

while True:
    # Get image path from user
    try:
        file_path = get_user_img()

        predictedArr = main_predict(file_path)
        # predictedArr = ['sun_captions', 'beach_captions', 'people_captions']

        print("Good news!!! We are done analysing your image.")
        print()
        time.sleep(2)
        print("How about you tell us how you feel about the image : ")
        print()
        mood = get_user_mood()



        filtered_captions_list = get_filtered_caption_list(predictedArr, mood, caption_db_loc)
        print("We have filtered a total of {} number of captions as per your image and the mood.".format(len(filtered_captions_list)))
        print()
        time.sleep(2)
        celeb = input("Who would you like to be today : \n1. Ellen\n2. BarackObama\n3. Rihanna\n4. Cristiano\n5. JustinBieber\n")
        print("Now personalizing the top 5 captions that are best for you . . .")
        print()




        personalized_captions = set(get_personalized_captions(filtered_captions_list, celeb_personality_vectors[celeb]))
        print("Voila !!!. Your personalized caption suggestions are ready")
        print()
        print("*Drum Roll* . . .")
        print()
        time.sleep(3)
        print("\n".join(personalized_captions))

        user_decision=input("if you want to continue press enter or if you wish to exit, type bye")
        print()
        if user_decision.lower() == "bye":
            print("see you soon mate\n\t\t\t\t -CaptionMe.ai")
            print()
            break
        else:
            continue
    except Exception as e:
        print("Sorry something went wrong in the process.....duh\n Lets try with another image")
        print()
