def printf(msg,tam=40):
    print(f'{msg:^{tam}}')


def linha(tam=40):
    print('\033[0;94m~\033[0;93m' * tam)


def colorido(cor='branco'):
    print('\033',end='')