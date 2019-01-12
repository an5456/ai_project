import aiml
import jieba
kernel = aiml.Kernel()
kernel.learn("std_startup.xml")
kernel.respond("load aiml b")
while True:
    response = kernel.respond(" ".join(jieba.cut(input("请输入你的内容>>"), cut_all=False)))
    s = response.replace(" ","")
    print(s)
