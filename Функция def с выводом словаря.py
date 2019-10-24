def pr_kwa(**kwa):
    for a, b in kwa.items():
        print(a, b, sep=' --> ', end='\n')
    if kwa:
        print()
tip = input('Your age: ')


slov = pr_kwa(krokodil=tip, koshka='doma', sobaka='ulichnaya' )

#print(slov)
