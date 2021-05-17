a = str(input())
a = a.lower()
vowel = ['a', 'o', 'y', 'e', 'u', 'i']


def XuLyChuoi(a):
    string = ""
    for i in a:
        if i in vowel:
            i = ''
        else:
            i = str('.') + str(i)
        string = string + i
    return string


print(XuLyChuoi(a))