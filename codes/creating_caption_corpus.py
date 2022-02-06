"""
This script is responsible for reading the entire captions csv file and performing some preprocessing on them
"""

from webbrowser import get
import pandas as pd
import nltk
import text2emotion as te
import numpy as np

def get_emotion_scores(caption_df):
    all_info_dict = {}
    for caption in caption_df:
        caption_dict = {}
        caption_dict["caption"] = caption
        emotion_vector = te.get_emotion(caption)
        caption_dict["vector"] = emotion_vector

        max_key_val = np.NINF
        max_key = ""
        for key in emotion_vector.keys():
            if emotion_vector[key] > max_key_val:
                max_key_val = emotion_vector[key]
                max_key = key
        if max_key in all_info_dict.keys():
            all_info_dict[max_key].append(caption_dict)
        else:
            all_info_dict[max_key]=[]
            all_info_dict[max_key].append(caption_dict)
    return all_info_dict

    # all_info_list=[]
    # for caption in caption_df:
    #     caption_dict = {}
    #     caption_dict["caption"] = caption
    #     emotion_vector = te.get_emotion(caption)
    #     caption_dict["vector"] = emotion_vector
    #     max_key_val = np.NINF
    #     max_key = ""
    #     for key in emotion_vector.keys():
    #         if emotion_vector[key] > max_key_val:
    #             max_key_val = emotion_vector[key]
    #             max_key = key
    #     caption_dict["mood"] = max_key
    #     all_info_list.append(caption_dict)
    #     return(all_info_list)


all_themes_captions = pd.read_csv('/Users/hardikrathod/Desktop/captionMe/caption_data/themes_captions.csv')
# all_captions_1 = all_data_1.iloc[:,2].dropna()
total_columns = all_themes_captions.shape[0]

beach_captions = all_themes_captions.iloc[:,0].dropna()
sun_captions = all_themes_captions.iloc[:,1].dropna()
trees_captions = all_themes_captions.iloc[:,2].dropna()
car_captions = all_themes_captions.iloc[:,3].dropna()
people_captions = all_themes_captions.iloc[:,4].dropna()
dog_captions = all_themes_captions.iloc[:,5].dropna()
food_captions = all_themes_captions.iloc[:,6].dropna()
building_captions = all_themes_captions.iloc[:,7].dropna()
road_captions = all_themes_captions.iloc[:,8].dropna()

print(len(beach_captions.index))
print(len(sun_captions.index))
print(len(trees_captions.index))
print(len(car_captions.index))
print(len(people_captions.index))
print(len(dog_captions.index))
print(len(food_captions.index))
print(len(building_captions.index))
print(len(road_captions.index))

all_captions_df_dict = {"beach_captions":beach_captions,
                        "sun_captions":sun_captions,
                        "trees_captions":trees_captions,
                        "car_captions":car_captions,
                        "people_captions":people_captions,
                        "dog_captions":dog_captions,
                        "food_captions":food_captions,
                        "building_captions":building_captions,
                        "road_captions":road_captions
                        }

all_caption_info_dict = {}
for caption_set in all_captions_df_dict.keys():
    all_caption_info_dict[caption_set] = get_emotion_scores(all_captions_df_dict[caption_set])
# print(all_caption_info_dict)
