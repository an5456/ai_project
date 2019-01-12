# def uniqueMorseRepresentations(words):
#     code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
#             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
#     ditc = {}
#     li = []
#     a_assic = ord('a')
#     for i in range(26):
#         ditc[chr(a_assic + i)] = code[i]
#     for s in words:
#         lis = []
#         for y in s:
#             lis += ditc[y.lower()]
#         if lis not in li:
#             li.append(lis)
#     return len(li)
#
#
# print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
# print(type("" + "-." + "--.."))


def uniqueMorseRepresentations(words):
    r = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    w = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    dic = dict(zip(w, r))
    li = []
    for i in words:
        s = ""
        for y in i:
            s+=dic.get(y)
        li.append(s)
    return len(set(li))
print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

