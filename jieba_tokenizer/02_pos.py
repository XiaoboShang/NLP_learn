# 词性标注 pos
import jieba.posseg as paseg

text = "我爱兰州牛肉面"
list = paseg.lcut(text)

for word,flag in list:
    print(f"词语：{word}, 词性：{flag}")
