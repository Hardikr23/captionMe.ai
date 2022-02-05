"""
This script is responsible for reading the entire captions csv file and performing some preprocessing on them
"""

import pandas as pd

# all_data = pd.concat(map(pd.read_csv, ['/Users/hardikrathod/Desktop/captionMe/caption_data/captions_csv.csv', '/Users/hardikrathod/Desktop/captionMe/caption_data/captions_csv2.csv']))
# replace with for loop to read files and keep concating the pd
all_data_1 = pd.read_csv('/Users/hardikrathod/Desktop/captionMe/caption_data/captions_csv.csv')
all_data_2 = pd.read_csv('/Users/hardikrathod/Desktop/captionMe/caption_data/captions_csv2.csv')
all_captions_1 = all_data_1.iloc[:,2].dropna()
all_captions_2 = all_data_2.iloc[:,2].dropna()

all_captions = pd.concat([all_captions_1,all_captions_2])
all_captions = list(set(all_captions))
print(len(all_captions))
print(type(all_captions))