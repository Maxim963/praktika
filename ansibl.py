import unicodedata as ud
def convert(say):
    import unicodedata as un
    sl = un.name(say)
    sl2 = un.lookup(sl)
    print("Это имя символа юникод в верхнем регистре - '%s', а это сам  символ - '%s',"
          " введено: '%s' "%(sl, sl2, say))
# while True:
#     try:
#         convert(input('Input simvol:  '))
#     except:
#         print('error')
e = 'caf\u00e9'
print(e)
v = e.encode('utf-8')
print(v)

v2 = v.decode('windows-1252')

print(v2)

n = 42
f = 3.09
s = 'stringi'
print('%5.4d %5.4f %5.4s'%(n, f, s))
print('%-5.6d %-10.3f %-5.3s'%(n, f, s))
print('%.5d %.8f %.2s'%(n, f, s))
print('{0} {1} {2} {nb}'.format(s, n, f, nb = 'Kodak'))

fn = {'m': 'Max', 'a': 'Anna', 'x': 9}
print('{0[m]:!<9} love is {0[a]:-^10} about {0[x]:|^10.2f} years{1:5.2}'.format(fn, '!!!'))
