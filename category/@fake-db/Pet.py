import pandas as pd
import numpy as np

def readFile():
    df = pd.read_csv('category/@fake-db/Chăm-Sóc-Thú-Cưng-processed.csv')
    print(df.head())
