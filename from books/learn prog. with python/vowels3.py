vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input('Введите текст: ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)