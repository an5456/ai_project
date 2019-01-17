import re


class Regular:
    def __init__(self, str_f):
        self.str_f = str_f

    # 匹配所有的数字
    def get_numbers(self):
        return re.findall('\d', self.str_f)

    # 匹配所有的邮箱
    def get_emails(self):
        ret = '[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z_]{1,13}\.[com,cn,net]{1,3}$'
        return re.findall(ret, self.str_f)

    # 方法可以匹配出所有的ip
    def get_ips(self):
        rep = re.findall('((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))', self.str_f)
        return rep

    # 方法能够匹配出所有的url，url可以以http开头、https开头、ftp开头
    def get_urls(self):
        ret = '[http,https,ftp]{1,5}://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.findall(ret, self.str_f)

if __name__ == '__main__':
    s = Regular('https://www.fdsafds$%%.com')
    s1 = Regular('my mumber is 18268194892 and my email address is 289965734@qq.com,and my ip address is 192.168.1.1 and 255.666.555.222 and my url is https://www.weekfan.com and my phone home_number is 0734-6838533 and 020-85071966')
    print(s1.get_ips())
    # print(s.get_numbers())
    print(s.get_urls())
