import math


def fibonacci():
    current = 1
    next = 1
    while (True):
        yield current
        next += current
        current = next - current


def primes():
    current = 2
    while (True):
        if check_prime(current):
            yield current
        current += 1


def alphabet(*, code=None, letters=None):
    if letters:
        _alphabet = letters
    elif code == 'lat':
        _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif code == 'bg':
        _alphabet = 'абвгдежзийклмнопрстуфхцчшщъьюя'
    else:
        _alphabet = 'wtf'

    for index in range(len(_alphabet)):
        yield _alphabet[index]


def intertwined_sequences(iterable, *, generator_definitions={}):
    generator_definitions.update({
        'fibonacci': fibonacci,
        'primes': primes,
        'alphabet': alphabet
    })
    cache = {}
    for generator_data in iterable:
        sequence = generator_data.pop("sequence")
        length = generator_data.pop("length")
        if sequence not in cache:
            cache[sequence] = iter(
                generator_definitions[sequence](**generator_data))
        generator = cache[sequence]
        for index in range(length):
            yield next(generator)


# Helper functions


def check_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
