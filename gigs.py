#!/usr/bin/python
from sys import argv

if len(argv) != 1 and argv[1]=='-h':
    print('Usage \npython3 gigs.py <size> <output filename> <memory buffer> <-h>')
    quit()
def verbose(txt):
    if verb:
        if nan:
            print('[Verbose] '+txt)
        else:
            print(Fore.GREEN+'[Verbose] '+txt+Style.RESET_ALL)
verb=False
for j in range(0,len(argv)):
    if argv[j] == '-v':
        nan=False
        try:
            from colorama import Fore, Back, Style
        except ModuleNotFoundError:
            import os
            os.system('python3 -m pip install colorama')
            try:
                from colorama import Fore, Back, Style
            except ModuleNotFoundError:
                nan=True
        verb=True
        verbose('Args : '+str(argv))
        del argv[j]
        break

def remplir(taille,nom,buffer=500000):
    taille=int(taille)
    buffer=int(buffer)
    f=open(nom,'wb')
    verbose('The file \'{}\' was created'.format(nom))
    #f.write(b'\xff'*taille)
    if int(taille/buffer)==0:
        verbose('File size ({}o) is inferior to the buffer size ({}o) so writing directlly into the file {}o'.format(str(taille),str(buffer),str(taille)))
        f.write(b'\xff'*taille)
    else:
        verbose('File size ({}o) is superior to the buffer size ({}o) so, writing {}o {} times plus {}o'.format(str(taille),str(buffer),str(buffer),str(int(taille/buffer)),str(taille-(buffer*int(taille/buffer)))))
        left=taille
        for i in range(int(taille/buffer)+1):
            if left > buffer:
                verbose('Adding {}o for the {} time'.format(str(buffer),str(i+1)))
                f.write(b'\xff'*buffer)
                left -= buffer
            else:
                verbose('Adding {}o'.format(str(left)))
                f.write(b'\xff'*left)
                left = 0
                break

if len(argv)==2:
    taille=argv[1]
    remplir(taille,'bombe.txt')
elif len(argv)==3:
    remplir(argv[1],argv[2])
elif len(argv)==4:
    remplir(argv[1], argv[2], argv[3])
else:
    taille=int(input('Taille du fichier : '))
    remplir(taille,'big-file.txt')
    print('Done !')
verbose('Tanks for using gigs.py. This softwear was created by Guillaume Favier.')
