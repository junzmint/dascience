import pandas as pd
import numpy as np
from .utils import get_keyword_dict

def get_keyword_list_for(dict_of_word, type_of_word):
    keyword_list = dict(sorted(dict_of_word.items(), key = lambda item : item[1], reverse = True))
    keyword_list_N = [{ "item": key, "frequency": value[0]} for i, (key, value) in enumerate(keyword_list.items()) if value[1] == type_of_word]
    return keyword_list_N[:30]

def readFile():
    df = pd.read_csv("category/@fake-db/Chăm-Sóc-Thú-Cưng-processed.csv")
    return df

def getInsightInComment(df):
    food_df = df[df['product_category'] == "food"]
    fashion_df= df[df['product_category'] == "fashion"]
    accessories_df= df[df['product_category'] == "accessories"]
    drug_df= df[df['product_category'] == "drugs"]
    
    food_dict_of_word = get_keyword_dict(food_df['normalize_comment_token'])
    food_list_N = get_keyword_list_for(food_dict_of_word, "N")
    food_list_A = get_keyword_list_for(food_dict_of_word, "A")

    fashion_dict_of_word = get_keyword_dict(fashion_df['normalize_comment_token'])
    fashion_list_N = get_keyword_list_for(fashion_dict_of_word, "N")
    fashion_list_A = get_keyword_list_for(fashion_dict_of_word, "A")

    accessories_dict_of_word = get_keyword_dict(accessories_df['normalize_comment_token'])
    accessories_list_N = get_keyword_list_for(accessories_dict_of_word, "N")
    accessories_list_A = get_keyword_list_for(accessories_dict_of_word, "A")

    drug_dict_of_word = get_keyword_dict(drug_df['normalize_comment_token'])
    drug_list_N = get_keyword_list_for(drug_dict_of_word, "N")
    drug_list_A = get_keyword_list_for(drug_dict_of_word, "A")
    
    return {
        "food_noun": food_list_N, 
        "food_adj": food_list_A,
        "fashion_noun": fashion_list_N,
        "fashion_adj": fashion_list_A,
        "accessories_noun": accessories_list_N,
        "accessories_adj": accessories_list_A,
        "drug_noun": drug_list_N,
        "drug_adj": drug_list_A,
        }

def getInsightPet(type):
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
