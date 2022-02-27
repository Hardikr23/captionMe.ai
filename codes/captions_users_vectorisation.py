import pandas as pd
import text2emotion as te
import numpy as np
import json
import nltk
nltk.download('omw-1.4')

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

def read_captions_csv(captions_csv_file_path):
    # all_themes_captions = pd.read_csv('/Users/hardikrathod/Desktop/captionMe/caption_data/themes_captions.csv')
    # total_columns = all_themes_captions.shape[0]

    all_themes_captions = pd.read_csv(captions_csv_file_path)

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

    outfile_path = "all_captions_info.json"
    outfile_id = open(outfile_path,"w")
    outfile_id.write(json.dumps(all_caption_info_dict))
    outfile_id.close()
    print("written all caption data to all_captions_info.json", )
    return(outfile_path)
    # pending writes in Neo4j

def generate_celeb_vector(celebrity):
    Text = celebrity.content.reset_index(drop=True)
    n=len(Text)
    empty =[]
    Happycount =0
    Angrycount=0
    Surprisecount=0
    Sadcount=0
    fearcount = 0
    for i in range(len(Text)):
        sccore = te.get_emotion(Text[i])
        empty.append(sccore)
        keys =list(sccore.keys())
        values = list(sccore.values())
        max_idx =  values.index(max(values))
        max_key = keys[max_idx]
        #print(max_key)
        if max_key == 'Happy':
            Happycount += 1
        elif max_key == 'Angry':
            Angrycount += 1
        elif max_key == 'Surprise':
            Surprisecount += 1
        elif max_key == 'Sad':
            Sadcount += 1
        else:
            fearcount += 1
    arr = np.array([Happycount/n,Angrycount/n,Surprisecount/n,Sadcount/n,fearcount/n])
    return arr

def read_celeb_csv(celeb_file_path):
    dataframe = pd.read_csv(celeb_file_path)
    ellen=dataframe.query('author == "TheEllenShow"')
    barack=dataframe.query('author == "BarackObama"')
    rihanna=dataframe.query('author == "rihanna"')
    cristiano=dataframe.query('author == "Cristiano"')
    justinbieber=dataframe.query('author == "justinbieber"')
    celeb_dict = {
        "Ellen": ellen,
        "BarackObama": barack,
        "Rihanna": rihanna,
        "Cristiano": cristiano,
        "JustinBieber": justinbieber
    }
    celeb_emotion_dict={}
    for celeb in celeb_dict.keys():
        celeb_emotion_dict[celeb]=generate_celeb_vector(celeb_dict[celeb])
    return celeb_emotion_dict