# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def recursividade(n, vezes):
    if vezes <= 1:
        return 1 + n
    return recursividade(1 / (2 + n), vezes - 1)


def main():
    n = int(input())
    if not n:
        print('{:.10f}'.format(1.0))
    else:
        print('{:.10f}'.format(recursividade(1/2, n)))


if __name__ == '__main__':
    main()
