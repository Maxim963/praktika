vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input('Введите текст: ')
found = {}
for letter in word:
    if letter in found:
        found[letter] += 1
    else:
        found[letter] = 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')