import re
class ReadFile():
    # 获取文件的信息，切分根据开头数字取出后面对应的信息
    def read_file(self, file_num):
        with open('../homework_02/answer_info', encoding='utf-8') as f:
            s = f.readlines()
            for i in s:
                h = i.split('.')
                if file_num in h[0]:
                    return '\033[33m%s\033[0m' % h[1]
                continue

    # 判断是否切分字符串格式化输出
    def format_out(self, fie):
        try:
            if '>' in fie:
                file_split = fie.split('>')
                file_len = len(file_split)
                for i in range(file_len):
                    s = '\t' + file_split[i] + '\t'
                    print(s)
            else:
                print('\t' + fie)
        except TypeError:
            print("值不存在")
     # 换行输出
    def for_split(self, file_num,flg=None):
        s = self.read_file(file_num).split('>')
        if flg is not None:
            for i in range(1, len(s) - 1):
                print('\t'+s[i])
        else:
            print(s[0])
    # 判断字符中包含的数字
    def te(self, f):
        j = len(re.findall('\d', f))
        print(j)

    def test_phone(self, f):
        # # li = []
        h = re.findall('\d{11}', f)
        # print(h)
        for s in h:
            reg = '^((18[4,7])|(17[1,6])|(13[3,8]))\d{8}$'
            u = re.findall(reg, s)
            if u:
                print(s)
    def test_ip(self, ip):
        h ='(\d{1,3}.){3}\d{1,3}'
        j = re.search(h, ip)[1]
        print(j)

    # 判断读取一行还是两行同时读取
    def get_info(self, yes, num1='', num2=None):
        if yes == '2':
            return self.format_out(self.read_file(num1) + '\t' + self.read_file(num2))
        else:
            return self.format_out(self.read_file(num1))


if __name__ == '__main__':
    s = ReadFile()
    # s.read_file('6')
    # s.format_out(s.read_file('6'))
    # s.get_info('1', '6')
    # s.for_split('6')
    # s.for_split('6','1')
    # s.te('42197里包含几个数字啊？')
    # print(s.test_ip('下边的号码中，哪些是手机号呢:18475309876,18719462345,17665148777,13332839908,12398028761'))
    s.test_ip('1324.231.432.1234,192.168.1.6,10.25.11.8这些信息中，哪些是ip呢')

