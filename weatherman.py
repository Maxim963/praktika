from imp import report, weekly
print('Дневная погода:', report.forecast())
print('Недельная погода:')
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)