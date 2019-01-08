import re

from homewor_2.read_fiel import ReadFile


class questint_answer():
    read = ReadFile()

    def qustion_an(self):
        # 根据用户的输入，做出对应的回答
        while True:
            info = input('\033[35m用户>>>\033[0m')
            if re.findall('贪心学院是做什么的？|做什么', info):
                self.read.get_info('1')
            elif re.findall('^贪心|贪心学院', info):
                self.read.get_info('2', '1', '2')
            elif re.findall('^课程|啥课程', info):
                self.read.get_info('2', '2', '5')
            elif re.findall('方式|（学院的课程是什么方式进行上课的？）', info):
                self.read.get_info(1,'2')
            elif re.findall('什么是项目式培训呢？|项目式', info):
                self.read.get_info(1,'3')
            elif re.findall('人工智能哪家强？|^强', info):
                self.read.get_info(1,'4')
            elif re.findall('(Python+AI)课程具体更适合哪些人群呢？|更适合哪些人群', info):
                self.read.for_split('6')
                self.read.for_split('6', '1')
            elif re.findall('(Python+AI)适合什么样的同学学习？|Python', info):
                self.read.get_info(1,'5')
            elif re.findall('优势是什么？|优势', info):
                self.read.get_info(1,'7')
            elif re.findall('42197393里包含几个数字啊？|\d', info):
                self.read.te(info)
            elif info == '下边的号码中，哪些是手机号呢:18475309876,18719462345,17665148777,13332839908,12398028761':
                j = re.findall('\d{11}', info)
                print(j)

                # for s in re.findall('\d{11}', info):
                #     print(type(s))
                #     reg = '^((18[4,7])|(17[1,6])|(13[3,8]))\d{8}$'
                #     u = re.findall(reg, s)
                #     if u:
                #
                #         print(type(s))

            elif re.findall('拜拜|再见|bye', info ):
                print('\t''再见')
                break
            else:
                print('\t' + '没有查询到任何信息')


if __name__ == '__main__':
    s = questint_answer()
    s.qustion_an()
