import pandas as pd
import numpy as np
from .utils import get_keyword_dict

def get_keyword_list_for(dict_of_word, type_of_word):
    keyword_list = dict(sorted(dict_of_word.items(), key = lambda item : item[1], reverse = True))
    keyword_list_N = [{ "item": key, "frequency": value[0]} for i, (key, value) in enumerate(keyword_list.items()) if value[1] == type_of_word]
    return keyword_list_N[:30]

def readFile():
    df = pd.read_csv("category/@fake-db/Sức-Khỏe-processed.csv")
    return df

def getInsightInComment(df):
    q_tip_df = df[df['product_category'] == "q-tip"]
    healthcare_df = df[df['product_category'] == "heathcare"]
    condoms_df = df[df['product_category'] == "condoms"]
    mask_df = df[df['product_category'] == "mask"]
    self_hygiene_df = df[df['product_category'] == "self-hygiene"]
    massage_df = df[df['product_category'] == "massage"]
    contact_lens_df = df[df['product_category'] == "contact-lens"]
    vitamins_df = df[df['product_category'] == "vitamins"]
    drugs_df = df[df['product_category'] == "drugs"]
    accessories_df = df[df['product_category'] == "accessories"]

    q_tip_dict_of_word = get_keyword_dict(q_tip_df['normalize_comment_token'])
    q_tip_list_N = get_keyword_list_for(q_tip_dict_of_word, "N")
    q_tip_list_A = get_keyword_list_for(q_tip_dict_of_word, "A")
    
    healthcare_dict_of_word = get_keyword_dict(healthcare_df['normalize_comment_token'])
    healthcare_list_N = get_keyword_list_for(healthcare_dict_of_word, "N")
    healthcare_list_A = get_keyword_list_for(healthcare_dict_of_word, "A")
    
    condoms_dict_of_word = get_keyword_dict(condoms_df['normalize_comment_token'])
    condoms_list_N = get_keyword_list_for(condoms_dict_of_word, "N")
    condoms_list_A = get_keyword_list_for(condoms_dict_of_word, "A")
    
    mask_dict_of_word = get_keyword_dict(mask_df['normalize_comment_token'])
    mask_list_N = get_keyword_list_for(mask_dict_of_word, "N")
    mask_list_A = get_keyword_list_for(mask_dict_of_word, "A")
    
    self_hygiene_dict_of_word = get_keyword_dict(self_hygiene_df['normalize_comment_token'])
    self_hygiene_list_N = get_keyword_list_for(self_hygiene_dict_of_word, "N")
    self_hygiene_list_A = get_keyword_list_for(self_hygiene_dict_of_word, "A")
    
    massage_dict_of_word = get_keyword_dict(massage_df['normalize_comment_token'])
    massage_list_N = get_keyword_list_for(massage_dict_of_word, "N")
    massage_list_A = get_keyword_list_for(massage_dict_of_word, "A")
    
    contact_lens_dict_of_word = get_keyword_dict(contact_lens_df['normalize_comment_token'])
    contact_lens_list_N = get_keyword_list_for(contact_lens_dict_of_word, "N")
    contact_lens_list_A = get_keyword_list_for(contact_lens_dict_of_word, "A")
    
    vitamins_dict_of_word = get_keyword_dict(vitamins_df['normalize_comment_token'])
    vitamins_list_N = get_keyword_list_for(vitamins_dict_of_word, "N")
    vitamins_list_A = get_keyword_list_for(vitamins_dict_of_word, "A")
    
    drugs_dict_of_word = get_keyword_dict(drugs_df['normalize_comment_token'])
    drugs_list_N = get_keyword_list_for(drugs_dict_of_word, "N")
    drugs_list_A = get_keyword_list_for(drugs_dict_of_word, "A")
    
    accessories_dict_of_word = get_keyword_dict(accessories_df['normalize_comment_token'])
    accessories_list_N = get_keyword_list_for(accessories_dict_of_word, "N")
    accessories_list_A = get_keyword_list_for(accessories_dict_of_word, "A")
    
    return {
        "q-tip_noun": q_tip_list_N, 
        "q-tip_adj": q_tip_list_A,
        "healthcare_noun": healthcare_list_N,
        "healthcare_adj": healthcare_list_A,
        "condoms_noun": condoms_list_N,
        "condoms_adj": condoms_list_A,
        "mask_noun": mask_list_N,
        "mask_adj": mask_list_A,
        "self-hygiene_noun": self_hygiene_list_N,
        "self-hygiene_adj": self_hygiene_list_A,
        "massage_noun": massage_list_N,
        "massage_adj": massage_list_A,
        "contact-lens_noun": contact_lens_list_N,
        "contact-lens_adj": contact_lens_list_A,
        "vitamins_noun": vitamins_list_N,
        "vitamins_adj": vitamins_list_A,
        "drugs_noun": drugs_list_N,
        "drugs_adj": drugs_list_A,
        "accessories_noun": accessories_list_N,
        "accessories_adj": accessories_list_A,
    }
    
def getInsightHealth(type):
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
