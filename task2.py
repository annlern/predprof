#2
def insertin_sort(a):
    for i in range (1, len(a)):
        j=i
        k=0
        k=int(a[j][1])
        b=0
        b=int(a[j-1][1])
        while (j>0 and k<b):
            a[j], a[j-1] = a[j-1], a[j]
            j=j-1
            k=0
            k=int(a[j][1])
            b=0
            b=int(a[j-1][1])
with open('magical.csv') as f:
    a=[f. readline()]
    s=[]
    for p in f:
        s.append(p.strip('\n').split(','))
s=intertion_sort(s)
for i in range(len(s)-1, -1,-1):
    print('Зелья'+ s[i][4] + 'осталоось' + s[i][1])
