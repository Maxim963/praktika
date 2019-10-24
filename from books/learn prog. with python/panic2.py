phrase = list("Don't panic!")
fir = ''.join(phrase[1:3:1])
sec = ''.join(phrase[4:8:3])
new_phrase = fir + ' ' + sec + phrase[6]
print(new_phrase)