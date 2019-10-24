count=0
for i in range(99, 0, -3):
    if i % 9 == 0:
        print(i, ' - Кратно девяти')
        count += 1
    else:
        print(i)
print(count, '- совпадений')