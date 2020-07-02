import functools
import pendulum


def logger(func):
    @functools.wraps(func)
    def inner(*args):
        with open('log.txt', 'r') as log:
            try:
                num = int(log.readlines()[-1].split(' : ')[0][1:])
            except IndexError:
                num = 0
        with open('log.txt', 'a') as log:
            now = pendulum.now().to_datetime_string()
            log.write(f'#{num+1} : {func(*args)}')
            log.write(f' [{now}]')
            log.write('\n')
    return inner


@logger
def calculate(expr):
    answer = f'{expr}={eval(expr.replace("^", "**"))}'
    answer = answer.replace(' ', '')
    return answer


def main():
    SIGNS = ['+', '-', '/', '*', '^']
    print(f'Available operators: {", ".join(SIGNS)}')
    expr = input('Enter an expression: ')
    ops = 0

    for i in SIGNS:
        if i in expr:
            ops += 1

    if ops > 0:
        try:
            result = calculate(expr)
            print(result)
        except SyntaxError:
            print('Wrong expression!')


main()

