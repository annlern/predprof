#3
'''
s-вводимое названние magic_herb_3
count- количество в аптеке
name - название злья с самы большим количеством в аптеках
max - максимальное количество
'''
max=0
with open('magical.csv') as f:
    a = f.readlines()
s = input()
while s!='СТОП':
    t = 0
    for i in range(1, len(a)):
        p = a[i].split(',')
        if p[4]==s:
            t = 1
            for i in range(1, len(a)):
                p = a[i].split(',')
                if intp[0]==s and p[1]>max:
                    max=int(p[1])
                    name = p[0]
                    count= p[1]
    if t==0: print('Такую траву мы не используем')
    else:  print( s + 'используется в' + name + 'его количество составляет:' + count) 
