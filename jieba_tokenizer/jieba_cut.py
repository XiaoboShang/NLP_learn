import jieba

def demo1():
    text = "谁能懂刚听完深度就能听到船新版本nlp的感觉,之前那个版本的nlp连ppt都没有,这个直接good,我在黑马杭州校区学两个月了,有想了解的可以问我"
    
    #cut_all=False：关键字参数，使用精确模式。False：精确模式，适合文本分析。
    list1 = jieba.lcut(text,cut_all=False)
    print(f"list1 : {list1}")

if __name__ == '__main__':
    demo1()