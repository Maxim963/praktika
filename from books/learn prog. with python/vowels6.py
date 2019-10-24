vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input('Введите текст: ')
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')
pppp = '|'.join(vowels)
print(pppp)
lll = pppp.split('|')
print(lll)