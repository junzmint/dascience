import pandas as pd
import numpy as np
from .utils import get_keyword_dict
def get_keyword_list_for(dict_of_word, type_of_word):
    negative_keyword_list = dict(sorted(dict_of_word.items(), key = lambda item : item[1], reverse = True))
    negative_keyword_list_N = [{ "item": key, "frequency": value[0]} for i, (key, value) in enumerate(negative_keyword_list.items()) if value[1] == type_of_word]
    return negative_keyword_list_N[:30]

def readFile():
    df = pd.read_csv("category/@fake-db/Chăm-Sóc-Thú-Cưng-processed.csv")
    return df
def getInsightInNegativeComment(negative_df):
    food_negative_df = negative_df[negative_df['product_category'] == "food"]
    fashion_negative_df= negative_df[negative_df['product_category'] == "fashion"]
    accessories_negative_df= negative_df[negative_df['product_category'] == "accessories"]
    drug_negative_df= negative_df[negative_df['product_category'] == "drugs"]
    food_negative_dict_of_word = get_keyword_dict(food_negative_df['normalize_comment'])
    food_negative_list_N = get_keyword_list_for(food_negative_dict_of_word, "N")
    food_negative_list_A = get_keyword_list_for(food_negative_dict_of_word, "A")

    fashion_negative_dict_of_word = get_keyword_dict(fashion_negative_df['normalize_comment'])
    fashion_negative_list_N = get_keyword_list_for(fashion_negative_dict_of_word, "N")
    fashion_negative_list_A = get_keyword_list_for(fashion_negative_dict_of_word, "A")

    accessories_negative_dict_of_word = get_keyword_dict(accessories_negative_df['normalize_comment'])
    accessories_negative_list_N = get_keyword_list_for(accessories_negative_dict_of_word, "N")
    accessories_negative_list_A = get_keyword_list_for(accessories_negative_dict_of_word, "A")

    return {
        "food_noun": food_negative_list_N, 
        "food_adj": food_negative_list_A,
        "fashion_noun": fashion_negative_list_N,
        "fashion_adj": fashion_negative_list_A,
        "accessories_noun": accessories_negative_list_N,
        "accessories_adj": accessories_negative_list_A,
        }

def getInsightPet():
    df = readFile()
    negative_df = df[df['rating_sentiment'] == 0]
    positive_df = df[df['rating_sentiment'] == 1]
    negative_keyword_list_N = getInsightInNegativeComment(negative_df)
    return negative_keyword_list_N