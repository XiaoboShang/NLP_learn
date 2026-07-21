import jieba

def demo1():
    text = "谁能懂刚听完深度就能听到船新版本nlp的感觉,之前那个版本的nlp连ppt都没有,这个直接good,我在黑马杭州校区学两个月了,有想了解的可以问我"
    
    #cut_all=False：关键字参数，使用精确模式。False：精确模式，适合文本分析。
    list1 = jieba.lcut(text,cut_all=False)
    print(f"list1 : {list1}")

def demo2():
    text = "谁能懂刚听完深度就能听到船新版本nlp的感觉,之前那个版本的nlp连ppt都没有,这个直接good,我在黑马杭州校区学两个月了,有想了解的可以问我"
    
    #cut_all=True：关键字参数，使用全模式。True：全模式，把句子中所有的可以成词的词语都扫描出来，速度非常快，但是不能解决歧义。
    list2 = jieba.lcut(text,cut_all=True)
    print(f"list2 : {list2}")

#搜索引擎模式
def demo3():
    text = "谁能懂刚听完深度就能听到船新版本nlp的感觉,之前那个版本的nlp连ppt都没有,这个直接good,我在黑马杭州校区学两个月了,有想了解的可以问我"
    
    list3 = jieba.lcut_for_search(text)
    print(f"list3 : {list3}")

def demo4():
    text = "我是旋风无敌雷霆暴龙战士大帅哥"
    list1 = jieba.lcut(text, cut_all=False)
    print(f"list1 : {list1}")
    jieba.load_userdict("./jieba_tokenizer/data/userdict.txt")

    list2 = jieba.lcut(text, cut_all=False)
    print(f"list2 : {list2}")

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    demo4()