def iterable():
    yield 1
    yield 2

def iterable_from():
    yield from iterable()
    yield 3

def iterable_yield():
    yield iterable()
    yield 3
    

for x in iterable_from():
    print(x)

print('------------------------------')

for x in iterable_yield():
    print(x)
print('------------------------------')

def iterable_yield():
    for x in iterable():
        yield x
    yield 3

for x in iterable_yield():
    print(x)


def coroutine():
    x = yield None
    yield 'You sent: %s' % x

c = coroutine()
next(c)
print(c.send('Hello world'))

