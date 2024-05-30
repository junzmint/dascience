import pandas as pd
import numpy as np
from .utils import get_keyword_dict

def get_keyword_list_for(dict_of_word, type_of_word):
    keyword_list = dict(sorted(dict_of_word.items(), key = lambda item : item[1], reverse = True))
    keyword_list_N = [{ "item": key, "frequency": value[0]} for i, (key, value) in enumerate(keyword_list.items()) if value[1] == type_of_word]
    return keyword_list_N[:30]

def readFile():
    df = pd.read_csv("category/@fake-db/Thời-Trang-Nam-processed.csv")
    return df

def getInsightInComment(df):
    t_shirt_df = df[df['product_category'] == "t-shirt"]
    shirt_df = df[df['product_category'] == "shirt"]
    sport_df = df[df['product_category'] == "sport"]
    polo_df = df[df['product_category'] == "polo"]
    jeans_df = df[df['product_category'] == "jeans"]
    shorts_df = df[df['product_category'] == "shorts"]
    jacket_df = df[df['product_category'] == "jacket"]
    belt_df = df[df['product_category'] == "belt"]
    pants_df = df[df['product_category'] == "pants"]
    underwear_df = df[df['product_category'] == "underwear"]
    hoodie_df = df[df['product_category'] == "hoodie"]
    sock_df = df[df['product_category'] == "sock"]
    footwear_df = df[df['product_category'] == "footwear"]
    accessories_df = df[df['product_category'] == "accessories"]
    hat_df = df[df['product_category'] == "hat"]
    
    t_shirt_dict_of_word = get_keyword_dict(t_shirt_df['normalize_comment_token'])
    t_shirt_list_N = get_keyword_list_for(t_shirt_dict_of_word, "N")
    t_shirt_list_A = get_keyword_list_for(t_shirt_dict_of_word, "A")
    
    shirt_dict_of_word = get_keyword_dict(shirt_df['normalize_comment_token'])
    shirt_list_N = get_keyword_list_for(shirt_dict_of_word, "N")
    shirt_list_A = get_keyword_list_for(shirt_dict_of_word, "A")
    
    sport_dict_of_word = get_keyword_dict(sport_df['normalize_comment_token'])
    sport_list_N = get_keyword_list_for(sport_dict_of_word, "N")
    sport_list_A = get_keyword_list_for(sport_dict_of_word, "A")
    
    polo_dict_of_word = get_keyword_dict(polo_df['normalize_comment_token'])
    polo_list_N = get_keyword_list_for(polo_dict_of_word, "N")
    polo_list_A = get_keyword_list_for(polo_dict_of_word, "A")
    
    jeans_dict_of_word = get_keyword_dict(jeans_df['normalize_comment_token'])
    jeans_list_N = get_keyword_list_for(jeans_dict_of_word, "N")
    jeans_list_A = get_keyword_list_for(jeans_dict_of_word, "A")
    
    shorts_dict_of_word = get_keyword_dict(shorts_df['normalize_comment_token'])
    shorts_list_N = get_keyword_list_for(shorts_dict_of_word, "N")
    shorts_list_A = get_keyword_list_for(shorts_dict_of_word, "A")
    
    jacket_dict_of_word = get_keyword_dict(jacket_df['normalize_comment_token'])
    jacket_list_N = get_keyword_list_for(jacket_dict_of_word, "N")
    jacket_list_A = get_keyword_list_for(jacket_dict_of_word, "A")
    
    belt_dict_of_word = get_keyword_dict(belt_df['normalize_comment_token'])
    belt_list_N = get_keyword_list_for(belt_dict_of_word, "N")
    belt_list_A = get_keyword_list_for(belt_dict_of_word, "A")
    
    pants_dict_of_word = get_keyword_dict(pants_df['normalize_comment_token'])
    pants_list_N = get_keyword_list_for(pants_dict_of_word, "N")
    pants_list_A = get_keyword_list_for(pants_dict_of_word, "A")
    
    underwear_dict_of_word = get_keyword_dict(underwear_df['normalize_comment_token'])
    underwear_list_N = get_keyword_list_for(underwear_dict_of_word, "N")
    underwear_list_A = get_keyword_list_for(underwear_dict_of_word, "A")
    
    hoodie_dict_of_word = get_keyword_dict(hoodie_df['normalize_comment_token'])
    hoodie_list_N = get_keyword_list_for(hoodie_dict_of_word, "N")
    hoodie_list_A = get_keyword_list_for(hoodie_dict_of_word, "A")
    
    sock_dict_of_word = get_keyword_dict(sock_df['normalize_comment_token'])
    sock_list_N = get_keyword_list_for(sock_dict_of_word, "N")
    sock_list_A = get_keyword_list_for(sock_dict_of_word, "A")
    
    footwear_dict_of_word = get_keyword_dict(footwear_df['normalize_comment_token'])
    footwear_list_N = get_keyword_list_for(footwear_dict_of_word, "N")
    footwear_list_A = get_keyword_list_for(footwear_dict_of_word, "A")
    
    accessories_dict_of_word = get_keyword_dict(accessories_df['normalize_comment_token'])
    accessories_list_N = get_keyword_list_for(accessories_dict_of_word, "N")
    accessories_list_A = get_keyword_list_for(accessories_dict_of_word, "A")
    
    hat_dict_of_word = get_keyword_dict(hat_df['normalize_comment_token'])
    hat_list_N = get_keyword_list_for(hat_dict_of_word, "N")
    hat_list_A = get_keyword_list_for(hat_dict_of_word, "A")
    
    return {
        "t_shirt_noun": t_shirt_list_N,
        "t_shirt_adj": t_shirt_list_A,
        "shirt_noun": shirt_list_N,
        "shirt_adj": shirt_list_A,
        "sport_noun": sport_list_N,
        "sport_adj": sport_list_A,
        "polo_noun": polo_list_N,
        "polo_adj": polo_list_A,
        "jeans_noun": jeans_list_N,
        "jeans_adj": jeans_list_A,
        "shorts_noun": shorts_list_N,
        "shorts_adj": shorts_list_A,
        "jacket_noun": jacket_list_N,
        "jacket_adj": jacket_list_A,
        "belt_noun": belt_list_N,
        "belt_adj": belt_list_A,
        "pants_noun": pants_list_N,
        "pants_adj": pants_list_A,
        "underwear_noun": underwear_list_N,
        "underwear_adj": underwear_list_A,
        "hoodie_noun": hoodie_list_N,
        "hoodie_adj": hoodie_list_A,
        "sock_noun": sock_list_N,
        "sock_adj": sock_list_A,
        "footwear_noun": footwear_list_N,
        "footwear_adj": footwear_list_A,
        "accessories_noun": accessories_list_N,
        "accessories_adj": accessories_list_A,
        "hat_noun": hat_list_N,
        "hat_adj": hat_list_A
    }
    
def getInsightManFashion(type):
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
