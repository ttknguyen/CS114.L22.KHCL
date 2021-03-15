s = input()
s = s.lower()

tmp = ""
na = ['a', 'o', 'y', 'e', 'u', 'i']
for i in range(len(s)):
    if s[i] not in na:
        tmp +=  '.' + s[i]

print(tmp)
