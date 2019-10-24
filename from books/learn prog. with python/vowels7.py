vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
word = input('Введите текст: ')
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
