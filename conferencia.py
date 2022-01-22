'''
01,02,03,31,38,53
08,12,19,38,44,53
07,39,42,45,47,59
19,22,29,38,42,49
04,36,37,40,54,57
01,08,11,36,37,56
'''
# 112532374756

from libs import *

jogo = [[1, 2, 3, 31, 38, 53],
        [8, 12, 19, 38, 44, 53],
        [7, 39, 42, 45, 47, 59],
        [19, 22, 29, 38, 42, 49],
        [4, 36, 37, 40, 54, 57],
        [1, 8, 11, 36, 37, 56]]
resultado = []
final = [[], [], [], [], [], []]
conta = []
dic = {'corretas': 0, 'incorretas': 0}
linha(100)
printf('bem vindo ao conferidor de jogos da mega sena', 100)
linha(100)
recebe = str(input('digite o resultado do jogo: '))
for c in range(0, 12, 2):
    resultado.append(int(recebe[c]+recebe[c+1]))
print(f'o resultado do jogo é \033[0;32m{resultado}')
for p, d in enumerate(jogo):
    for e in d:
        if e in resultado:
            final[p].append(f'\033[0;32m{e}')
            dic['corretas'] += 1
        else:
            final[p].append(f'\033[0;31m{e}')
            dic['incorretas'] += 1
    conta.append(dic.copy())
    dic = {'corretas': 0, 'incorretas': 0}
linha(100)
for p, h in enumerate(final):
    print(f'os resultados do {p+1}° jogo foram: [',end='')
    for p2, j in enumerate(h):
        if p2 < len(h)-1:
            print(j, end=', ')
        else:
            print(j, end='')
    print(f'\033[0;93m] com um total de {conta[p]["corretas"]} acertos e {conta[p]["incorretas"]} erros')
linha(100)
printf('obrigado por usar o conferidor V1.0',100)
linha(100)
