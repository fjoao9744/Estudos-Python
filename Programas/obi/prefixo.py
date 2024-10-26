n = int(input()) #carcteres da 1° palavra
p1 = str(input())  #1° palavra
m = int(input()) #carcteres da 1° palavra
s1 = str(input()) #2° palavra

resul = 0



for c, v in p1, s1:
    if c == v:
        resul += 1
    else:
        break



print(resul)



