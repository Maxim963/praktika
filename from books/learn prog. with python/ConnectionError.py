class ConnectionError(Exception):
    pass
# raise ConnectionError('Стоит ли паниковать? Нету коннекта.')
try:
    raise ConnectionError('What"s up?')
except ConnectionError as err:
    print('Chto delat? ', err)