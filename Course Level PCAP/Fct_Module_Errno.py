# Les fonctions du module ERRNO en python
Ce module met à disposition des symboles du système standard errno. La valeur de chaque symbole est la valeur entière correspondante.
Les noms et les descriptions sont empruntés à linux/include/errno.h, qui devrait être assez exhaustif.

#errno.errorcode

Dictionnaire associant la valeur errno au nom de chaîne dans le système sous-jacent.
Par exemple, errno.errorcode[errno.EPERM] correspond à 'EPERM'.

import errno
print(errno.errorcode)

#errno.EPERM
Operation not permitted. This error is mapped to the exception PermissionError.
   
import errno
print(errno.errorcode)
