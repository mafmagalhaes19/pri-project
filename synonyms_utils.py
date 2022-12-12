import nltk
import pandas as pd
import enchant
import csv

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('word_tokenize')

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sw = set(stopwords.words('english'))


dictionary = enchant.Dict("en_US")


all_words = set()
all_synonims = []

df = pd.read_csv('datasets/final_data.csv')
final_csv = pd.DataFrame(columns=["Synonyms"])

def get_all_synonym(word, wd):
    for sense in wn.synsets(word):
        for names in sense.lemmas():
            wd.add(names.name())

def check_synonym(word, word_check):
    for sense in wn.synsets(word):
        for names in sense.lemmas():
            if word_check in names.name():
                return True
    
    return False

def get_all_words(str, final):

    word_tokens = word_tokenize(str)

    filtered_sentence = [w for w in word_tokens if not w.lower() in sw]

    filtered_sentence = []
    for w in word_tokens:
        if w not in sw:
            filtered_sentence.append(w)

    output = set([el  for el in filtered_sentence if len(el)>1 and el.isalpha() and dictionary.check(el)])

    final.update(output)

def convert_element(str, output):
    str_1 = str[1:len(str)-1]
    str_2 = str_1.split(',')
    for i in str_2:
        str_3 = i.strip()
        output.add(str_3[1:len(str_3)-1].lower())


def add_all_words(df, words_list):
    lists = df['reviews'].tolist()
    lists_final = set()
    
    for i in lists:
        convert_element(i, lists_final)
        print("convertendo")
    for j in lists_final:
        get_all_words(j, words_list)
        print("separando palavras")

def add_synonim(synonyms_list, words):
    wd = set()
    
    for i in words:
        
        csvFile = open('synonyms.csv', 'a', encoding="utf-8")
        get_all_synonym(i, wd)
        if wd not in synonyms_list:
            print('checando')
            synonyms_list.append(wd)
        b = list(wd)
        for w in range(0, len(b)):
            if(w == len(b)-1):
                csvFile.write(f"{b[w]}\n")
            else:
                csvFile.write(f"{b[w]}"+', ')
        wd.clear()
        csvFile.close()
            #for j in synonyms_list:
             #   e = next(iter(j))
              #  if (check_synonym(e, i)):
               #     print("checando sinonimo")
                #    j.add(i)
                #    break
                #synonyms_list.append({i})
    csvFile.close()


def create_csv(synonyms_list, df):
    for i in synonyms_list:
        df = df.append({'Synonyms': list(i)}, ignore_index=True)
    
    df.to_csv('synonims.csv')

#print(df2)



add_all_words(df, all_words)
add_synonim(all_synonims, all_words)
#print(all_synonims

#print(get_all_words("'Most expensive McDonalds in the world"))
#text = "Good Swiss Food at Reasonable Prices"

#print(get_all_words(text))