def glas(phrase: str) -> set:
    '''Поиск гласных во фразе'''
    vowels = set('aeiouy')
    return vowels.intersection(set(phrase))
glas('trrffggh')


def letters(phrase, letters='aeuio') -> str:  # 'второй аргумент не обязателен
    '''Поиск во фразе указанных букв'''
    return set(phrase).intersection(set(letters))
