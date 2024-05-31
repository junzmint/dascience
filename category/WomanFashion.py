import pandas as pd
import numpy as np

from multiprocessing import Pool
from .utils import get_keyword_dict

def get_keyword_list_for(dict_of_word, type_of_word):
    keyword_list = dict(sorted(dict_of_word.items(), key = lambda item : item[1], reverse = True))
    keyword_list_N = [{ "item": key, "frequency": value[0]} for i, (key, value) in enumerate(keyword_list.items()) if value[1] == type_of_word]
    return keyword_list_N[:30]

def readFile():
    return pd.read_csv("category/@fake-db/Thời-Trang-Nữ-processed.csv")

def process_category(category, df):
    category_df = df[df['product_category'] == category]
    dict_of_word = get_keyword_dict(category_df['normalize_comment_token'])
    list_N = get_keyword_list_for(dict_of_word, "N")
    list_A = get_keyword_list_for(dict_of_word, "A")
        
    return {
        f"{category}_noun": list_N,
        f"{category}_adj": list_A
    }

def getInsightInComment(df):
    product_categories = [
        "t-shirt",
        "sport",
      "pyjama",
      "polo",
      "shorts",
      "sock",
      "bra",
      "panties",
      "hoodie",
      "jacket",
    ]
        
    with Pool() as pool:
        results = pool.starmap(process_category, [(category, df) for category in product_categories])

    insight_dict = {}
    for result in results:
        insight_dict.update(result)

    return insight_dict
    
def getInsightWomanFashion(type):
    df = readFile()
    df.dropna(subset=['normalize_comment'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    if type == "negative":
        negative_df = df[df['rating_sentiment'] == 0]
        keyword_list = getInsightInComment(negative_df)
        return keyword_list
    
    if type == "positive":
        positive_df = df[df['rating_sentiment'] == 1]
        keyword_list = getInsightInComment(positive_df)
        return keyword_list
