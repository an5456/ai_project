import re

# reg = "hellofdsaa4544f@wangscaihello"
# h = re.findall('[a-z]{4}', reg)
# print(h)
io = '1324.231.432.1234,192.168.1.6,10.25.11.8这些信息中，哪些是ip呢'
# ip = 'this is ip:192.168.1.234;192.145.56.788'
j = re.findall(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", io)
print(j)


# reg = '(\d{1,3}.){3}\d{1,3}'
# h = re.search(reg, ip)[0]
# print(h)
#
# info = 'pytoppppytofdsaf'
# f = re.findall('pyto+?', info)
# print(f)
# f = re.findall('pyto*?', info)
# print(f)
# f = re.findall('pyto??', info)
# print(f)
# s = '下边的号码中，哪些是手机号呢:18475309876,18719462345,17665148777,13332839908,12398028761'
# h = re.findall('\d{11}',s)
# print(h)
# def test(f):
#     h = re.findall('\d{11}', f)
#     for i in h:
#         reg = '^((18[4,7])|(17[1,6])|(13[3,8]))\d{8}$'
#         h = re.findall(reg, i)
#         if h:
#             print('匹配成功')
#             print(i)
#         else:
#             print('匹配失败')
#
#
# test('下边的号码中，哪些是手机号呢:18475309876,18719462345,17665148777,13332839908,12398028761')
# j = '42197393里包含几个数字啊'
# h = len(re.findall('\d', j))

# def test(f):
#     j = len(re.findall('\d', f))
#     return j
# print(test('42197543543543543里包含几个数字啊'))
