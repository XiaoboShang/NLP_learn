# onehot编码
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import jieba
from tensorflow.keras.preprocessing.text import Tokenizer
import joblib

def one_hot_gen():
    vocabs = ['暴龙', '水牛', '熊大', '特普', '美国', '中国']
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(vocabs)

    # print(tokenizer.word_index)
    # {'暴龙': 1, '水牛': 2, '熊大': 3, '特普': 4, '美国': 5, '中国': 6}
    for vocab in vocabs:
        zero_vector = [0] * len(vocabs)
        index = tokenizer.word_index[vocab] - 1
        zero_vector[index] = 1
        # print(f"{vocab} 的 one-hot 编码为: {zero_vector}")

    joblib.dump(tokenizer, 'jieba_tokenizer/model/one_hot_tokenizer.pkl')

def use_one_hot():
    tokenzier = joblib.load('jieba_tokenizer/model/one_hot_tokenizer.pkl')
    token = "暴龙"
    zero_vector = [0] * len(tokenzier.word_index)
    index = tokenzier.word_index[token] - 1
    zero_vector[index] = 1
    print(f"{token} 的 one-hot 编码为: {zero_vector}")

def simple_one_hot():
    vocabs = ['暴龙', '水牛', '熊大', '特普', '美国', '中国']
    word_index = {vocab: idx for idx, vocab in enumerate(vocabs)}
    print(word_index)

if __name__ == '__main__':
    # one_hot_gen()
    # use_one_hot()
    simple_one_hot()