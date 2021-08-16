frase = str(input('digite uma frase ')).lower().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
