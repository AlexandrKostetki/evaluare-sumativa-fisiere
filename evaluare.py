with open('Desktop/input.txt','r') as f:
    linii=f.readlines()
print('Nr) NumelePRENUMELE NOTA1 NOTA2 NOTA3\n',linii)
with open('Desktop/rezerva.txt','w') as f:
    for i in linii:
        f.write(i)
for i in linii:
    linii2=i.split()
    n=linii2[0]+''+linii2[1]+''+linii2[2]
    nm=str(linii2[3])+(linii2[4])+(linii2[5])
    m=n+''+nm+'\n'
    with open ('Desktop/Output.txt','a') as f:
        f.write(m)
    with open('Desktop/Output.txt','w') as f:
        linii3=f.readlines()
    print('Nr) Numele PRENUMELE media\n',linii3)
