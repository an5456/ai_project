def toGoatLatin(S):
    list_s = S.split(' ')
    result = ''
    index = 1
    for i in list_s:
        if i[0] in ['a','e','i','o','u','A','E','I','O','U']:
            i =i+'ma'+'a'*index
        else:
            i=i[1:]+i[0]+'ma'+'a'*index
        index +=1
        result+=i+' '
    return result
print(toGoatLatin("I speak Goat Latin"))






#
#
# def toGoatLatin(S):
#
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     temp = S.split()
#     for i in range(len(temp)):
#         if temp[i][0].lower() in vowel:
#             temp[i] = temp[i] + 'ma' + 'a' * (i + 1)
#         else:
#             temp[i] = temp[i][1:] + temp[i][0] + 'ma' + 'a' * (i + 1)
#     return " ".join(temp).strip()
# print(toGoatLatin("I speak Goat Latin"))