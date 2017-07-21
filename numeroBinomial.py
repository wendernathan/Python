import Fatorial_recusiva

n = int(input('Digite o valor de n'))
k = int(input('Digite o valor de k'))

binomi = float((Fatorial_recusiva(n)) / Fatorial_recusiva(k) * (Fatorial_recusiva(n - k)))

print('Numero Binominal {}'.format(binomi))
