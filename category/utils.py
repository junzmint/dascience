from pyvi import ViTokenizer, ViPosTagger
import unicodedata
import itertools 
def normalize_comment(cmt):
  return unicodedata.normalize('NFD', cmt)

def buildListFromFile(ppath: str):
    """
    Tạo List[str] chứa các từ trong ppath

    Args:
        ppath (str): đường dẫn đến file cần đọc

    Returns:
        (List[str]):
    """
    d = []

    with open(ppath) as rows:
        for row in rows:
          row = row.replace("\n","")
          row = normalize_comment(row)
          d.append(row)
          if row == "chó":
            print(row)
            break

    return d

def get_keyword_dict(df):
  stopwords = buildListFromFile("category/@fake-db/stopwords.txt")
  dict_of_word ={}
  for line in df:
    words_and_tags = eval(line)
    for word, tag in zip(words_and_tags[0], words_and_tags[1]):
      word = normalize_comment(word)
      if word not in stopwords:
        if word in dict_of_word:
          dict_of_word[word][0] = dict_of_word[word][0] + 1
        else:
          dict_of_word[word] = []
          dict_of_word[word].append(1)
          dict_of_word[word].append(tag)

  # word_list = []
  # for i, (word, frequency) in enumerate(dict_of_word.items()):
  #   obj = {}
  #   obj['word'] = word
  #   obj['frequency'] = frequency
  #   word_list.append(obj)
  #   if i == 30:
  #     break

  return dict_of_word