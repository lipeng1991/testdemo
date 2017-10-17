# coding=utf-8

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(a):
    print('bar', a)


for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)